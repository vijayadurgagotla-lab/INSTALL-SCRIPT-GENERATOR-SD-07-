
from flask import Flask, request, jsonify, render_template
import uuid
from db import get_connection, init_db
from agent import get_groq_response, validate_script

app = Flask(__name__)
init_db()

def save_message(session_id, role, content):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
        (session_id, role, content)
    )
    conn.commit()
    conn.close()

def get_history(session_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT role, content FROM messages WHERE session_id=? ORDER BY created_at ASC",
        (session_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return [{"role": r["role"], "content": r["content"]} for r in rows]

def ensure_session(session_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO sessions (session_id) VALUES (?)",
        (session_id,)
    )
    conn.commit()
    conn.close()

@app.route("/")
def index():
    session_id = str(uuid.uuid4())
    return render_template("index.html", session_id=session_id)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data["message"]
    session_id = data["session_id"]
    ensure_session(session_id)
    save_message(session_id, "user", user_msg)
    history = get_history(session_id)
    reply = get_groq_response(history)
    save_message(session_id, "assistant", reply)
    return jsonify({"reply": reply})

# Step 5 — Validate route
@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    script = data["script"]
    result = validate_script(script)
    return jsonify({"reply": result})

if __name__ == "__main__":
    app.run(debug=True)

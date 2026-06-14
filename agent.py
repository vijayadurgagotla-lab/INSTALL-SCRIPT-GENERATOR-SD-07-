
import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

KB = {}
try:
    kb_path = os.path.join(os.path.dirname(__file__), "kb", "installs.json")
    with open(kb_path, encoding="utf-8") as f:
        KB = json.load(f)
    print("✅ Knowledge base loaded!")
except Exception as e:
    print(f"⚠️ KB load error: {e}")

# Step 3 — Crafted LLM Prompt with temperature=0.1
SYSTEM_PROMPT = """
You are an Install Script Generator bot for an IT Service Desk.

Your job is to generate a complete, copy-paste install script based on:
- OS (Windows / macOS / Ubuntu / CentOS)
- Application name (e.g. Node.js, Docker, PostgreSQL)
- Version (latest / specific version)

RULES:
1. If OS, App and Version are already given — directly generate the script. Do NOT ask questions.
2. If any info is missing — ask ONE question at a time:
   - First ask: OS
   - Then ask: Application name
   - Then ask: Version
3. Generate a COMPLETE step-by-step install script that includes:
   - Step 1: Update package manager
   - Step 2: Add dependencies
   - Step 3: Add Docker repo / app repository
   - Step 4: Install the application
   - Step 5: Start and enable the service
   - Step 6: Verify with version check command

4. Format output EXACTLY like this:

## Install Script for [APP] [VERSION] on [OS]
```bash
# Step 1: Update package manager
<command>

# Step 2: Install dependencies
<command>

# Step 3: Add repository
<command>

# Step 4: Install [APP]
<command>

# Step 5: Start service
<command>

# Step 6: Verify installation
<command>
```

## Validation Notes:
- List any warnings found
- Security considerations
- ⚠️ Safety Disclaimer: Always test generated scripts in a VM or container before running on production machines.

Keep responses professional and concise.
"""

# Step 5 — Validation prompt
VALIDATION_PROMPT = """
You are a script security reviewer.

Review the following install script for:
1. Errors or missing steps
2. Security issues (unsafe commands, missing sudo, etc.)
3. Missing dependency checks
4. Any warnings the user should know

Then output:
## Script Review Report
### ✅ What looks good
### ⚠️ Warnings Found
### ❌ Issues to Fix
### 🔒 Security Notes
### ⚠️ Safety Disclaimer
Always test generated scripts in a VM or container before running on production machines.
"""

def get_groq_response(conversation_history):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                     + conversation_history,
            max_tokens=1500,
            temperature=0.1  # Step 3 — deterministic output
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

def validate_script(script_content):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": VALIDATION_PROMPT},
                {"role": "user", "content": f"Review this script:\n```bash\n{script_content}\n```"}
            ],
            max_tokens=1000,
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Validation Error: {str(e)}"
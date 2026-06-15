
# Script Generator

## Project Overview

AI Script Generator is a Generative AI-based application that automatically creates software installation and configuration scripts based on user requirements.

The application uses an AI Agent with a domain-specific Knowledge Base to understand user requests, retrieve relevant information, and generate customized installation scripts.

The main objective of this project is to reduce manual scripting effort, minimize configuration errors, and simplify software deployment through AI-powered automation.

---

Live Demo
https://www.loom.com/share/77d82a84008f4053847b6f9cfea1214a
Generate your API key to run this project.


# Features

* AI-powered installation script generation
* Natural language based user interaction
* Automated script creation from user requirements
* Knowledge Base integration for accurate information retrieval
* AI Agent for intelligent decision-making
* Script storage and history management using SQLite database
* User-friendly web interface
* Flask-based backend API
* Support for customizable installation requirements

---

# How It Works

```
User Requirement
        |
        ↓
Web Interface
        |
        ↓
Flask Backend
        |
        ↓
AI Agent
        |
        ↓
Knowledge Base
        |
        ↓
Generated Installation Script
        |
        ↓
SQLite Database Storage
```

### Workflow:

1. User enters software installation requirements.
2. Flask receives and processes the request.
3. AI Agent analyzes the user requirement.
4. Relevant information is retrieved from the Knowledge Base.
5. AI generates a customized installation script.
6. The generated script is stored in SQLite database.
7. The final script is displayed to the user.

---

# Technology Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python
* Flask

## Database

* SQLite

## AI Components

* Large Language Model (LLM)
* AI Agent
* Knowledge Base Retrieval

---

# AI Model

The application uses a Large Language Model to generate intelligent and customized scripts.

## Model Used:

```
Llama 3.3 70B Versatile
```

### AI Model Responsibilities:

* Understand user requirements
* Generate installation commands
* Customize scripts according to requirements
* Provide structured script output
* Improve automation and accuracy

---

# Project Architecture

```
                    User
                      |
                      ↓
              Web Interface
                      |
                      ↓
              Flask Application
                      |
          -----------------------
          |                     |
          ↓                     ↓
      AI Agent            SQLite Database
          |
          ↓
   Knowledge Base
   (installs.json)
          |
          ↓
 Generated Installation Script
```

---

# Folder Structure

```
AI-Script-Generator/

│
├── app.py                 # Flask application entry point
│
├── agent.py               # AI agent and script generation logic
│
├── db.py                  # Database operations
│
├── requirements.txt       # Project dependencies
│
├── install_gen.db         # SQLite database
│
├── templates/
│      └── index.html      # User interface
│
├── static/
│      └── style.css       # Frontend styling
│
└── kb/
       └── installs.json   # Knowledge Base
```

---

# Installation and Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

## 2. Navigate to Project Directory

```bash
cd AI-Script-Generator
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows:

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run Application

```bash
python app.py
```

## 7. Open Browser

```
http://127.0.0.1:5000
```

---

# Database

SQLite database is used to store generated scripts and user interaction details.

Database:

```
install_gen.db
```

## Database Table

### scripts

| Column           | Description                 |
| ---------------- | --------------------------- |
| id               | Unique script identifier    |
| user_input       | User requirement            |
| generated_script | AI generated script         |
| created_at       | Script generation timestamp |

---

# Knowledge Base

The Knowledge Base contains installation-related information used by the AI Agent.

Example:

```
kb/
 |
 └── installs.json
```

The AI Agent retrieves relevant information from this knowledge source to generate accurate scripts.

---
## AI Model

Provider:
Groq API

Model:
llama-3.3-70b-versatile

Purpose:
- Understand user requirements
- Generate installation scripts
- Provide customized outputs

# Assumptions

* User provides valid installation requirements.
* Required software information exists in the Knowledge Base.
* Generated scripts may require verification before execution.

---

# Limitations

* Accuracy depends on available Knowledge Base information.
* Complex installation scenarios may require additional customization.
* Generated scripts should be tested before production usage.

---

# Future Enhancements

* Add support for more software packages
* Add multiple operating system support
* Implement user authentication
* Deploy application on cloud platforms
* Improve AI reasoning capabilities
* Add script export options (PDF/TXT)
* Add script version management
* Expand Knowledge Base dynamically

---

# Conclusion

AI Script Generator demonstrates the use of Generative AI and intelligent automation for simplifying software installation tasks.

By combining an AI Agent, Knowledge Base, and Large Language Model, the system provides a scalable solution for automatic script generation and configuration assistance.

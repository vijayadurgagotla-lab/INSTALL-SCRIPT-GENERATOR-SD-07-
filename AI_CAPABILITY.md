# AI Capability Demonstration

## External API / Service Integration

The application integrates with the Groq API to access a Large Language Model (LLM) for generating customized installation scripts.

## AI Model Used

- Provider: Groq API
- Model: llama-3.3-70b-versatile

## Workflow

User Requirement
        |
        ↓
Web Interface
        |
        ↓
Flask Backend
        |
        ↓
Groq API
        |
        ↓
Llama 3.3 70B Versatile Model
        |
        ↓
Generated Installation Script
        |
        ↓
SQLite Database Storage


## Implementation Details

1. User enters installation requirements through the web interface.
2. Flask backend receives the request.
3. The request is sent to the Groq API.
4. The Llama model processes the requirement and generates a script.
5. The generated response is displayed to the user and stored in SQLite.

## Capability Demonstrated

This project demonstrates:

- External API / Service Integration
- Large Language Model usage
- AI-powered content generation
- Automated script generation 
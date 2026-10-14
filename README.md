# AI Workflow Automation Platform

A web-based project focused on automating everyday tasks using AI. The goal is to build a platform that can help with tasks like email generation, document understanding, report creation, and workflow automation through a simple web interface.

## About the Project

The idea behind this project is to bring different AI-powered tasks together in one place instead of handling them manually.

I'm building the project step by step, starting with the frontend and backend, then moving towards AI integration and more advanced features. The aim is to understand how each part works and build a platform that can be extended as new features are added.

The project is currently in its initial development stage.

## What I'm Building

- A web interface for AI-powered task automation.
- REST APIs using Python and FastAPI.
- An email generator with options for recipient, purpose, and writing tone.
- AI integration for generating useful and context-aware responses.
- Document processing and question answering using Retrieval-Augmented Generation (RAG).
- Vector search for retrieving relevant information from documents.
- Multi-agent workflows for handling tasks that involve multiple steps.
- Report generation and other automation features.
- Containerization and deployment using Docker.

## Technologies

| Technology | Usage |
|---|---|
| Python | Backend logic |
| FastAPI | Building REST APIs |
| HTML | Webpage structure |
| CSS | Styling and responsive design |
| JavaScript | Frontend functionality and API requests |
| OpenAI API | Planned AI model integration |
| LangChain | Planned LLM integration and orchestration |
| Pinecone | Planned vector search |
| Docker | Planned containerization |

## Current Progress

The initial backend and frontend structure are in place.

- Created a FastAPI application.
- Added a health check endpoint to check whether the backend is running.
- Built an email generation API that accepts the recipient, email purpose, and writing tone.
- Added request validation using Pydantic.
- Created the initial web interface using HTML, CSS, and JavaScript.
- Designed a two-column layout with an email form and an output panel.

At the moment, the email API uses a Python template to generate its response. Connecting the frontend to the backend and integrating a real AI model are the next steps.

## Project Structure

AI_automation_workflow/
│
├── main.py
├── test_openai.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js

The `venv/` directory is used for the local Python environment and should not be uploaded to GitHub. The `.env` file contains local configuration and secrets, so it should also remain private.

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git
- Visual Studio Code or another code editor
- A modern web browser

### 1. Clone the repository

bash
git clone <https://github.com/divya-tiwari2005/ai_workflow_automation.git>
cd AI_automation_workflow

### 2. Create a virtual environment

bash
python -m venv venv

On Windows PowerShell, activate it using:

powershell
.\venv\Scripts\Activate.ps1


### 3. Install dependencies

If requirements.txt is available, run:

bash
pip install -r requirements.txt

Otherwise, install FastAPI and its standard dependencies:

bash
pip install "fastapi[standard]"

### 4. Run the backend

From the project root, run:

bash
fastapi dev main.py

Once the server starts, you can access:

- API: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

Keep the backend running while using the application.

### 5. Run the frontend

Open frontend/index.html using the Live Server extension in VS Code.

Alternatively, if Node.js is installed, you can start a local server with:

bash
npx http-server frontend -p 5500

Then open http://127.0.0.1:5500 in your browser.

The frontend and backend run separately during local development. If the browser blocks API requests because of CORS, the backend will need to be configured to allow the frontend's local origin.

## API Endpoints

### Health Check

Method: GET

Endpoint: /health

Checks whether the backend is responding.

Example:

bash
curl http://127.0.0.1:8000/health

### Generate Email

Method: POST

Endpoint: /generate-email

Accepts the recipient, purpose, and tone of an email.

Example request:

json
{
  "recipient": "HR Manager",
  "purpose": "Applying for a Python developer role",
  "tone": "professional"
}

The endpoint validates the input and returns an email generated using the current Python template. Real AI-based generation will be added in a later stage.

## What's Next?

The next development steps include:

- Completing and testing communication between the frontend and backend.
- Integrating a real AI model, preferably a locally hosted model initially to avoid per-request API costs.
- Improving email generation with AI.
- Adding document processing and RAG.
- Implementing vector search using Pinecone.
- Building multi-agent workflows.
- Adding report generation and more automation features.
- Improving testing, error handling, logging, and security.
- Containerizing the application with Docker.
- Preparing the platform for deployment.

## Configuration and Security

API keys and other sensitive configuration values should be stored in environment variables rather than directly in the source code.

The .env file and venv/ directory should be excluded through .gitignore. An .env.example file can be used to show the required configuration variables without exposing actual credentials.

Before deployment, the application will also need appropriate authentication, authorization, input validation, rate limiting, and error handling.

## Project Goal

The long-term goal is to develop a platform where users can run different AI-powered workflows from one place. This includes generating content, working with documents, creating reports, and automating tasks that would otherwise require repetitive manual effort.

The project is being developed incrementally, with a focus on understanding the architecture and implementing each component properly.

## License

A license has not been added yet. A suitable license will be selected if the project is intended to be reused or distributed as open-source software.

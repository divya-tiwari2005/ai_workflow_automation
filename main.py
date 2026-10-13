
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Workflow Automation Platform")


class EmailRequest(BaseModel):
    recipient: str
    purpose: str
    tone: str = "professional"


@app.get("/health")
def health_check():
    return {"status": "running"}


@app.post("/generate-email")
def generate_email(request: EmailRequest):
    return {
        "message": "Email generation endpoint is working",
        "recipient": request.recipient,
        "purpose": request.purpose,
        "tone": request.tone,
        "generated_email": (
            f"Dear {request.recipient},\n\n"
            f"I am writing regarding {request.purpose}.\n\n"
            "Best regards"
        ),
    }

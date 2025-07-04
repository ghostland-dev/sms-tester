from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

STORAGE_FILE = "sms_storage.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SMSMessage(BaseModel):
    id: UUID
    to: str
    from_: str = Field(..., alias="from")
    message: str
    timestamp: str

    class Config:
        populate_by_name = True

class SMSRequest(BaseModel):
    to: str
    from_: str = Field(..., alias="from")
    message: str

    class Config:
        populate_by_name = True

def load_messages() -> List[SMSMessage]:
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
            return [SMSMessage(**msg) for msg in data]
    return []

def save_messages(messages: List[SMSMessage]):
    with open(STORAGE_FILE, "w") as f:
        json.dump([
            {**msg.model_dump(by_alias=True), "id": str(msg.id)} for msg in messages
        ], f, indent=2)

messages: List[SMSMessage] = load_messages()

@app.post("/sms/send", response_model=SMSMessage)
def send_sms(sms: SMSRequest):
    msg = SMSMessage(
        id=uuid4(),
        to=sms.to,
        from_=sms.from_,
        message=sms.message,
        timestamp=datetime.utcnow().isoformat()
    )
    messages.append(msg)
    save_messages(messages)
    return msg

@app.get("/sms/inbox", response_model=List[SMSMessage])
def get_inbox():
    return messages

@app.get("/sms/inbox/{phone}", response_model=List[SMSMessage])
def get_inbox_for_phone(phone: str):
    filtered = [msg for msg in messages if msg.to == phone]
    return filtered

@app.post("/sms/reset")
def reset_inbox():
    global messages
    messages = []
    save_messages(messages)
    return {"status": "reset"} 
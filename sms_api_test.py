import pytest
from fastapi.testclient import TestClient
from sms_api import app

client = TestClient(app)

def test_send_and_inbox():
    # Reset inbox
    r = client.post('/sms/reset')
    assert r.status_code == 200
    # Send SMS
    resp = client.post('/sms/send', json={
        "to": "+33600000001",
        "from": "PYTEST",
        "message": "pytest message"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["to"] == "+33600000001"
    assert data["from"] == "PYTEST"
    # Inbox
    inbox = client.get('/sms/inbox').json()
    assert any(sms["message"] == "pytest message" for sms in inbox)
    # Filter by phone
    filtered = client.get('/sms/inbox/+33600000001').json()
    assert any(sms["from"] == "PYTEST" for sms in filtered) 
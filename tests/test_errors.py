from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_escalate_conversation():
    response = client.post(
        "/escalate",
        json={
            "conversation_id": "ticket-test-001",
            "reason": "Automated test escalation"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["conversation_id"] == "ticket-test-001"
    assert data["status"] == "ESCALATED"
    assert data["reason"] == "Automated test escalation"


def test_invalid_order_id():
    response = client.get("/orders/99999")

    assert response.status_code == 404

    data = response.json()

    assert "not found" in data["detail"].lower()
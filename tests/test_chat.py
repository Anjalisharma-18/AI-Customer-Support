from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_chat_order_status():
    response = client.post(
        "/chat",
        json={
            "message": "What is the status of my order 45821?",
            "conversation_id": "automated-chat-test-001",
            "customer_id": "customer-001"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["intent"] == "order_status"
    assert data["source"] == "order_database"
    assert "45821" in data["answer"]
    assert "SHIPPED" in data["answer"]
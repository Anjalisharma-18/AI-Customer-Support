from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_conversation_memory():
    conversation_id = "automated-memory-test-001"

    first_response = client.post(
        "/chat",
        json={
            "message": "My order number is 45821",
            "conversation_id": conversation_id,
            "customer_id": "customer-001"
        }
    )

    assert first_response.status_code == 200

    first_data = first_response.json()

    assert first_data["context"]["order_id"] == "45821"

    second_response = client.post(
        "/chat",
        json={
            "message": "When will it arrive?",
            "conversation_id": conversation_id,
            "customer_id": "customer-001"
        }
    )

    assert second_response.status_code == 200

    second_data = second_response.json()

    assert second_data["intent"] == "delivery_status"
    assert "45821" in second_data["answer"]
    assert second_data["source"] == "order_database"
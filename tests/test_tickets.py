from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_create_ticket():
    response = client.post(
        "/tickets",
        json={
            "customer_id": "customer-001",
            "issue": "Test ticket from automated test",
            "category": "TEST",
            "priority": "LOW"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["customer_id"] == "customer-001"
    assert data["issue"] == "Test ticket from automated test"
    assert data["category"] == "TEST"
    assert data["priority"] == "LOW"
    assert data["status"] == "OPEN"
    assert data["ticket_id"]
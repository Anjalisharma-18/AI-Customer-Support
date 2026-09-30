from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_order():
    response = client.get("/orders/45821")

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["order_id"] == "45821"
    assert data["customer_id"] == "customer-001"
    assert data["status"] == "SHIPPED"
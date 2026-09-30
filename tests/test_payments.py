from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_payment():
    response = client.get("/payments/45821")

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["payment_id"] == "PAY45821"
    assert data["order_id"] == "45821"
    assert data["status"] == "SUCCESS"
    assert data["payment_method"] == "UPI"
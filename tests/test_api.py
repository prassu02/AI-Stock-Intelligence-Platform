import sys
import os

sys.path.append(os.path.abspath("."))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_predict():
    response = client.get("/predict/AAPL")
    assert response.status_code == 200
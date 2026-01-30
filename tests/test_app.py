import pytest
from app import app  # Import your Flask app instance

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    # Check for key content from your index.html
    assert b"California Housing Price Predictor" in response.data
    assert b"Median Income (MedInc)" in response.data  # One of your labels

def test_prediction_route_success(client):
    form_data = {
        "MedInc": "8.32",
        "AveRooms": "6.0",
        "HouseAge": "30.0",
        "Latitude": "37.88",
        "Longitude": "-122.23"
    }
    response = client.post("/predict", data=form_data)
    assert response.status_code == 200
    # Check for success message (adjust based on your exact output)
    assert b"Predicted Median House Value:" in response.data
    assert b"$" in response.data  # Should have dollar sign

def test_prediction_invalid_input(client):
    form_data = {
        "MedInc": "abc",  # invalid number
        "AveRooms": "6.0",
        "HouseAge": "30.0",
        "Latitude": "37.88",
        "Longitude": "-122.23"
    }
    response = client.post("/predict", data=form_data)
    assert response.status_code == 200  # Your route returns 200 on error
    assert b"Error:" in response.data   # Assuming you render error in template
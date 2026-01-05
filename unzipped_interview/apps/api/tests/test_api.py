import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pagination_is_stable():
    """Test that pagination doesn't return duplicate items across pages."""
    # Fetch page 1
    response1 = client.get("/tasks?page=1&limit=10")
    data1 = response1.json().get("data") or response1.json().get("items")
    ids1 = [t["id"] for t in data1]
    
    # Fetch page 2
    response2 = client.get("/tasks?page=2&limit=10")
    data2 = response2.json().get("data") or response2.json().get("items")
    ids2 = [t["id"] for t in data2]
    
    # Check for duplicates
    duplicates = set(ids1).intersection(set(ids2))
    assert not duplicates, f"Duplicate items found across pages: {duplicates}"

def test_pagination_correct_slice():
    """Test that pagination returns the correct number of items and correct slice."""
    limit = 5
    response = client.get(f"/tasks?page=1&limit={limit}")
    data = response.json().get("data") or response.json().get("items")
    assert len(data) == limit, f"Expected {limit} items, got {len(data)}"
    
    # Page 2 should start from the next item
    response2 = client.get(f"/tasks?page=2&limit={limit}")
    data2 = response2.json().get("data") or response2.json().get("items")
    assert data[0]["id"] != data2[0]["id"], "Page 1 and Page 2 start with the same item"

def test_integration_contract():
    """Test that the API returns the expected data structure."""
    response = client.get("/tasks")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data, "Response missing 'data' key (Integration Mismatch)"
    assert isinstance(json_data["data"], list)

def test_suggestion_complexity():
    """Test that the suggestion engine is efficient."""
    query = "Task 1"
    response = client.post("/suggestions", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    
    # Threshold for 100 tasks: 
    # Efficient: ~100-200 ops
    # Naive: ~100 tasks * 2 fields * 2 words = 400+ ops
    assert data["operations"] < 300, f"Too many operations: {data['operations']}. Suggests O(N*M) complexity."

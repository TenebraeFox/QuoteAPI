import pytest
from fastapi.testclient import TestClient
from main import app
import sqlite3

client = TestClient(app)

# Test if the FastAPI app is running
def test_app():
    response = client.get("/")
    assert response.status_code == 200

# Test if the quotes endpoint is accessible and returns a valid response
def test_get_quotes():
    response = client.get("/quotes")
    assert response.status_code == 200
    # Assuming the quote is returned in a proper format
    assert "id" in response.json()
    assert "text" in response.json()

# Test if the database can be accessed (simple query)
def test_database_connection():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM quotes')
    result = cursor.fetchone()
    conn.close()
    assert result is not None

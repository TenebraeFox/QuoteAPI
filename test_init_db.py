import pytest
import sqlite3
from init_db import create_table, get_random_quote

# Test if the table is created successfully
def test_create_table():
    create_table()
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='quotes'")
    table_exists = cursor.fetchone()
    conn.close()
    assert table_exists is not None

# Test if a random quote can be retrieved (assuming there is data)
def test_get_random_quote():
    create_table()
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    # Insert a test quote into the table for testing
    cursor.execute("INSERT INTO quotes (text, author, theme) VALUES ('Test Quote', 'Test Author', 'Test Theme')")
    conn.commit()
    conn.close()

    # Now test if the random quote can be fetched
    random_quote = get_random_quote()
    assert random_quote is not None
    assert "text" in random_quote
    assert "author" in random_quote

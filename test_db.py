import sqlite3


def test_check_user_in_db():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = 'standard_user'")

    result = cursor.fetchone()

    assert result == (1, 'standard_user', 'customer')
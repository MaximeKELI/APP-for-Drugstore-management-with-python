from db import connect

def add_customer(name, email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Customers (name, email)
    VALUES (?, ?)""", (name, email))
    conn.commit()
    conn.close()

def get_customer_by_email(email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers WHERE email = ?", (email,))
    customer = cursor.fetchone()
    conn.close()
    return customer

def update_loyalty_points(customer_id, points):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE Customers
    SET loyalty_points = loyalty_points + ?
    WHERE id = ?""", (points, customer_id))
    conn.commit()
    conn.close()

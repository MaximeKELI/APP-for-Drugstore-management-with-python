from db import connect

def add_product(name, category, price, stock_quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Products (name, category, price, stock_quantity)
    VALUES (?, ?, ?, ?)""", (name, category, price, stock_quantity))
    conn.commit()
    conn.close()

def update_product_stock(product_id, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE Products
    SET stock_quantity = stock_quantity + ?
    WHERE id = ?""", (quantity, product_id))
    conn.commit()
    conn.close()

def get_all_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

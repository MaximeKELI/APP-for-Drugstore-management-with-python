from db import connect
from datetime import datetime

def record_sale(product_id, customer_id, quantity):
    product = get_product_by_id(product_id)
    if product:
        total = product[3] * quantity  # price * quantity
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Sales (product_id, customer_id, quantity, total, date)
        VALUES (?, ?, ?, ?, ?)""", (product_id, customer_id, quantity, total, datetime.now()))
        update_product_stock(product_id, -quantity)  # Update stock
        conn.commit()
        conn.close()
        print(f"Sale recorded: {quantity} x {product[1]} for {total} USD.")
    else:
        print("Product not found!")

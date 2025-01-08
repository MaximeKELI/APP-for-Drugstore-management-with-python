from db import connect
from datetime import datetime

def create_order(product_id, quantity, supplier):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Orders (product_id, quantity, supplier, status, date)
    VALUES (?, ?, ?, ?, ?)""", (product_id, quantity, supplier, "Pending", datetime.now()))
    conn.commit()
    conn.close()
    print(f"Order created for {quantity} units of product {product_id} from {supplier}.")

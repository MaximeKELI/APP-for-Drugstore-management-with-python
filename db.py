import sqlite3

def connect():
    conn = sqlite3.connect("drugstore.db")
    return conn

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    # Table Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL
    )""")
    
    # Table Customers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        loyalty_points INTEGER DEFAULT 0
    )""")
    
    # Table Sales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        customer_id INTEGER,
        quantity INTEGER,
        total REAL,
        date TEXT,
        FOREIGN KEY (product_id) REFERENCES Products(id),
        FOREIGN KEY (customer_id) REFERENCES Customers(id)
    )""")
    
    # Table Orders
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        supplier TEXT,
        status TEXT,
        date TEXT,
        FOREIGN KEY (product_id) REFERENCES Products(id)
    )""")
    
    conn.commit()
    conn.close()

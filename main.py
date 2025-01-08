from db import create_tables
from product import add_product, get_all_products
from customer import add_customer
from sale import record_sale
from order import create_order

def main():
    create_tables()
    
    # Example: Adding products
    add_product("Aspirin", "Medication", 10.0, 100)
    add_product("Toothpaste", "Personal Care", 3.5, 50)
    
    # Example: Adding a customer
    add_customer("John Doe", "john.doe@example.com")
    
    # Example: Recording a sale
    record_sale(1, 1, 2)  # Sale of 2 Aspirins to John Doe
    
    # Example: Creating an order for stock replenishment
    create_order(2, 50, "PharmaCorp")
    
    # Display all products
    products = get_all_products()
    for product in products:
        print(product)

if __name__ == "__main__":
    main()

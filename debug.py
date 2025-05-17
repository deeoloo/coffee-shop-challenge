from customer import Customer
from coffee import Coffee
from order import Order

def print_header(title):
    print(f"\n{'='*30}")
    print(f"{title.upper():^30}")
    print(f"{'='*30}")

def test_initialization():
    print_header("Initialization Tests")
    
    # Valid cases
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    print(f"✓ Customer initialized: {customer.name}")
    print(f"✓ Coffee initialized: {coffee.name}")
    print(f"✓ Order initialized: ${order.price} {order.coffee.name} for {order.customer.name}")

    # Invalid cases
    try:
        Customer("")  # Should fail
    except Exception as e:
        print(f"✓ Invalid customer name caught: {e}")

    try:
        Coffee("A")  # Should fail
    except Exception as e:
        print(f"✓ Invalid coffee name caught: {e}")

    try:
        Order(customer, coffee, 11.0)  # Should fail
    except Exception as e:
        print(f"✓ Invalid order price caught: {e}")

def test_relationships():
    print_header("Relationship Tests")
    
    # Setup
    customers = [Customer(n) for n in ["Alice", "Bob", "Charlie"]]
    coffees = [Coffee(n) for n in ["Latte", "Cappuccino", "Espresso"]]
    
    orders = [
        Order(customers[0], coffees[0], 5.0),
        Order(customers[0], coffees[1], 4.5),
        Order(customers[1], coffees[0], 6.0),
        Order(customers[2], coffees[2], 3.5),
        Order(customers[0], coffees[0], 4.0)  # Alice orders Latte again
    ]
    
    # Test customer relationships
    alice = customers[0]
    print(f"\nAlice's orders ({len(alice.orders())}):")
    for order in alice.orders():
        print(f"- {order.coffee.name} (${order.price})")
    
    print(f"\nAlice's unique coffees ({len(alice.coffees())}):")
    for coffee in alice.coffees():
        print(f"- {coffee.name}")

    # Test coffee relationships
    latte = coffees[0]
    print(f"\nLatte orders ({latte.num_orders()}):")
    print(f"- Average price: ${latte.average_price():.2f}")
    print(f"- Customers ({len(latte.customers())}):")
    for customer in latte.customers():
        print(f"  - {customer.name}")

def test_immutability():
    print_header("Immutability Tests")
    
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    try:
        coffee.name = "Mocha"
    except Exception as e:
        print(f"✓ Coffee name immutability enforced: {e}")
    
    try:
        order.price = 6.0
    except Exception as e:
        print(f"✓ Order price immutability enforced: {e}")

def test_bonus_methods():
    print_header("Bonus Methods Test")
    
    # Setup
    coffee = Coffee("Special Blend")
    customers = [Customer(n) for n in ["Big Spender", "Medium Spender", "Small Spender"]]
    
    orders = [
        Order(customers[0], coffee, 10.0),  # Big Spender
        Order(customers[0], coffee, 10.0),  # Big Spender again
        Order(customers[1], coffee, 7.5),   # Medium Spender
        Order(customers[2], coffee, 5.0)    # Small Spender
    ]
    
    top_customer = Customer.most_aficionado(coffee)
    print(f"Top customer for {coffee.name}: {top_customer.name} (Total spent: ${sum(o.price for o in orders if o.customer == top_customer)})")

def run_all_tests():
    test_initialization()
    test_relationships()
    test_immutability()
    test_bonus_methods()
    print_header("All Tests Complete")

if __name__ == "__main__":
    run_all_tests()
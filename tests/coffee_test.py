from customer import Customer
from coffee import Coffee
from order import Order
import pytest

def test_coffee_init():
    """Test Coffee class initializes with name"""
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_is_string():
    """Test Coffee class validates name is string"""
    with pytest.raises(Exception):
        Coffee(123)

def test_coffee_name_length():
    """Test Coffee class validates name is at least 3 characters"""
    with pytest.raises(Exception):
        Coffee("a")
    Coffee("abc") 

def test_coffee_name_immutable():
    """Test Coffee name cannot be changed after initialization"""
    coffee = Coffee("Latte")
    with pytest.raises(Exception):
        coffee.name = "Mocha"

def test_coffee_has_orders():
    """Test Coffee class has method orders() that returns list of its orders"""
    coffee = Coffee("Latte")
    customer = Customer("Steve")
    order = Order(customer, coffee, 5.0)
    
    assert order in coffee.orders()

def test_coffee_has_customers():
    """Test Coffee class has method customers() that returns unique list of customers"""
    coffee = Coffee("Latte")
    customer1 = Customer("Steve")
    customer2 = Customer("Alice")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 6.0)  # Same customer
    Order(customer2, coffee, 4.5)  # Different customer
    
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_coffee_num_orders():
    """Test Coffee class has method num_orders() that returns count of orders"""
    coffee = Coffee("Latte")
    customer = Customer("Steve")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 6.0)
    
    assert coffee.num_orders() == 2
    assert Coffee("New").num_orders() == 0

def test_coffee_average_price():
    """Test Coffee class has method average_price() that returns mean price"""
    coffee = Coffee("Latte")
    customer = Customer("Steve")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 7.0)
    
    assert coffee.average_price() == 6.0
    assert Coffee("New").average_price() == 0
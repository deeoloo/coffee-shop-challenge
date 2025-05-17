from customer import Customer
from coffee import Coffee
from order import Order
import pytest

def test_order_init():
    """Test Order class initializes with customer, coffee, price"""
    customer = Customer("Steve")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_validates_customer():
    """Test Order class validates customer is Customer instance"""
    coffee = Coffee("Latte")
    with pytest.raises(Exception):
        Order("Not a customer", coffee, 5.0)

def test_order_validates_coffee():
    """Test Order class validates coffee is Coffee instance"""
    customer = Customer("Steve")
    with pytest.raises(Exception):
        Order(customer, "Not a coffee", 5.0)

def test_order_validates_price():
    """Test Order class validates price is float between 1.0 and 10.0"""
    customer = Customer("Steve")
    coffee = Coffee("Latte")
    
    with pytest.raises(Exception):
        Order(customer, coffee, 0.99)  # Too low
    with pytest.raises(Exception):
        Order(customer, coffee, 10.01)  # Too high
    with pytest.raises(Exception):
        Order(customer, coffee, "five")  # Not float
    Order(customer, coffee, 1.0)  # Edge cases should pass
    Order(customer, coffee, 10.0)

def test_order_price_immutable():
    """Test Order price cannot be changed after initialization"""
    customer = Customer("Steve")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    with pytest.raises(Exception):
        order.price = 6.0
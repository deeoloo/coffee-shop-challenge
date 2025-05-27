from customer import Customer
from coffee import Coffee
from order import Order
import pytest

def test_customer_init():
    """Test Customer class initializes with name"""
    customer = Customer("Steve")
    assert customer.name == "Steve"

def test_customer_name_is_string():
    """Test Customer class validates name is string"""
    with pytest.raises(Exception):
        Customer(123)

def test_customer_name_length():
    """Test Customer class validates name length 1-15 characters"""
    with pytest.raises(Exception):
        Customer("")
    with pytest.raises(Exception):
        Customer("ThisNameIsWayTooLong")
    Customer("Bob") 

def test_customer_has_orders():
    """Test Customer class has method orders() that returns list of its orders"""
    customer = Customer("Steve")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order in customer.orders()

def test_customer_has_coffees():
    """Test Customer class has method coffees() that returns unique list of coffees"""
    customer = Customer("Steve")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    Order(customer, coffee1, 5.0)
    Order(customer, coffee1, 6.0)  # Same coffee
    Order(customer, coffee2, 4.5)  # Different coffee
    
    assert len(customer.coffees()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_customer_create_order():
    """Test Customer class has method create_order() that makes new Order"""
    customer = Customer("Steve")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert order in customer.orders()

def test_customer_most_aficionado():
    """Test Customer class has method most_aficionado() that returns top spender for given coffee"""
    coffee = Coffee("Latte")
    customer1 = Customer("Steve")
    customer2 = Customer("Alice")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 5.0)  # Total $10
    Order(customer2, coffee, 8.0)  # Total $8
    
    assert Customer.most_aficionado(coffee) == customer1
    assert Customer.most_aficionado(Coffee("New")) is None
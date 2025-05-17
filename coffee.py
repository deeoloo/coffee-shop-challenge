from order import Order

class Coffee:
    def __init__(self, name):
        self._name = None  # Initialize before property setter
        self.name = name  # This will use the property setter
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name is not None:
            raise Exception("Coffee name cannot be changed after initialization")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 3:
            raise Exception("Name must be at least 3 characters long")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        from customer import Customer  # Lazy import to avoid circularity
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders)/len(orders) if orders else 0
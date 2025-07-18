from order import Order

class Coffee:
    def __init__(self, name):
        self._name = None  
        self.name = name  
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name is not None:
            raise ValueError("Coffee name cannot be changed after initialization")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        from customer import Customer  
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders)/len(orders) if orders else 0
    




    
from order import Order

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        from coffee import Coffee  
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee 
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide Coffee instance")
            
        customers_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customers_spending:
                    customers_spending[order.customer] += order.price
                else:
                    customers_spending[order.customer] = order.price
        
        return max(customers_spending.items(), key=lambda x: x[1])[0] if customers_spending else None
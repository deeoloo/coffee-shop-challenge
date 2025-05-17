class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        # Initializing the attributes using the property setters
        self._price = None  # Initializing the backing field
        self._customer = None
        self._coffee = None
        
        # Now use the setters
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if hasattr(self, '_price') and self._price is not None:
            raise Exception("Price cannot be changed after initialization")
        if not isinstance(value, float):
            raise Exception("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = value
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer  # Lazy import to avoid circular imports
        if not isinstance(value, Customer):
            raise Exception("customer must be of type Customer")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee  # Lazy import to avoid circular imports
        if not isinstance(value, Coffee):
            raise Exception("coffee must be of type Coffee")
        self._coffee = value
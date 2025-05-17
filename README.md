# ☕ Coffee Shop OOP System

A Python implementation demonstrating object-oriented programming principles through a coffee shop model.

## Key Components

### Core Classes
- **Customer**: Tracks customer details and order history
- **Coffee**: Manages coffee items and sales metrics  
- **Order**: Handles transaction records and validations

## Key Features
✅ Relationship mapping (customers ↔ orders ↔ coffees)  
✅ Attribute validation with proper error handling  
✅ Business logic methods (average price, top customers)  
✅ Immutable properties where required  
✅ Comprehensive test coverage

## Getting Started

1. Clone repo and create virtual environment:
```bash
python -m venv venv && source venv/bin/activate
```

2. Install requirements:
```bash
pip install pytest
```

3. Run tests:
```bash
pytest tests/ -v
```

## Usage Example
```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create objects
customer = Customer("Sarah")
coffee = Coffee("Cold Brew")

# Place order
order = customer.create_order(coffee, 4.5)

# Get insights
print(f"Favorite coffee: {customer.coffees()[0].name}")
print(f"Total orders: {coffee.num_orders()}")
```

## Testing
- Unit tests cover all core functionality
- Run with `pytest tests/`
- Manual tests available in `debug.py`

## Requirements
- Python 3.8+
- pytest (for testing)

---

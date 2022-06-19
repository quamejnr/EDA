from dataclasses import dataclass


@dataclass
class Product:
    """Model for product objects in database"""
    name: str
    price: float
    quantity: int
    
    
@dataclass
class User:
    """Model for user objects in database"""
    name: str
    email: str
    
    
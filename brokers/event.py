from models.model import Product, User
from dataclasses import dataclass


@dataclass
class OrderPlacedEvent:
    event_name: str
    product: Product
    quantity: int
    user: User
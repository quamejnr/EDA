from brokers.broker import notify
from brokers.event import OrderPlacedEvent
from models.model import Product, User


class Producer:
    """Class for producing events."""
    
    async def order_placed(self, product: Product, quantity: int, user: User):
        """Sends an event when an order is placed"""
        event_name = 'order_placed'  
        event = OrderPlacedEvent(event_name=event_name, product=product, quantity=quantity, user=user)
        await notify(event)


from brokers.event import OrderPlacedEvent
from services.listener import Listener
from brokers.broker import subscribe


class DeliveryService(Listener):
    """Service responsible for delivering orders"""
    
    async def handle_order_placed(self, event: OrderPlacedEvent):
        """Handles an order placed event. """
        print("***  Delivery Service  ***")
        print(f"'Product:{event.product.name}, quantity: {event.quantity}' is being delivered to {event.user.name}...\n")
        
    def setup_event_handler(self):
        """Register service to consume event"""
        subscribe("order_placed", self.handle_order_placed)
from brokers.event import OrderPlacedEvent
from services.listener import Listener
from brokers.broker import subscribe
from models.model import User, Product
import asyncio


class EmailNotificationService(Listener):
    """Service responsible for sending Emails"""
    async def handle_order_placed(self, event: OrderPlacedEvent):
        """Handles an order placed event"""
        print("***  Email Service   ***")
        await self._send_email(event)
    
    async def _send_email(self, event: OrderPlacedEvent):
        """Sends email to user"""
        print(f"Sending email to {event.user.email}...\n")
        await asyncio.sleep(3)
        print(f"""Hello {event.user.name},
              Your order 'product name:{event.product.name}, price:{event.product.price}, quantity:{event.quantity}' has been received\n""")
        print("Email sent!!!\n")
        
    def setup_event_handler(self):
        """Register service to consume events."""
        subscribe("order_placed", self.handle_order_placed)
       
    
class SlackNotificationService(Listener):
    """ Service responsible for send slack messages."""
    async def handle_order_placed(self, event: OrderPlacedEvent):
        """ Handles an order placed event. """
        print("***  Slack Service   ***")
        await self._send_slack_message(event)
    
    async def _send_slack_message(self, event: OrderPlacedEvent):
        """Sends slack message to operations. """
        print(f"User: '{event.user.name}' placed an order for 'Product: {event.product.name}, Quantity: {event.quantity}'.\n")
        
    def setup_event_handler(self):
        """Register service to consume events."""
        subscribe("order_placed", self.handle_order_placed)
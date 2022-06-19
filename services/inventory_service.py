from brokers.broker import subscribe
from producers.producer import OrderPlacedEvent
from services.listener import Listener
from models.db import INVENTORY
from models.model import Product
from typing import Union


class InventoryService(Listener):
    """Service responsible for inventory."""
    
    async def handle_order_placed(self, event: OrderPlacedEvent) -> None:
        """Handles an order placed event"""
        print("***  Inventory Service   ***")
        event.product.quantity -= event.quantity
        print(f"Current inventory: {INVENTORY}\n")
            
    def get_product(self, product_name: str, quantity: int) -> Union[None, Product]:
        """Gets product from the database"""
        product = INVENTORY.get(product_name)
        if self._is_out_of_stock(product):
            print(f"Product: '{product_name}' is out of stock")
            return
        if self._is_not_sufficient_stock(product, quantity):
            print(f"You ordered for {quantity} of {product.name}. We only have {product.quantity} in stock")
            return
        return product
        
    def _is_out_of_stock(self, product: str) -> bool:
        """Check if product is in inventory or the quantity is more than one."""
        if product is None:
            return True
        return product.quantity < 1
    
    def _is_not_sufficient_stock(self, product: Product, quantity: int) -> bool:
        """Check if product has more quantity in stock than the quantity being requested."""
        return product.quantity < quantity
        
    def setup_event_handler(self) -> None:
        """Register service to consume events"""
        subscribe("order_placed", self.handle_order_placed)
        
        

from services.inventory_service import InventoryService
from services.user_service import UserService
from producers.producer import Producer


inventory_service = InventoryService()
user_service = UserService()
producer = Producer()

async def buy_product(product_name: str, quantity: int, username: str) -> None:
    """Place an order for product. """
    product = inventory_service.get_product(product_name, quantity)
    if product is None:
        return 
    
    user = user_service.get_user(username=username)
    if user is None:
        user = user_service.create_user(username)
    await producer.order_placed(product=product, quantity=quantity, user=user)
    
    

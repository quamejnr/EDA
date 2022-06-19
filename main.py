from services.delivery_service import DeliveryService
from services.inventory_service import InventoryService
from services.notification_service import EmailNotificationService, SlackNotificationService
import asyncio

from views import buy_product


async def main():
    # Initializing event handlers
    EmailNotificationService().setup_event_handler()
    SlackNotificationService().setup_event_handler()
    InventoryService().setup_event_handler()
    DeliveryService().setup_event_handler()
    
    # TestData
    username = 'johndoe'
    product = 'Playstation 5'
    quantity = 10

    buy_product(product_name=product, quantity=quantity, username=username)

if __name__ == "__main__":
    asyncio.run(main())






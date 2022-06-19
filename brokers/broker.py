import asyncio
from collections import deque
from typing import Callable

SUBSCRIBERS = dict()

def subscribe(event_name: str, function: Callable) -> None:
    """Subscribes new function to event type"""
    SUBSCRIBERS.setdefault(event_name, [])
    SUBSCRIBERS[event_name].append(function)


def unsubscribe(event_name: str, function: Callable) -> None:
    """Unsubscribes new function to event type"""
    if event_name in SUBSCRIBERS:
        SUBSCRIBERS[event_name].remove(function)


async def notify(event) -> None:
    """Notify listeners of event."""
    if event.event_name not in SUBSCRIBERS:
        return
    await asyncio.gather(*[function(event) for function in SUBSCRIBERS[event.event_name]])
    

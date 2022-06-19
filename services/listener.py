from abc import ABC, abstractmethod


class Listener(ABC):

    @abstractmethod
    def setup_event_handler(self):
        pass



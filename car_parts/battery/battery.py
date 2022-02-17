from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, name=None):
        self.name = name + " BATTERY"

    @abstractmethod
    def needs_service(self):
        pass

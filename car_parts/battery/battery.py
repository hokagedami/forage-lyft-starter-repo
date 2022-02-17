from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def needs_service(self):
        pass

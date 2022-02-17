from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, name=None):
        self.name = name + " ENGINE"

    @abstractmethod
    def needs_service(self):
        pass


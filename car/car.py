from abc import ABC


class Car(ABC):
    def __init__(self, name, engine, battery):
        self.name = name
        self.battery = battery
        self.engine = engine

    # @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

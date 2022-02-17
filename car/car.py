from abc import ABC

from car_parts.battery.battery import Battery
from car_parts.engine.engine import Engine
from car_parts.tires.tires import Tires


class Car(ABC):
    def __init__(self, name, engine: Engine, battery: Battery, tires: Tires):
        self.name = name + " CAR"
        self.battery = battery
        self.engine = engine
        self.tires = tires

    # @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self, name, wear_sensor_values):
        if wear_sensor_values is None:
            wear_sensor_values = [0, 0, 0, 0]

        self.name = name + " TIRE"
        self.wear_sensor_values = wear_sensor_values

    @abstractmethod
    def needs_service(self):
        pass

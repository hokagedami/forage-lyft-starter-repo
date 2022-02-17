from abc import ABC

from car_parts.tires.tires import Tires


class CarriganTires(Tires, ABC):
    def __init__(self, wear_sensor_values):
        super().__init__("CARRIGAN", wear_sensor_values)

    def needs_service(self):
        return any(value > 0.9 for value in self.wear_sensor_values)

from abc import ABC

from car_parts.tires.tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, wear_sensor_values):
        super().__init__("CARRIGAN", wear_sensor_values)

    def needs_service(self):
        return sum(self.wear_sensor_values) > 3

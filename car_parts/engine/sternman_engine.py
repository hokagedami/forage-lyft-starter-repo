from abc import ABC
from car_parts.engine.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on=False):
        super().__init__("STERNMAN")
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on

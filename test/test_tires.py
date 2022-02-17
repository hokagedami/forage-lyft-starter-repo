import unittest

from car_parts.tires.carrigan_tire import CarriganTires
from car_parts.tires.octoprime_tire import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_service_sensor_values = [0.9, 0, 0, 1]
        tires = CarriganTires(tire_service_sensor_values)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_service_sensor_values = [0.2, 0.8, 0, 0.1]
        tires = CarriganTires(tire_service_sensor_values)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_service_sensor_values = [0.9, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(tire_service_sensor_values)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_service_sensor_values = [.2, .4, .5, .5]
        tires = OctoprimeTires(tire_service_sensor_values)
        self.assertFalse(tires.needs_service())

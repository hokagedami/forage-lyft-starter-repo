from datetime import date

from car_parts.battery.nubbin_battery import NubbinBattery
from car.car import Car
from car_parts.battery.spindler_battery import SpindlerBattery
from car_parts.engine.capulet_engine import CapuletEngine
from car_parts.engine.sternman_engine import SternmanEngine
from car_parts.engine.willoughby_engine import WilloughbyEngine
from car_parts.tires.carrigan_tire import CarriganTires
from car_parts.tires.octoprime_tire import OctoprimeTires


class CarFactory:

    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_sensor_values)
        return Car("CALLIOPE", engine, battery, tires)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_sensor_values)
        return Car("GLISSADE", engine, battery, tires)

    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_is_on: bool, tire_sensor_values):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tire_sensor_values)
        return Car("PALINDROME", engine, battery, tires)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tire_sensor_values)
        return Car("RORSCHACH", engine, battery, tires)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = CarriganTires(tire_sensor_values)
        return Car("NUBBIN", engine, battery, tires)

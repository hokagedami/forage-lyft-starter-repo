from datetime import date

from car_parts.battery.nubbin_battery import NubbinBattery
from car.car import Car
from car_parts.battery.spindler_battery import SpindlerBattery
from car_parts.engine.capulet_engine import CapuletEngine
from car_parts.engine.sternman_engine import SternmanEngine
from car_parts.engine.willoughby_engine import WilloughbyEngine


class CarFactory:

    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car("CALLIOPE", engine, battery)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car("GLISSADE", engine, battery)

    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_is_on: bool):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        return Car("PALINDROME", engine, battery)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car("RORSCHACH", engine, battery)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car("NUBBIN", engine, battery)

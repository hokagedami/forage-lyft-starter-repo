import unittest
from datetime import datetime

from car.car_factory import CarFactory

car_factory = CarFactory()


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.engine.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0.9, 0, 0.9]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.engine.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0.9, 0, 0.9]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_palindrome(last_service_date, warning_light_is_on, tire_sensor_values)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_palindrome(last_service_date, warning_light_is_on, tire_sensor_values)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_palindrome(last_service_date, warning_light_is_on, tire_sensor_values)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_palindrome(last_service_date, warning_light_is_on, tire_sensor_values)
        self.assertFalse(car.engine.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [1, 0.9, 0.6, 0.9]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.engine.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0.8, 0.9, 0.7, 0.6]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0, 0, 0, 0]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.engine.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [0.9, 0.9, 0, 0.9]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_values = [.2, 0, .8, 0]

        car = car_factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_sensor_values)
        self.assertFalse(car.tires.needs_service())


if __name__ == '__main__':
    unittest.main()

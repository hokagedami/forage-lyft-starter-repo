from _datetime import datetime
from dateutil.relativedelta import relativedelta

from car_parts.battery.battery import Battery
from abc import ABC


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date=datetime.today()):
        super().__init__("NUBBIN")
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return relativedelta(self.current_date, self.last_service_date).years >= 4

from _datetime import datetime
from dateutil.relativedelta import relativedelta

from car_parts.battery.battery import Battery
from abc import ABC


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date):
        super().__init__("NUBBIN")
        self.last_service_date = last_service_date

    def needs_service(self):
        return relativedelta(datetime.today(), self.last_service_date).years >= 4
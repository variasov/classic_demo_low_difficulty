from abc import ABC, abstractmethod
from datetime import date

from .dataclasses import DayOrdersInfo, PeriodOrdersInfo


class OrdersInfoRepoInterface(ABC):

    @abstractmethod
    def get_for_day(self, day: date) -> DayOrdersInfo: ...

    @abstractmethod
    def get_for_period(self, start_day: date,
                       end_day: date) -> PeriodOrdersInfo: ...

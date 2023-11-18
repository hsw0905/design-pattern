from abc import ABC, abstractmethod
from datetime import datetime


class TourPlanBuilder(ABC):
    @abstractmethod
    def title(self, title: str):
        ...

    @abstractmethod
    def nights_and_days(self, nights: int, days: int):
        ...

    @abstractmethod
    def start_date(self, start_date: datetime):
        ...

    @abstractmethod
    def where_to_stay(self, where_to_stay: str):
        ...

    @abstractmethod
    def add_plan(self, day: int, plan: str):
        ...

    @abstractmethod
    def build(self):
        ...

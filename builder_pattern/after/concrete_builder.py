from datetime import datetime

from builder_pattern.after.builder import TourPlanBuilder
from builder_pattern.before.detail_plan import DetailPlan
from builder_pattern.before.tour_plan import TourPlan


class TourBuilder(TourPlanBuilder):
    def __init__(self):
        self._tour_plan = TourPlan("", 0, 0, datetime(2023, 11, 18), "", [])

    def title(self, title):
        self._tour_plan.title = title
        return self

    def nights_and_days(self, nights: int, days: int):
        self._tour_plan.nights = nights
        self._tour_plan.days = days
        return self

    def start_date(self, start_date: datetime):
        self._tour_plan.start_date = start_date
        return self

    def where_to_stay(self, where_to_stay: str):
        self._tour_plan.where_to_stay = where_to_stay
        return self

    def add_plan(self, day: int, plan: str):
        self._tour_plan.plans.append(DetailPlan(day, plan))
        return self

    def build(self):
        return self._tour_plan

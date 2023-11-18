from datetime import datetime

from builder_pattern.before.detail_plan import DetailPlan


class TourPlan:
    def __init__(self,
                 title: str,
                 nights: int,
                 days: int,
                 start_date: datetime,
                 where_to_stay: str,
                 plans: list[DetailPlan]) -> None:
        self.title = title
        self.nights = nights,
        self.days = days
        self.start_date = start_date,
        self.where_to_stay = where_to_stay,
        self.plans = plans

from datetime import datetime

from builder_pattern.after.concrete_builder import TourBuilder
from builder_pattern.before.tour_plan import TourPlan

if __name__ == "__main__":
    tour_builder = TourBuilder()

    tour_plan: TourPlan = (
        tour_builder
        .title("칸쿤 여행")
        .nights_and_days(2, 3)
        .start_date(datetime(2023, 12, 24))
        .where_to_stay("호텔")
        .add_plan(0, "체크인 후 짐풀기")
        .add_plan(0, "저녁 식사")
        .add_plan(1, "호텔 조식")
        .add_plan(1, "해변가 산책")
        .add_plan(1, "수영장 근처 음식점 점심")
        .add_plan(1, "수영장에서 놀기")
        .add_plan(1, "스테이크 저녁")
        .add_plan(2, "호텔 조식")
        .add_plan(2, "체크 아웃")
        .build()
    )

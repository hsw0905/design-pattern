from datetime import datetime

from builder_pattern.before.detail_plan import DetailPlan
from builder_pattern.before.tour_plan import TourPlan

if __name__ == "__main__":
    # 불완전한 객체
    # short_trip = TourPlan(title="롱비치 여행", start_date=datetime(2023, 11, 18))

    tour_plan = TourPlan(
        title="칸쿤여행",
        nights=2,
        days=3,
        start_date=datetime(2023, 11, 18),
        where_to_stay="호텔",
        plans=[
            DetailPlan(0, "체크인 후 짐풀기"),
            DetailPlan(0, "저녁 식사"),
            DetailPlan(1, "호텔 조식"),
            DetailPlan(1, "해변가 산책"),
            DetailPlan(1, "수영장 근처 음식점 점심"),
            DetailPlan(1, "수영장에서 놀기"),
            DetailPlan(1, "스테이크 저녁"),
            DetailPlan(2, "호텔 조식"),
            DetailPlan(2, "체크 아웃"),
        ]
    )

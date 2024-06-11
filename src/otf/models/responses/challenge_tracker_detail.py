from datetime import datetime

from pydantic import BaseModel, Field


class MetricEntry(BaseModel):
    title: str = Field(..., alias="Title")
    equipment_id: int = Field(..., alias="EquipmentId")
    entry_type: str = Field(..., alias="EntryType")
    metric_key: str = Field(..., alias="MetricKey")
    min_value: str = Field(..., alias="MinValue")
    max_value: str = Field(..., alias="MaxValue")


class BenchmarkHistory(BaseModel):
    studio_name: str = Field(..., alias="StudioName")
    equipment_id: int = Field(..., alias="EquipmentId")
    result: float | str = Field(..., alias="Result")
    date_created: str = Field(..., alias="DateCreated")
    date_updated: str = Field(..., alias="DateUpdated")
    class_time: datetime = Field(..., alias="ClassTime")
    challenge_sub_category_id: None = Field(..., alias="ChallengeSubCategoryId")
    class_id: int = Field(..., alias="ClassId")
    substitute_id: int | None = Field(..., alias="SubstituteId")
    weight_lbs: int = Field(..., alias="WeightLBS")
    class_name: str = Field(..., alias="ClassName")
    coach_name: str = Field(..., alias="CoachName")
    coach_image_url: str = Field(..., alias="CoachImageUrl")
    workout_type_id: None = Field(..., alias="WorkoutTypeId")
    workout_id: None = Field(..., alias="WorkoutId")
    linked_challenges: list = Field(..., alias="LinkedChallenges")


class ChallengeHistory(BaseModel):
    challenge_objective: str = Field(..., alias="ChallengeObjective")
    challenge_id: int = Field(..., alias="ChallengeId")
    studio_id: int = Field(..., alias="StudioId")
    studio_name: str = Field(..., alias="StudioName")
    start_date: datetime = Field(..., alias="StartDate")
    end_date: datetime = Field(..., alias="EndDate")
    total_result: float | str = Field(..., alias="TotalResult")
    is_finished: bool = Field(..., alias="IsFinished")
    benchmark_histories: list[BenchmarkHistory] = Field(..., alias="BenchmarkHistories")


class ChallengeTrackerDetail(BaseModel):
    challenge_category_id: int = Field(..., alias="ChallengeCategoryId")
    challenge_sub_category_id: None = Field(..., alias="ChallengeSubCategoryId")
    equipment_id: int = Field(..., alias="EquipmentId")
    equipment_name: str = Field(..., alias="EquipmentName")
    metric_entry: MetricEntry = Field(..., alias="MetricEntry")
    challenge_name: str = Field(..., alias="ChallengeName")
    logo_url: str = Field(..., alias="LogoUrl")
    best_record: float | str = Field(..., alias="BestRecord")
    last_record: float | str = Field(..., alias="LastRecord")
    previous_record: float | str = Field(..., alias="PreviousRecord")
    unit: str | None = Field(..., alias="Unit")
    goals: None = Field(..., alias="Goals")
    challenge_histories: list[ChallengeHistory] = Field(..., alias="ChallengeHistories")


class ChallengeTrackerDetailList(BaseModel):
    details: list[ChallengeTrackerDetail]

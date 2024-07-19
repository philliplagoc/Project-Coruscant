"""
This module contains the DaySchedule Class. This represents a Day in the user's travel itinerary.
"""
from langchain_core.pydantic_v1 import BaseModel, Field

from .timeblock import TimeBlock


class DaySchedule(BaseModel):
    """
    Represents a day in the user's travel itinerary.
    """
    morning_block: TimeBlock = Field(description="The morning block of the day.")
    afternoon_block: TimeBlock = Field(description="The afternoon block of the day.")
    evening_block: TimeBlock = Field(description="The evening block of the day.")

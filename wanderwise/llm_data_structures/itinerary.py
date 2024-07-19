"""
This module contains the Itinerary Class. This represents the user's travel itinerary.
"""
from typing import Dict

from langchain_core.pydantic_v1 import BaseModel, Field

from .day_schedule import DaySchedule


class Itinerary(BaseModel):
    """
    Represents the user's entire travel itinerary.
    """
    itinerary: Dict[str, DaySchedule] = Field(description="Each day of the itinerary.")

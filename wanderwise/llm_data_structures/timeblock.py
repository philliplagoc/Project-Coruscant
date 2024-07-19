"""
This module contains the TimeBlock class.
"""

from langchain_core.pydantic_v1 import BaseModel, Field


class TimeBlock(BaseModel):
    """
    Represents a time block in the itinerary.
    """
    activity: str = Field(description="The name of the activity to do.")
    activity_description: str = Field(description="A brief description of the activity.")
    activity_location: str = Field(description="The location of the activity.")

    dining: str = Field(description="The name of a restaurant to dine in.")
    dining_description: str = Field(description="A brief description of the restaurant.")
    dining_location: str = Field(description="The location of the restaurant.")

    time_of_day: str = Field(description="The time of day to do the activity. Only choose between "
                                         "Morning, Afternoon, or Evening.")

"""A Prompt instance for generating the itinerary."""
from wanderwise.llm_prompts.base import Prompt

ITINERARY_PROMPT = Prompt(
    """
    I want to travel to {destination}.
    {activities}
    {trip_length}
    """
)

DEFAULT_DURATION = 3

HAS_PREFERRED_ACTIVITIES_STRING = Prompt("My preferred activities are: {activities}.")

NO_PREFERRED_ACTIVITIES_STRING = Prompt("I don't have any preferred activities.")

TRAVELING_DATES_STRING = Prompt("I will be traveling from {start_date} to {end_date}.")

TRAVELING_DURATION_STRING = Prompt("I will be traveling for {duration} days.")

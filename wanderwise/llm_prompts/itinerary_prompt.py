"""A Prompt instance for generating the itinerary."""
from wanderwise.llm_prompts.base import Prompt

ITINERARY_PROMPT = Prompt(
    """
    I want to travel to {destination}. I will be staying there for {duration} days.
    {activities}
    """
)

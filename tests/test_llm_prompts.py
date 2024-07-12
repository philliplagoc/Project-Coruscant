"""Tests the formatting of prompts in llm_prompts directory.
"""

from wanderwise.llm_prompts.itinerary_prompt import ITINERARY_PROMPT


def test_itinerary_prompt():
    """Tests the itinerary prompt."""
    assert ITINERARY_PROMPT

    prompt = ITINERARY_PROMPT.format(
        destination="Paris",
        activities="Hiking",
        trip_length="6"
    )

    assert "I want to travel to Paris." in prompt
    assert "Hiking" in prompt
    assert "6" in prompt

"""Generates a trip itinerary using an LLM and user input.
"""

import os

import markdown
from dotenv import load_dotenv
from flask import Blueprint, flash, render_template, request, session
from langchain_openai import ChatOpenAI

from wanderwise.llm_prompts.itinerary_prompt import ITINERARY_PROMPT
from wanderwise.llm_prompts.system_instructions import ITINERARY_SYSTEM_INSTRUCTIONS

# Load environment variables.
load_dotenv()

bp = Blueprint("generate_trip", __name__)
"""flask.Blueprint: Create generate_trip Blueprint."""

llm = ChatOpenAI(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    temperature=1,
    model_name="gpt-4o"
)
"""langchain_openai.ChatOpenAI: OpenAI LLM to generate trips with"""


def md_to_html(s: str) -> str:
    """Converts a Markdown string into HTML

    Args:
        s (str): The string written in markdown.

    Returns:
        str: The string written in HTML.
    """
    return markdown.markdown(s)


def generate_itinerary(prompt: str) -> str:
    """Generates an itinerary given a prompt.

    Args:
        prompt (str): Prompt for the trip. Includes the
            destination, duration, and preferred activities.

    Returns:
        str: The AI-planned itinerary.
    """
    print(prompt)
    messages = [
        (
            "system",
            ITINERARY_SYSTEM_INSTRUCTIONS
        ),
        (
            "human",
            prompt
        )
    ]
    llm_response = llm.invoke(messages).content

    return llm_response


@bp.route("/", methods=("GET", "POST"))
def index():
    """Show a text area where the user inputs a
       destination and AI generates a trip itinerary.

    Returns:
        str: A rendered template of the index.html page.
    """
    # Get the Advanced Settings from the user.
    activities = session.get('saved_activities', "I don't have any preferred activities.")  # TODO Fix magic string.

    # Determine if user knows when their trip will take place.
    if session.get('saved_toggle', False):
        start_date = session.get('saved_start_date', '')
        end_date = session.get('saved_end_date', '')
        trip_length = f"I will be traveling from {start_date} to {end_date}."  # TODO Fix this magic string.
    else:  # User didn't know dates, so chose a duration.
        duration = session.get('saved_duration', 6)  # TODO Fix this magic number.
        trip_length = f"I will be traveling for {duration} days."  # TODO Fix this magic string.

    destination = ""
    base_itinerary = ""

    # User entered a destination.
    if request.method == "POST":
        destination = request.form["destination"].strip()

        # Ensure that the user didn't send in an empty string.
        if not destination:
            flash("Destination is required.")
        else:
            # If the user knows when their trip will take place, format that into the prompt.
            prompt = ITINERARY_PROMPT.format(destination=destination,
                                             activities=activities,
                                             trip_length=trip_length)
            base_itinerary = generate_itinerary(prompt)
            # Convert from Markdown to HTML
            base_itinerary = md_to_html(base_itinerary)

    return render_template(
        "generate_trip/index.html",
        destination=destination,
        base_itinerary=base_itinerary,
        activities=activities,
        trip_length=trip_length
    )

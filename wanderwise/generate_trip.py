"""Generates a trip itinerary using an LLM and user input.
"""

import os
import markdown
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash


# Load environment variables.
load_dotenv()

bp = Blueprint("generate_trip", __name__)
"""flask.Blueprint: Create generate_trip Blueprint."""

llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"], temperature=1, model_name="gpt-4o"
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


def generate_itinerary(destination: str):
    """Generates an itinerary given a destination.

    Args:
        destination (str): Where to generate the itinerary.

    Returns:
        str: The AI-planned itinerary.
    """
    prompt = f"""
    You are a highly skilled trip planner with extensive experience in organizing memorable weekend getaways across the globe.

    **Destination:** `{destination}`

    **Objective:** Craft a comprehensive itinerary for an unforgettable weekend in `{destination}`.

    ### Itinerary Overview

    **Day 1: Arrival and Exploration**
    - **Morning:** 
    - Arrival at `{destination}`, check-in at [Accommodation Name].
    - Breakfast at [Restaurant Name], known for its [Specialty Dish].
    - **Afternoon:** 
    - Visit [Place of Interest #1], a must-see attraction because of its [Unique Feature].
    - Lunch at [Restaurant Name], offering exquisite [Type of Cuisine] cuisine.
    - **Evening:** 
    - Explore [Local Market/Area], perfect for experiencing `{destination}`'s vibrant culture.
    - Dinner at [Restaurant Name], a top pick for [Type of Cuisine] dishes.

    **Day 2: Adventure and Leisure**
    - **Morning:** 
    - Start the day with an adventure activity at [Location], such as [Activity].
    - Brunch at [Café Name], famous for its [Signature Dish].
    - **Afternoon:** 
    - Relaxing visit to [Park/Beach], including optional activities like [Activity #1, Activity #2].
    - Snack at [Local Eatery], try the [Local Specialty].
    - **Evening:** 
    - Dinner at [Restaurant Name], renowned for its [Dish] and ambiance.
    - Optional evening entertainment at [Venue], featuring [Type of Entertainment].

    **Day 3: Culture and Departure**
    - **Morning:** 
    - Visit [Cultural Site], an iconic spot that offers insights into `{destination}`'s history.
    - Breakfast at [Restaurant Name], where you can enjoy a leisurely meal before departure.
    - **Afternoon:** 
    - Last-minute shopping at [Shopping Area], perfect for souvenirs and local goods.
    - Lunch at [Restaurant Name], a final taste of `{destination}` before heading home.

    **Accommodations:**
    - **Stay at:** [Hotel/Hostel Name], located in [Area], known for its [Feature, e.g., great views, central location, cozy atmosphere].

    **Notes:**
    - Adjust the schedule based on personal preferences and travel pace.
    - Ensure to check the opening hours and any need for reservations in advance.
    - Consider local transportation options for getting around efficiently.

    This itinerary is designed to offer a blend of adventure, relaxation, and cultural exploration, ensuring a well-rounded and enriching weekend experience in `{destination}`.
    """
    llm_response = llm.invoke(prompt).content

    return llm_response


@bp.route("/", methods=("GET", "POST"))
def index():
    """Show a text area where the user inputs a
       destination and AI generates a trip itinerary.

    Returns:
        str: A rendered template of the index.html page.
    """
    destination = ""
    base_itinerary = ""
    # User entered a destination
    if request.method == "POST":
        destination = request.form["destination"].strip()

        # Ensure that the user didn't send in an empty string.
        if not destination:
            flash("Destination is required.")
        else:
            base_itinerary = generate_itinerary(destination)
            # Convert from Markdown to HTML
            base_itinerary = md_to_html(base_itinerary)

    return render_template(
        "generate_trip/index.html",
        destination=destination,
        base_itinerary=base_itinerary,
    )

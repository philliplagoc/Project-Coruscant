"""Generates a trip itinerary using an LLM and user input.
"""

import markdown
from flask import Blueprint, flash, render_template, request, session

from wanderwise.generate_itinerary import generate_itinerary
from wanderwise.llm_prompts.itinerary_prompt import NO_PREFERRED_ACTIVITIES_STRING, HAS_PREFERRED_ACTIVITIES_STRING, \
    TRAVELING_DATES_STRING, TRAVELING_DURATION_STRING, DEFAULT_DURATION

bp = Blueprint("calendar", __name__)
"""flask.Blueprint: Create calendar Blueprint."""


def md_to_html(s: str) -> str:
    """Converts a Markdown string into HTML

    Args:
        s (str): The string written in markdown.

    Returns:
        str: The string written in HTML.
    """
    return markdown.markdown(s)


@bp.route("/", methods=("GET", "POST"))
def index():
    """Show a text area where the user inputs a
       destination and AI generates a trip itinerary.

    Returns:
        str: A rendered template of the index.html page.
    """
    # Get the Advanced Settings from the user.
    activities = session.get('saved_activities',
                             "").strip()
    if activities == "":  # User didn't enter any activities.
        activities = NO_PREFERRED_ACTIVITIES_STRING
    else:
        activities = HAS_PREFERRED_ACTIVITIES_STRING.format(activities=activities)

    # Determine if user knows when their trip will take place.
    if session.get('saved_toggle', False):
        start_date = session.get('saved_start_date', '')
        end_date = session.get('saved_end_date', '')
        trip_length = TRAVELING_DATES_STRING.format(start_date=start_date, end_date=end_date)
    else:  # User didn't know dates, so chose a duration.
        duration = session.get('saved_duration', DEFAULT_DURATION)
        trip_length = TRAVELING_DURATION_STRING.format(duration=duration)

    destination = ""
    user_itinerary = ""

    # User entered a destination.
    if request.method == "POST":
        destination = request.form["destination"].strip()

        # Ensure that the user didn't send in an empty string.
        if not destination:
            flash("Destination is required.")
        else:
            user_itinerary = generate_itinerary(destination=destination,
                                                activities=activities,
                                                trip_length=trip_length)
            # Convert from Markdown to HTML
            # user_itinerary = md_to_html(user_itinerary)

    return render_template(
        "calendar/index.html",
        destination=destination,
        user_itinerary=user_itinerary,
        activities=activities,
        trip_length=trip_length
    )

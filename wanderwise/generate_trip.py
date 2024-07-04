"""Generates a trip itinerary using an LLM and user input.
"""

from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

# Create a Blueprint to collect all routes involved with generating
# a trip itinerary using LLM.
bp = Blueprint("generate_trip", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    """Show a text area where the user inputs a
       destination and AI generates a trip itinerary.

    Returns:
        str: A rendered template of the index.html page.
    """
    destination = ""
    # User entered a destination
    if request.method == "POST":
        destination = request.form["destination"].strip()

        # Ensure that the user didn't send in an empty string.
        if not destination:
            flash("Destination is required.")

    return render_template("generate_trip/index.html", destination=destination)

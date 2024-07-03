"""Generates a trip itinerary using an LLM and user input.
"""

from flask import Blueprint
from flask import render_template
from flask import request

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
    # User entered a destination
    if request.method == "POST":
        return f"You want to visit: {request.form["destination"]}"
    
    return render_template("generate_trip/index.html")
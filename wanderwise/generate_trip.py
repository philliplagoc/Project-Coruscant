"""Generates a trip itinerary using an LLM and user input.

TODO:
    - Complete TripStructure Class definition.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

# Load environment variables.
load_dotenv()

bp = Blueprint("generate_trip", __name__)
"""flask.Blueprint: Create generate_trip Blueprint."""

llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    temperature=1,
    model_name="gpt-4o",
)
"""langchain_openai.ChatOpenAI: OpenAI LLM to generate trips with"""


class TripStructure(BaseModel):
    """Defines JSON structure for LLM output.

    Args:
        BaseModel (_type_): _description_

    Attributes:
        attr1 (Field): Description of `attr1`.
        attr2 (Field, optional): Description of `attr2`.

    """

    destination: str = Field(description="The trip's destination")
    duration: int = Field(
        description="The length of the trip in number of days"
    )
    trip_price: float = Field(
        description="The total estimated price (in USD) for the trip"
    )
    attractions: list = Field(
        description="A list of the attractions to visit during the trip"
    )
    transports: list = Field(
        description="A list of the modes of transporation to take throughout the trip"
    )


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

"""Shows the Advanced Settings a user can configure.
"""

from flask import Blueprint, render_template

bp = Blueprint("advanced_settings", __name__)
"""flask.Blueprint: Create advanced_settings Blueprint."""


@bp.route("/advanced_settings", methods=("GET", "POST"))
def show_advanced_settings():
    """Show the Advanced Settings a user can configure.

    These settings alter the AI-generated itinerary.

    Returns:
        str: A rendered template of the advanced_settings.html page.
    """
    return render_template(
        "advanced_settings/advanced_settings.html"
    )

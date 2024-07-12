"""Shows the Advanced Settings a user can configure.
"""

from flask import Blueprint, render_template, request, redirect, url_for, session

bp = Blueprint("advanced_settings", __name__)
"""flask.Blueprint: Create advanced_settings Blueprint."""


@bp.route("/advanced_settings", methods=("GET", "POST"))
def show_advanced_settings():
    """Show the Advanced Settings a user can configure.

    These settings alter the AI-generated itinerary.

    Returns:
        str: A rendered template of the advanced_settings.html page.
    """
    # Handle settings made by the user.
    if request.method == 'POST':
        # TODO Validate all input from user.
        # TODO Add calendar input.
        # Save the activities inputted by user.
        session["saved_activities"] = request.form["activities"]

        # Determine if user knows when their trip will take place.
        if "toggle" in request.form:
            session["saved_toggle"] = True
            session["saved_start_date"] = request.form["start_date"]
            session["saved_end_date"] = request.form["end_date"]
        elif "toggle" not in request.form:  # toggle is removed from form when off.
            session["saved_toggle"] = False
            session["saved_duration"] = request.form["duration"]

        return redirect(url_for('generate_trip.index'))

    activities = session.get('saved_activities', '')
    duration = session.get('saved_duration', 6)  # TODO Fix this magic number.
    start_date = session.get('saved_start_date', '')
    end_date = session.get('saved_end_date', '')
    toggle = session.get('saved_toggle', False)
    return render_template('advanced_settings/advanced_settings.html',
                           activities=activities,
                           duration=duration,
                           start_date=start_date,
                           end_date=end_date,
                           toggle=toggle)

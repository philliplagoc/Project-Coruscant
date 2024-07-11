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
    if request.method == 'POST':
        session["saved_activities"] = request.form["activities"]
        session['saved_duration'] = request.form['duration']
        return redirect(url_for('generate_trip.index'))
    activities = session.get('saved_activities', '')
    duration = session.get('saved_duration', 6)
    return render_template('advanced_settings/advanced_settings.html',
                           activities=activities,
                           duration=duration)

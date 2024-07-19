"""Module initializing the WanderWise Flask App."""

from flask import Flask


def create_app(test_config=None):
    """Creates and configures an instance of the Flask application.

    Args:
        test_config (flask.Config, optional): The test configuration. Defaults to None.

    Returns:
        flask.Flask: A configured Flask instance.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # A default secret that should be overridden by instance config.
        SECRET_KEY="dev"
    )

    if test_config is None:
        # Load the instance config if it exists, when not testing.
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in.
        app.config.update(test_config)

    # Apply Blueprints to the app.
    from wanderwise import calendar
    from wanderwise import advanced_settings

    app.register_blueprint(calendar.bp)
    app.register_blueprint(advanced_settings.bp)

    # make url_for('index') == url_for('blog.index')
    # since the generate_trip page is the main index.
    app.add_url_rule("/", endpoint="index")

    return app

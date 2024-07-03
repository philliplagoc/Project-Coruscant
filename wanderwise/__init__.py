"""Module initializing the WanderWise Flask App."""

import os

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

    @app.route("/hello")
    def hello():
        """A simple function to print Hello World on the page.

        Returns:
            str: "Hello, World!" string for the page
        """
        return "Hello, World!"

    return app

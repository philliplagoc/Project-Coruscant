"""Tests for setting up a test app and test client."""

import pytest
from dotenv import load_dotenv
from wanderwise import create_app

# Load environment variables.
load_dotenv()


@pytest.fixture
def app():
    """Create and configure a new app instance
        for each test.

    Yields:
        flask.Flask: A configured app for testing.
    """
    # Create an app with common testing config.
    app = create_app({"TESTING": True})

    yield app


@pytest.fixture
def client(app):
    """Creates a test client for the app.

    Args:
        app (flask.Flask): A configured Flask app.

    Returns:
        flask.testing.FlaskClient: A test client.
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """Creates a runner for the app.

    Args:
        app (flask.Flask): A configured Flask app.

    Returns:
        flask.testing.FlaskCliRunner: A CLI runner for testing CLI commands.
    """
    return app.test_cli_runner()

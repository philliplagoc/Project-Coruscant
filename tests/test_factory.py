"""Tests for the WanderWise Flask App.

Tests for whether or not the Flask App is configured correctly.

"""

from wanderwise import create_app


def test_config():
    """Test create_app() without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    """Tests the hello() function.

    Checks if the data of the page has the phrase
    "Hello, World!"

    Args:
        client (flask.testing.FlaskClient): A test client that
            makes requests.
    """
    response = client.get("/hello")
    assert response.data == b"Hello, World!"

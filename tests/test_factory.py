"""Tests for the WanderWise Flask App.

Tests for whether or not the Flask App is configured correctly.

"""

from wanderwise import create_app


def test_config():
    """Test create_app() without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing

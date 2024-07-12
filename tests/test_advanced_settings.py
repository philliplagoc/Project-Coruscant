"""Tests advanced_settings.py.
"""

import pytest

from wanderwise.advanced_settings import validate_duration


@pytest.fixture
def knows_date():
    """Returns a dictionary of user input for advanced_settings.

    This is from a user who knows the dates for their trip. Note that in this case, a toggle is needed, since
    the user knows the dates for their trip.

    Returns:
        dict: A dictionary of user input for advanced_settings.
    """
    return {
        "activities": "Snorkeling, Temples",
        "duration": "6",
        "start_date": "2022-01-01",
        "end_date": "2022-01-02",
        "toggle": "on"
    }


@pytest.fixture
def knows_duration():
    """Returns a dictionary of user input for advanced_settings.

    This is from a user who knows the duration of their trip. Note that in this case, no toggle is needed.

    Returns:
        dict: A dictionary of user input for advanced_settings.
    """
    return {
        "activities": "Hiking, Swimming",
        "duration": "11",
        "start_date": "",
        "end_date": "",
    }


def test_show_advanced_settings_get(client):
    """Test GET request for Advanced Settings page.

    Args:
        client (flask.testing.FlaskClient): A test client that makes
            requests.
    """
    response = client.get("/advanced_settings")
    assert response.status_code == 200
    html_content = response.data.decode("utf-8")

    assert "<h1>Advanced Settings</h1>" in html_content


def test_show_advanced_settings_knows_date(client, knows_date):
    """Tests the POST request for Advanced Settings page.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """

    # Test with a user who knows the dates for their trip.
    response = client.post("/advanced_settings",
                           data=knows_date,
                           follow_redirects=True)

    assert response.status_code == 200

    # Check if session variables set correctly.
    with client.session_transaction() as sess:
        assert sess['saved_activities'] == "Snorkeling, Temples"
        assert "saved_duration" not in sess
        assert sess["saved_start_date"] == "2022-01-01"
        assert sess["saved_end_date"] == "2022-01-02"
        assert sess["saved_toggle"]


def test_show_advanced_settings_knows_duration(client, knows_duration):
    """Tests the POST request for Advanced Settings page.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """

    # Test with a user who knows the dates for their trip.
    response = client.post("/advanced_settings",
                           data=knows_duration,
                           follow_redirects=True)

    assert response.status_code == 200

    # Check if session variables set correctly.
    with client.session_transaction() as sess:
        assert sess['saved_activities'] == "Hiking, Swimming"
        assert sess["saved_duration"] == "11"
        assert "saved_start_date" not in sess
        assert "saved_end_date" not in sess
        assert not sess["saved_toggle"]


def test_show_advanced_settings_with_session_data(client):
    """Tests the POST request for Advanced Settings page
        with pre-existing session data.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """
    with client.session_transaction() as sess:
        sess['saved_activities'] = "Surfing, Jet-skis"
        sess['saved_duration'] = "11"

    response = client.get("/advanced_settings")
    assert response.status_code == 200
    assert b'Surfing, Jet-skis' in response.data
    assert b'11' in response.data


def test_validate_duration():
    """Tests the validate_duration function.
    """
    assert validate_duration("10")
    assert not validate_duration("a")

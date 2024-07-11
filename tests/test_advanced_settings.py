"""Tests advanced_settings.py.
"""


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


def test_show_advanced_settings_post(client):
    """Tests the POST request for Advanced Settings page.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """
    test_activities = "Snorkeling, Temples"
    test_duration = "10"
    response = client.post("/advanced_settings",
                           data={
                               "activities": test_activities,
                               "duration": test_duration
                           }, follow_redirects=True)

    assert response.status_code == 200

    # Check if session variables set correctly.
    with client.session_transaction() as sess:
        assert sess['saved_activities'] == test_activities
        assert sess['saved_duration'] == test_duration

    # TODO Check if bad input shows flash error message correctly.


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

"""Tests generate_trip.py.
"""

from unittest.mock import Mock

import pytest

from wanderwise.generate_trip import generate_itinerary
from wanderwise.generate_trip import md_to_html


@pytest.fixture
def md_string():
    """Returns a simple Markdown string.

    Returns:
        str: A simple markdown string to test md_to_html().
    """
    return "# This is a header.\n\nThis is a paragraph."


def test_generate_itinerary(monkeypatch):
    """Tests generate_itinerary().

    In other words, test the post request for index page.

    Args:
        monkeypatch (pytest.MonkeyPatch): Pytest fixture that changes the llm variable
                                          during testing.
    """
    # Create a mock LLM.
    mock_llm = Mock()
    mock_llm.invoke.return_value.content = "Fake itinerary."

    # Patch the LLM in the generate_itinerary function.
    monkeypatch.setattr("wanderwise.generate_trip.llm", mock_llm)

    # Test with a valid destination
    result = generate_itinerary("Paris")

    # Check if the LLM was called with the correct prompt
    mock_llm.invoke.assert_called_once()
    prompt_arg = mock_llm.invoke.call_args[0][0]
    assert "Paris" in prompt_arg[1][1]  # Points to the "human" message in what's sent to LLM.

    expected = "Fake itinerary."
    assert result == expected

    # TODO Test that prompt is formatted correctly when different arguments are provided.


def test_md_to_html(md_string):
    """Tests the md_to_html() method.

    Args:
        md_string (str): The fixture for md_string.
    """
    expected = "<h1>This is a header.</h1>\n<p>This is a paragraph.</p>"
    result = md_to_html(md_string)
    assert expected == result


def test_index_get(client):
    """Tests the index page with a GET request.

    Args:
        client (flask.testing.FlaskClient): A test client that
            makes requests.
    """
    response = client.get("/")
    assert response.status_code == 200
    html_content = response.data.decode("utf-8")

    # Check if title is correct.
    assert "<h1>Plan a Trip</h1>" in html_content

    # Check if the form exists with correct method.
    assert '<form method="post">' in html_content

    # Check if the input field exists with correct attributes.
    assert (
        '<input name="destination" id="destination" value="" required>' in html_content
    )

    # Check if submit button exists with correct value.
    assert '<input type="submit" value="Generate a Trip">' in html_content


def test_index_post_empty(client):
    """Tests if user submits an empty string as destination.

    Should flash an error message that the destination is required and
    redirect back to the form.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """
    response = client.post("/", data={"destination": ""})
    assert response.status_code == 200

    html = response.data.decode("utf-8")
    assert "Destination is required." in html
    assert '<form method="post">' in html


def test_index_post_whitespace(client):
    """Tests if user submits whitespace as destination.

    Should flash an error message that the destination is required and
    redirect back to the form.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """
    response = client.post("/", data={"destination": "   "})
    assert response.status_code == 200

    html = response.data.decode("utf-8")
    assert "Destination is required." in html
    assert '<form method="post">' in html

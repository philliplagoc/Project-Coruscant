"""Tests generate_trip.py.
"""


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
        '<input name="destination" id="destination" value="" required>'
        in html_content
    )

    # Check if submit button exists with correct value.
    assert '<input type="submit" value="Generate a Trip">' in html_content


def test_index_post(client):
    """Tests the index page with a POST request.

    A statement should be printed containing the inputted destination.

    Args:
        client (flask.testing.FlaskClient): A test client that
            makes requests.
    """
    response = client.post("/", data={"destination": "Paris"})
    assert response.status_code == 200

    # Check if the response contains the expected text
    assert "You want to visit: Paris" in response.data.decode("utf-8")


def test_index_post_empty(client):
    """Tests if user submits an empty string as destination.

    Should flash an error message that the destination is required and
    redirect back to the form.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """    
    response = client.post('/', data={'destination': ''})
    assert response.status_code == 200
    
    html = response.data.decode('utf-8')
    assert 'Destination is required.' in html
    assert '<form method="post">' in html

def test_index_post_whitespace(client):
    """Tests if user submits whitespace as destination.

    Should flash an error message that the destination is required and
    redirect back to the form.

    Args:
        client (flask.testing.FlaskClient): A test client that makes requests.
    """    
    response = client.post('/', data={'destination': '   '})
    assert response.status_code == 200
    
    html = response.data.decode('utf-8')
    assert 'Destination is required.' in html
    assert '<form method="post">' in html

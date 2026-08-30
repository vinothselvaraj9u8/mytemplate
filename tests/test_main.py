def test_homepage_loads(client):
    """The homepage should load successfully for an anonymous visitor."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'MyTemplate' in response.data


def test_terms_page_loads(client):
    """The terms page should load successfully."""
    response = client.get('/terms')
    assert response.status_code == 200

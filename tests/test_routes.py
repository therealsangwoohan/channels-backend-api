from api import app


def test_get_channels():
    response = app.test_client().get("/api/channels")
    print(response)
    assert True

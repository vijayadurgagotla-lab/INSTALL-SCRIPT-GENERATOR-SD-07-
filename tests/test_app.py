def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_script_generation(client):
    response = client.post(
        "/generate",
        json={
            "prompt":"Install Python"
        }
    )

    assert response.status_code == 200
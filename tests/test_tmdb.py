import tmdb_client
from unittest.mock import Mock

def test_get_single_movie(monkeypatch):
    mock_single_movie = ['Movie 1']
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)

    single_movie = tmdb_client.get_single_movie(movie_id=343611)
    assert single_movie ==mock_single_movie


def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = ["Movie 1"]
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)

    single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=343611)
    assert single_movie_cast ==mock_single_movie_cast




def test_get_movie_images(monkeypatch):
    mock_movie_images = ["Movie 1"]
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)

    movie_images = tmdb_client.get_movie_images(movie_id=343611)
    assert movie_images ==mock_movie_images


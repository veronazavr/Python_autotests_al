import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'


def test_name():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': 3570}, headers=HEADER, timeout=5)
    assert response != response.json()['trainer_name'] == 'QATrainer', ''
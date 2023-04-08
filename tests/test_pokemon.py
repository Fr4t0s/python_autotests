import requests
import pytest
Url = "https://pokemonbattle.me:9104/"

# проверка статус-кода запроса информации о тренере
def test_status_code():
    response = requests.get (f"{Url}trainers", params = {"trainer_id": 3768}
)
    assert response.status_code == 200
    
# проверка имени и города тренера
@pytest.mark.parametrize('key, value', [('trainer_name', 'ЫЫЫЫ'), ('city', 'ЫЫ')])
def test_pats_of_body(key,value):
    response = requests.get (f"{Url}trainers", params = {"trainer_id": 3768}
)
    assert response.json()[key] == value

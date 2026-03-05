import allure
import pytest
import requests

from tests.api_tests.test_get_nasa_subj import response

url = "https://osdr.nasa.gov/geode-py/ws/api/vehicles"
# response = requests.get(url)

#a = 2

# @allure.id("1")
# @allure.feature("NASA_API")
# @allure.label("Api_tests")
# @allure.title("Получение эксперимента от nasa_api")
# @allure.description("Тест проверяет, что в ручке экспериментов приходят эксперименты")
# @pytest.mark.nasa_tests
# @allure.testcase("some_test_case_url")
# @pytest.mark.skip(reason="Метод получения экспериментов не работает")
# @pytest.mark.skipif(a=2, reason="Метод получения экспериментов не работает, если а=2")
# @pytest.mark.parametrize("language", ['eng','uz','kz')

# def text_experiment():
#     response = requests.get(url)
#     my_json = response.json()
#     vehicles = my_json.get('data')
#     val = 'https://osdr.nasa.gov/geode-py/ws/api/vehicles/154'
#     for subj in vehicles:
#         if subj.get("vehicles") == val:
#             break
#     print(response.status_code)
# assert response.status_code == 200


def test_text_experiment():
    response = requests.get(url)
    my_json = response.json()
    vehicles = my_json.get('data')
    val = ('https://osdr.nasa.gov/geode-py/ws/api/vehicle/Apollo')
    response = requests.get(val).json()
    for subj in vehicles:
        if subj.get("vehicles") == val:
            break
    print(response.status_code)
    assert response.status_code == 200
# with allure.step

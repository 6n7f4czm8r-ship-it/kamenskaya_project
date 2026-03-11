import requests

# url = ("https://petstore.swagger.io/v2/pet/1")
url = ("https://osdr.nasa.gov/geode-py/ws/api/subjects")
response = requests.get(url)

def test_1():
    response = requests.get(url)
    my_json = response.json()
    subjects = my_json.get('data')
    val = 'https://osdr.nasa.gov/geode-py/ws/api/subject/197'
    for subj in subjects:
        if subj.get("subject") == val:
            break
    print(response.status_code)
assert response.status_code ==200


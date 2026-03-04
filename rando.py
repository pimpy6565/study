import requests

url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)
data = response.json()

for question in data["results"]:
    print(question["question"])
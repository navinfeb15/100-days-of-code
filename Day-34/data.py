
import requests

parameters = {
    "amount" : 10,
    "type" : "boolean",
    "category" : None,
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
question = response.json()["results"]
question_data = [{"text":item['question'],"answer":item["correct_answer"]} for item in question]

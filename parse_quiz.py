
import json
from pprint import pprint

with open('quiz1.json', 'r') as file:
    data = file.read()
    json_data = json.loads(data)
    quiz_config = json_data['attrs']['quizConfig']
    quiz_config = json.loads(quiz_config)
    pprint(quiz_config, indent=2)
import json
import sys

def parse(DATA_NAME):
    data = open(DATA_NAME)
    print(data)
    json_data = json.load(data)
    data.close()
    return json_data
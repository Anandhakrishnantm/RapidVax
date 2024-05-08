import os, json

current_path = os.path.abspath(__file__)
file_path = os.path.dirname(current_path)
json_path = os.path.join(file_path, 'stock.json')

with open(json_path, 'r') as wfile:
    datas = wfile.read()
    parsed_data = json.loads(datas)
    print(type(parsed_data))
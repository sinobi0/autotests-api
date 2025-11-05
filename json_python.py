import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address" :  {
    "city": "Москва",
    "zip": 101000
  }
}
"""
parsed_data = json.loads(json_data)
print(parsed_data['name'])

data = {
    'name': 'Мария',
    'age': 30,
    'is_student': True
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)


with open('json_example.json', 'r', encoding='utf-8') as f:
    read_data = json.load(f)
    print(data['address']['city'])

with open('json_user.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
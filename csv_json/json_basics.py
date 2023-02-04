from json import loads, dumps

def json_string_to_python_val(string_of_json):
    json_data_as_python_value = loads(string_of_json)
    print(json_data_as_python_value)

def python_val_to_json(python_val):
    return dumps(python_val)

# print(
    # type(python_val_to_json(
        # {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
    # 'felineIQ': None}
    # ))
# )

# json_string_to_python_val(
    # '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
# )
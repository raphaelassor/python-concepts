import json

data = {
    "website": {
        "email": "raphassor@gmail.com",
        "password": 123456,
    }
}
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        print(data)
except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
else:
    new_data = {
        "cookies": {
            "chocolate": 50,
            "vanilla": 25
        }
    }
    data.update(new_data)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

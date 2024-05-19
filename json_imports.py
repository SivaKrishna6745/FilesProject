import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)  # read files and turns it to a dictionary
file.close()

print(file_contents['friends'][0])  # {'name': 'Jose', 'degree': 'Applied Computing'}

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

cars_json = open('cars_json.txt', 'w')
json.dump(cars, cars_json, indent=4)  # write the data as a json into the file, indent for indentation
cars_json.close()

my_json_string = '[{"name": "Alfa Romeo"}, {"released": "1950"}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])  # Alfa Romeo
import json

# file = open('friends_json.txt', 'r')
# file_contents = json.load(file)  # read files and turns it to a dictionary
# file.close()

# the above lines (3-5) can be written as below:
with open('friends_json.txt', 'r') as file:  # context manager - automatically closes the file
    file_contents = json.load(file)

print(file_contents['friends'][0])  # {'name': 'Jose', 'degree': 'Applied Computing'}

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

# cars_json = open('cars_json.txt', 'w')
# json.dump(cars, cars_json, indent=4)  # write the data as a json into the file, indent for indentation
# cars_json.close()

# the above lines (18-20) can be written as below:
with open('cars_json.txt', 'w') as file:
    json.dump(cars, file, indent=4)

my_json_string = '[{"name": "Alfa Romeo"}, {"released": "1950"}]'
incorrect_car = json.loads(my_json_string)  # load the string as declared in line 18 and convert into python dictionary (json)
print(incorrect_car[0]['name'])  # Alfa Romeo

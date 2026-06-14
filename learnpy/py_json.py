import json

userJSON ='{"first name":"John", "last name":"Doe", "age":30, "city":"New York"}'
#parse to a dictionary
user = json.loads(userJSON)

print(user)
print(userJSON['first_name'])

car = {'make':'Ford', 'model':'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
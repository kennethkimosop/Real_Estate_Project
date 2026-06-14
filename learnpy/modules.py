#core modules
import datetime
import time
from datetime import date
from time import time


#pip modules
import camelcase

#Custom modules
import validator


# today = datetime.date.today()
today = date.today()
timestamp = time()
print(today,timestamp)

camel = camelcase.CamelCase()
text = 'hellloo there worls' 
print(camel.hump(text))

email = 'test@gmail.com'
if validator.validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')
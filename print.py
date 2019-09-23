name = input('Please enter your name:')
print('Blank line \n in the middle of string')
print('hello world')
print('Adding numbers')
x = 42 + 206 
print('Peforming Division')
#y = x / 0 
print("Math's Complete")
# These are comments in Python 
# Strings 
first_name = 'Christopher'
last_name = 'Harrison'
print('hello'+first_name + last_name)

sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# String Format 
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1}'.format(first_name, last_name)
#output = f'Hello, {first_name} {last_name}'

# Numbers
first_num = 6 
second_num = 2 
print(first_num + second_num)
print(first_num ** second_num)

print(str(first_num)+'days in February')

# input function always returns string 
first_num = '5'
second_num = '6'
print(int(first_num)+int(second_num))
print(float(first_num)+float(second_num))

# Date Library 
from datetime import datetime, timedelta
today = datetime.now()

print('Today is '+str(today))
one_day = timedelta(days=1)
yesterday = today - one_day 
print('Yesterday was: '+ str(yesterday))

print('Day: '+ str(today.day))
print('Month: '+ str(today.month))
print('Year: '+ str(today.year))

birthday = input('Birthday (dd/mm/yyyy)')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: '+ str(birthday_date))

#Exception handling. 
# Error Types
# Syntax Error 
# Runtime Error 
# 
x = 100 
y = 0  

try:
    print(x / y)
except ZeroDivisionError as e: 
    # Optionally log e somewhere 
    print('Sorry, something went wrong')
except: #you can also have else in here 
    print('Something really went wrong')
finally: 
    print('This always runs on success or failure')


#Handling Condition 
price = 10.00 
if price >= 1.00: 
    tax = .07  #4 spaces 
else: 
    tax = 0 
print(tax)

# String Comparison are case sensitive. 
country = 'Nepal'
province = 'Ontario'
if country == 'Canada':
    if province.lower() in ('Alberta', \
        'Yukon', 'Nunavut'):
        tax = 0.05 
    elif province == 'Ontario':
        tax = 0.13 
    else: 
        tax = 0.15 
else: 
    tax = 0.0

# AND Condition 
if gpa >= .85: 
    if lowest_grade >= .70:
        honor_roll = True 
        print('Well done')
if gpa >= .85 and lowest_grade >= .70:     
    print('Well Done')


# Collection
names = ['Christopher', 'b1k']
scores = [] 
scores.append(98) #Add new item to the end 
scores.append(99)
print(scores)
print(scores[1]) #Collections are zero-indexed 

from array import array 
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

"""
Arrays VS Lists
Arrays can only store specific items. 
Lists can store any datatypes
"""

names = ['Susan', 'Christopher']
print(len(names)) #Get the number of items 
names.insert(0,'Bill') #Insert before index 
print(names)
names.sort()
print(names)
presenters = name[0:2]
print(presenters)
print(len(presenters))



#Dictionaries 
person = {'first': 'christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

""""
Dictionary gives key value pair 
Garunteed the order of items. 


"""

# Loops ; while, for 

for name in ['Christopher','Susan']:
    print name 

for index in range(0,2):
    print(index)

names = ['Christopher','Susan']
index = 0 
while index < len(names):
    print(names[index])
    # Change the condition ! 
    index = index + 1 


# Function 
import datetime 

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()

def print_time():
    print('task completed')
    print(datetime.datetime.now())

# parameter 

first_name = 'Susan'

def print_time(task_name):
    print(task_name)
    print(datetime.datetime.now())

first_name = input('Enter name')
first_name_initial = first_name[0:1]
print(first_name_initial)

def get_initial(name):
    initial = name[0:1].upper()
    return initial

# if you do not pass parameter it will use default 
def get_initial(name,force_uppercase=True):
    if force_uppercase: 
        initial = name[0:1].upper()
    else: 
        initial = name[0:1]
    return initial 

#named parameter 

get_initial(force_uppercase=True, name='b1k')


# Modules and packages 

#helper.py 

def display(message, is_warning=false):
    if is_warning: 
        print('Warning !!!')
    print(message)

# import module as namespace 
import helpers
helpers.display('Not a warning')

from helpers import * #imported in current namesapce 
display('Not a warning')

from helpers import display #
display('Not a warning') 
"""
pip install colorma 
pip install -r requirements.txt 

requirements.txt 
colorma 


Virtual Environments: 
by default, pip install packages globally, 
a folder that has all the code needed to run your application. 

#install virtual environment
pip install virtualenv 
#windows systems 
python -m venv <folder_name>
# OSX/Linux (bash)
virtualenv <folder_name> 

#Windoes systems 
#cmd.exe 
<folder_name>\Scripts\Activate.bat 
#powershell 
<folder_name>\Scripts\Activate.ps1 
#bash shell 
. ./<folder_name>/Scripts/activate 

# OSX/Linux bash 
<folder_name>/bin/activate 


Call an API: 
Calling Computer Vision API: 
request library simplifies 



JSON: 
JavaScript Object Notation: basically key value pairs. 

import JSON 

Create JSON from Dictionary 
json.dump(person_dict)
You can do dictionary in dictionary or list in dictionary. 

Managing Subscription Key: 

using environment variable: 
    connecting to a database 
    determining the operating system 
    system level
    user level 
    application level 


import os 
os_version = os.getenv('OS')
print(os_version)

# .env file 
DATABASE = SAMPLE_CONNECTION_STRING 

# app.py 
from dotenv import load_dotenv 
import os 
load_dotenv() 
database = os.getenv('DATABASE')
print(database)

Decorators: 
Objects : Noun, Data Constructs 
Function/Methods: Verb, Actions 
Decorators: Adjectives, add additional meaning to our code. 
            common in frameworks. 

#snippet from flask 
#register https://myserver.com 
//router is a decorator
@route('api/products')
def get_products:
    # code to list from databse 
    pass 

def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')

    return wrapper 

@logger
def sample():
    print('--Inside sample function')




"""



from datetime import datetime, timedelta
import sys

print('Welcome to b1k Shipping Agency.\nPlease provide your information to create your shipping profile. \n')
print('Once we have your shipping profile, we can ship you your order. \n')
first_name = ""
last_name = ""

while(len(first_name)<=0 and len(last_name)<=0):
    print('Please provider your first name and last name.')
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')

print('Welcome, {} {}'.format(first_name.capitalize(),last_name.capitalize()) )

dateofbirth = input('Please enter your date of birth in dd/mm/YYY format.')
try:
     birthday_date = datetime.strptime(dateofbirth, '%d/%m/%Y')
except: #you can also have else in here 
    print('Something really went wrong. Please enter your date of birth in right format.')
    sys.exit('Exiting Now')
finally: 
    print('Thank you for entering your date of birth.')
print('Your Birthday is: '+ str(birthday_date))


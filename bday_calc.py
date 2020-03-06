import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

cur_month = int(datetime.date.today().month)

cur_day = int(datetime.date.today().day)

cur_year = int(datetime.date.today().year)

print(f'\nThe Current date is set to {cur_month}/{cur_day}/{cur_year}\n')

bday_month = int(input('Enter the month you were born: '))
while cur_month not in range(1, 12):
    print('Not a vaild month. Please try again')
    cur_month = input('Enter the month you were born: ')

bday_day = int(input('Enter the day you were born: '))
while cur_day not in range(1, 31):
    print('Not a vaild day. Please try again')
    cur_day = input('Enter the day you were born: ')

bday_year = int(input('Enter the year you were born: '))
while cur_year not in range(1900, 2100):
    print('Not a vaild year. Please try again')
    cur_year = input('Enter the year you were born: ')

print(f'\nYour birthday is {bday_month}/{bday_day}/{bday_year}\n')

cur_date = (str(cur_year + "-" + cur_month + "-" + cur_day))
bday_date = (join(bday_year + "-" + bday_month + "-" + bday_day))
print(cur_date)
print(bday_date)
age_day = days_between(cur_date, bday_date)

cur_age = cur_year - bday_year - 1

if bday_month < cur_month:
    cur_age = cur_age + 1

if bday_month == cur_month and bday_day < cur_day:
    cur_age = cur_age + 1

if bday_month == cur_month and bday_day == cur_day:
    print("It's your birthday! Happy Birthday!")
    cur_age = cur_age + 1

print(f'You are {cur_age} years old.\n')

if bday_month == cur_month and bday_day > cur_day:
    if bday_day - cur_day == 1:
        print('Your birthday is in 1 day!\n')
    else:
        day_diff = bday_day - cur_day
        print(f'Your birthday is in {day_diff} days!\n')

if bday_month > cur_month:
    month_diff = bday_month - cur_month
    if month_diff == 1:
        print('Your birthday is Next month')
    else:
        print(f'Your birthday is in {month_diff} months.')
    
print('\nHow old would you be on each planet? ')
print('------------------------------------')
print(f'Mercury -\t {float("{0:.2f}".format(age_day / 87.97))} years old')
print(f'Venus -\t\t {float("{0:.2f}".format(age_day / 224.7))} years old')
print(f'Earth -\t\t {float("{0:.2f}".format(age_day / 365))} years old')
print(f'Mars -\t\t {float("{0:.2f}".format(age_day / 686.2))} years old')
print(f'Jupiter -\t {float("{0:.2f}".format(age_day / 4328.9))} years old')
print(f'Saturn -\t {float("{0:.2f}".format(age_day / 10752.9))} years old')
print(f'Uranus -\t {float("{0:.2f}".format(age_day / 30663.65))} years old')
print(f'Neptune -\t {float("{0:.2f}".format(age_day / 60148.35))} years old')
print(f'Pluto -\t\t {float("{0:.2f}".format(age_day / 90735.35))} years old')
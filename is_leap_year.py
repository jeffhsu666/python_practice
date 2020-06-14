

def is_leap(year='2020'):
    year = int(year)
    if (year % 400 == 0) & (year % 3200 != 0):
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = input('Please enter a year to check if it is a leap year: ')

if is_leap(year):
	print(year, 'is a leap year')
else:
	print(year, 'is not a leap year')


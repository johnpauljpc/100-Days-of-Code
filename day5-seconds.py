#A python program to calculate the number of seconds in a year
isleap = input('Is it a leap year (Yes or No): ')

oneDay = 60 * 60 * 24
if (isleap.lower() == 'yes'):
    seconds = oneDay * 366
    print("we have %d seconds in a leap year" %seconds)

elif (isleap.lower() == 'no'):
    seconds = oneDay * 365
    print("We have %d seconds in a year" %seconds)
else:
    print("Your input is invalid")

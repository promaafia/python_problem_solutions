'''
    1.25. Write a program that read any date in the format DD-MM-YYYY and displays day, month and year separately
'''
import datetime

# take date as input
date = input('Enter date as format DD-MM-YYYY: ')
# convert string date as date
date_formate = datetime.datetime.strptime(date, '%d-%m-%Y')

print("day: ", date_formate.day)
print("Month: ", date_formate.month)
print("Year: ", date_formate.year)

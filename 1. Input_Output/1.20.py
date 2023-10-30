'''
    1.20. Write a program that read any date and displays in the format DD/MM/YYYY
'''
import datetime

# get the current date and time
now = datetime.datetime.now()

# take only date and formatting as dd/mm/YY
currentDate = now.strftime("%d/%m/%Y")
print(currentDate)

'''
'strftime' is used to convert datetime to string and it consists of various format codes that define specific parts of the date and time.
"%Y-%m-%d %H:%M:%S" or "%d/%m/%Y, %H:%M:%S"

%a - sun, mon...
%A - Saturday, Monday...
%w - weekday as decimal like 1, 2, 3...
%b -  jan, feb, mar...
%B - January, February...
%Y - 2020, 2023...
%y - year without century like 00, 23, 20
'''

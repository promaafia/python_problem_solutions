'''
    1.23. Write a program that read any date and displays in the format DD,MM,YYYY
'''
import datetime

# get the current date and time
now = datetime.datetime.now()
date = now.strftime("%d,%m,%Y")
print(date)
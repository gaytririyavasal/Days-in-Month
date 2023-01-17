# File: DaysInMonth.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 9/22/2021
# Date Last Modified: 9/24/2021
# Description of Program: The following program will return the number of days in the month entered for the specified year.

def main () :
    year = int(input("Please enter a year: "))
    num = int(input("Please enter a month: "))
    
    if (num == 1):
        month = "January"
    elif (num == 2):
        month = "February"
    elif (num == 3):
        month = "March"
    elif (num == 4):
        month = "April"
    elif (num == 5):
        month = "May"
    elif (num == 6):
        month = "June"
    elif (num == 7):
        month = "July"
    elif (num == 8):
        month = "August"
    elif (num == 9):
        month = "September"
    elif (num == 10):
        month = "October"
    elif (num == 11):
        month = "November"
    else:
        month = "December"

    if(year % 400 == 0):
        LeapYear = True
    elif(year % 100 == 0):
        LeapYear = False
    elif(year % 4 == 0):
        LeapYear = True
    else:
        LeapYear = False

    if LeapYear and month == "February":
       print(month, year, "has 29 days")

    if (month == "January"):
        print(month, year, "has 31 days")
    elif (month == "February" and not LeapYear):
        print(month, year, "has 28 days")
    elif (month == "March"):
        print(month, year, "has 31 days")
    elif (month == "April"):
        print(month, year, "has 30 days")
    elif (month == "May"):
        print(month, year, "has 31 days")
    elif (month == "June"):
        print(month, year, "has 30 days")
    elif (month == "July"):
        print(month, year, "has 31 days")
    elif (month == "August"):
        print(month, year, "has 31 days")
    elif (month == "September"):
        print(month, year, "has 30 days")
    elif (month == "October"):
        print(month, year, "has 31 days")
    elif (month == "November"):
        print(month, year, "has 30 days")
    elif (month == "December"):
        print(month, year, "has 31 days")

main()

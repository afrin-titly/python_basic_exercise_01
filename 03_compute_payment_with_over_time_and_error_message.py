"""
Write a program that will take hours and rate per hour as input and will compute the total payment.  your program will give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Here your program will show an error message for non-numeric value of hours/rate. After showing the error message, the program will exit

Example 01:
Enter Hours: 45
Enter Rate: 10
Pay: 475.00


Example 02:
Enter Hours: 45
Enter Rate: nine
Error, please enter numeric input

"""


# your code here


# take hours and rate as input



try:
    pay = 0
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate:'))
    if hours <= 40:
        pay = hours * rate
    else:
        over_time = hours-40
        pay = (40 * rate) + (over_time * rate*1.5)

    print('Pay: {:.2f}'.format(pay))

except ValueError:
    print("Error, please enter numeric input")

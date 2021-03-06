"""
Write a program that will take hours and rate per hour as input and will compute the total payment.
Here your program will give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Example:
Enter Hours: 45
Enter Rate: 10
Pay: 475.00

"""

# take hours and rate as input
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate:'))
pay = 0

# your code here
if hours <= 40:
    pay = hours * rate
else:
    over_time = hours-40
    pay = (40 * rate) + (over_time * rate*1.5)


print('Pay: {:.2f}'.format(pay))

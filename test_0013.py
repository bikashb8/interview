#Python program to check whether an years is leap or not.
year = int(input("Enter the year:"))
if year % 4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
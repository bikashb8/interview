#Python program to show the last digit of a number is divisible by 3 or no
num = int(input("Enter the number:"))
digit = num %10
if digit %3==0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 3")
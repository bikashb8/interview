#Python program to calculate the electricity bill
#first 100 units no charge , next 100 units rs 5 , after 200 charge Rs 10
#350 unit is Rs 2000
unit = int(input("What is the unit for billable:"))
rem = unit - 100
rem1 = (unit - rem)*5
rem2 = (unit-200)*10
if unit <=100:
    print("Free as per rule")
elif unit>100 and unit<=200:
    print("The bill is :",rem1)
else:
    print("The bill is :",(rem2+rem1))
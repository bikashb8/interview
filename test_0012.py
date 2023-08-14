#python program to accept the cost price of a bike and display the road tax to be paid according to the following criteria
#>100000 15 % tax , >50000 and <=100000 10% tax <=50000 5% tax
price_vehicle = int(input("Enter the amount of the vehicle price:"))
tax = 0
if price_vehicle > 100000:
    tax = 15 / 100 * 100000
    print("You have to pay 15 % tax.",tax)
elif price_vehicle > 50000 and price_vehicle <=100000:
    tax = 10/100*100000
    print("You have pay tax 10%.")
else:
    tax = 5/100*100000
    print("You have to pay 5 % tax.")
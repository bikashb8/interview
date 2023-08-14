#Python program to check the pecentage with grade
#Criteria : >90 -- A grade, >80 and <=90 B grade, >=60 and <=80 C grade, below 60 d
percentage = int(input("Enter the percentage secured:"))
if percentage > 90:
    print("You are scored A ")
elif percentage >80 and percentage <= 90:
    print("You are scored B")
elif percentage >=60 and percentage <=80:
    print("You are scored C")
else:
    print("You are scored D")
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(
    input("What percentage of tip would you like to give? 10, 12, or 15? "))
person = int(input("How many person should pay the bill? "))
bill_pp = (total_bill + (tip_percent/100)*total_bill)/person
print("Each person should pay: " ,"{:.2f}".format(round(bill_pp, 2)))

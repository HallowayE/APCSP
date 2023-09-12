
amount = float(input("Amount Saved: "))
rate = float(input("Interest Rate: "))
time = float(input("Number of Days at Interest: "))

interest = round(amount*pow(1+((0.01*rate)/365), time), 2)
earned = round(interest - amount, 2)
print("The interest earned is $", earned)
print("The total amount in savings is now $", interest)

"""
Amount Saved: 5000
Interest Rate: 11.5
Number of Days at Interest: 900
The interest earned is $ 1638.96
The total amount in savings is now $ 6638.96
"""
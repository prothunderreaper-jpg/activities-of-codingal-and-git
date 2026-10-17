print("Welcome to bill ")

unit_consumed = float(input("How much unit you consume: "))

unit_price = 10.45

if unit_consumed >= 200:
    bill = unit_price * unit_consumed
    bill += 5000
    print("bill is", bill)

else:
    bill = unit_price * unit_consumed
    print(" bill is ", bill)
    
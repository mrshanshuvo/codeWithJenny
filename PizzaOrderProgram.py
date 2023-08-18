bill = 0
size = input("What size of Pizza do you want(S/M/L)?")

if size == 's' or size == 'S':
    print("Small Size Pizza is 100 TK")
    bill += 100
elif size == 'm' or size == 'M':
    print("Medium Size Pizza is 200 TK")
    bill += 200
elif size == 'l' or size == 'L':
    print("Large Pizza is 300 TK")
    bill += 300
else:
    print("Please Enter Valid Input")

pepperoni = input("Do you want Pepperoni(Y/N)?")

if pepperoni == 'y' or pepperoni == 'Y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50

cheese = input("Do you want extra cheese(Y/N)?")

if cheese == 'y' or cheese == 'Y':
    bill += 20

print(f"Your Final bill is {bill} TK")
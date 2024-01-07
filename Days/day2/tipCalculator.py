print("Welcome to tip calculator")
amount = int(input("What is the amount?\n "))
valid = False

people = 1
tip = 0
while not valid:
    tip = int(input("What will be the Tip percentage?(eg. 10, 12 or 15)\n"))
    people = int(input("How many people to split the bill?\n "))
    if people > 0 and (tip >= 0):
        valid = True
    else:
        print("Tip or number of people cannot be zero or less")
   
Result = (amount + amount*(tip/100)) / people
print(f"The Amount to be paid by each person is Rs {Result}")
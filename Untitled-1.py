age = int(input("Age?: "))
mem = input("Member or Non-Member: ")

if age < 18:
    if mem == "Member":
        print("₱450.00")
    else:
        print("₱650.00")
elif age >= 18 and age <= 65:
    if mem == "Member":
        print("₱550.00")
    else:
        print("₱750.00")
elif age > 65:
    if mem == "Member":
        print("₱400.00")
    else:
        print("₱600.00")
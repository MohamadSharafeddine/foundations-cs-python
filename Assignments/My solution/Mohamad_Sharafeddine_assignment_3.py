items = [["Cheese", 1, 0], ["Chocolate", 2, 0], ["Tomato", 1, 0], ["Potato", 2, 0], ["Soap", 0.5, 0], ["Popcorn", 0.7, 0]]
order = []
coupons = []
total = 0

def mainMenu():
    while True:
        print("1. To start a new order\n2. To close the program")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            startNewProgram()
        elif choice == 2:
            print("bye bye")
            break
        else:
            print("Invalid input")

def startNewProgram():
    while True:
        print("1. To add a new item\n2. To check the total of the bill\n3. To add a coupon\n4. To checkout")
        choice_new_program = int(input("Enter your choice: "))
        if choice_new_program == 1:
            addNewItem()
        elif choice_new_program == 2:
            checkTotal(total)
        elif choice_new_program == 3:
            addCoupon(total)
        elif choice_new_program == 4:
            checkout()
            break
        else:
            print("Invalid input")
            
def addNewItem():
    choice = input("Enter product you want to buy: ")
    match = False
    for item in items:
        if choice.lower() == item[0].lower():
            match = True
            # for ordered_item in range(len(items)):
            #     print(ordered_item)
            #     print("test")
            #     if choice.lower() == ordered_item[0].lower():
            #         ordered_item[2] += 1
            #     else:
            #         order.append(item.copy())
            order.append(item.copy())
            print(f"{item[0]} was added to your order.")
    if not match:
        print("Item not found")
    
    for ordered_item in order:
        if choice.lower() == ordered_item[0].lower() :
            ordered_item[2] += 1
    
def checkTotal(total):
    for ordered_item in order:
        total += (ordered_item[1] * ordered_item[2])
    print(f"The total of your bill is {total}")

def addCoupon(total):
    coupon = int(input("Enter the value of your coupon: "))
    coupons.append(coupon)
    total -= coupon
    print(total)
    
def checkout():
    print("Items bought: ")
    for ordered_item in order:
        print(f"{ordered_item[0]} x {ordered_item[2]}")
    print(f"Total: {total}")
    print(f"Coupons: {sum(coupons)}")
    print(f"Total after coupons: {total - sum(coupons)}")

mainMenu()
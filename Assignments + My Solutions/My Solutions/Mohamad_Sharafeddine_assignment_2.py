# # Exercise 1
# number = input("Enter a number: ")
# print(f"{number} has {len(number)} digits")

# print("")
# # Exercise 2
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print("*" * i)

# print("")
# # Exercise 3
# list1=[54, 76, 2, 4, 98, 100]
# int1 = int(input("Enter the first integer: "))
# int2 = int(input("Enter the second integer: "))
# while int1 >= int2:
#     int1 = int(input("Enter the first integer: "))
#     int2 = int(input("Enter the second integer (must be bigger than the first integer): "))
# for num in list1:
#     if int1 <= num <= int2:
#         print(num)

# print("")
# Exercise 4
names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
    letter = input("Enter a letter: ")
    for name in names:
        if letter.lower() or letter.upper() in name:
            print(name)
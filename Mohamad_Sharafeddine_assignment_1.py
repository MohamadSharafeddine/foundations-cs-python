# Exercise 1
top = float(input("Enter top number: "))
bottom = float(input("Enter bottom number: "))
val = float(input("Enter value: "))

if top > val > bottom:
    print("True")
else:
    print("False")

print("")
# Exercise 2
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b > c:
    print("The maximum value is a")
    print("The minimum value is c")
elif a > c > b:
    print("The maximum value is a")
    print("The minimum value is b")
elif b > a > c:
    print("The maximum value is b")
    print("The minimum value is c")
elif b > c > a:
    print("The maximum value is b")
    print("The minimum value is a")
elif c > a > b:
    print("The maximum value is c")
    print("The minimum value is b")
elif c > b > a:
    print("The maximum value is c")
    print("The minimum value is a")

print("")
# Exercise 3
total_grade = int(input("Enter your total grade: "))
if total_grade > 89:
    print("Your letter grade is A")
elif total_grade > 79:
    print("Your letter grade is B")
elif total_grade > 69:
    print("Your letter grade is C")
elif total_grade > 59:
    print("Your letter grade is D")
elif total_grade <= 59:
    print("Your letter grade is F")
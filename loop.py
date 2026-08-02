# 1. if-else statement
if True:
    print("This is true")  # This is true
else:
    print("This is false")

# 2. Shorthand if-else statement
x = 5
y = 10
result = "x is greater than y" if x > y else "x is less than y"
print(result)

# 3. if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# 4. Match statement
x = 5
match x:
    case 5:
        print("x is 5") # Return this value
    case 10:
        print("x is 10")
    case _:
        print("x is something else")

""" 
Ex1: Viết 1 chương trình nhập 1 số integer .
Nếu a là số chẵn thì in ra "a là số chẵn"
Nếu a là số lẻ thì in ra "a là số lẻ"   
"""
a = int(input("Nhập 1 số integer: "))
if a % 2 == 0:
    print(f"{a} là số chẵn")
else:
    print(f"{a} là số lẻ")
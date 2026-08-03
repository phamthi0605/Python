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

"""
Ex2: Viết 1 chương trình nhập 2 integer a và b.
Nếu a > b or = b thì in ra màn hình "a is greater than or equal to b"
Ngược lại, in ra màn hình "a is less than b"
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")   

""" 
Ex3: Viết 1 chương trình nhập tên 2 người. 
Kiểm tra xem nếu tên là giống nhau thì in ra "Their names are the same"
Ngược lại, "Their names are NOT the same"
 """
name1 = input("Nhập tên người thứ nhất: ")
name2 = input("Nhập tên người thứ hai: ")
if name1 == name2:
    print("Their names are the same")
else:
    print("Their names are NOT the same")

""" 
Ex4: Viết 1 chương trình để nhập 1 số integer và kiểm tra xem số đó có
nằm trong range[22-65]
 """
a = int(input("Nhập 1 số integer: "))
if 22 <= a <= 65:
    print(f"{a} nằm trong range [22-65]")
else:
    print(f"{a} không nằm trong range [22-65]")

""" 
Ex5: Viết 1 chương trình nhập điểm của học sinh và in ra rating của học sinh đó
points on [0, 4) : EASY
points in the interval [4, 6) : C
points in the interval [6, 8) : B
points in the range [8, 10] : A
other case: invalid number
 """
points = float(input("Nhập điểm của học sinh: "))
if 0 <= points < 4:
    print("Rating: EASY")
elif 4 <= points < 6:
    print("Rating: C")
elif 6 <= points < 8:
    print("Rating: B")
elif 8 <= points <= 10:
    print("Rating: A")
else:
    print("Invalid number")
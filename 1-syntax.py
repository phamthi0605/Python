import cmath

# 1. variable
a = int(3)
print(a)

b = float(5)
print(b)

name = ("Bob")
print(name)

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Naming Rule valid
name = "Alice"
_company = "TechCorp" 

# Naming Rule invalid
# 1name = "John"  # Cannot start with a number
# class = "Math"  # Cannot use Python keywords as variable names

# 2. Data types

# Numeric types
x = 5  # int
y = 3.14  # float
z = 2 + 3j  # complex
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Dictionary: lưu trữ các cặp key-value, không theo thứ tự
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person) 
# {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Boolean: lưu trữ giá trị True hoặc False
is_active = True
print(is_active)  # True

# Set: lưu trữ các giá trị duy nhất, không theo thứ tự
print(fruits)  # {'banana', 'cherry', 'apple'}

# Sequence types
# String
greeting = "Hello, World!"
print(greeting)  # Hello, World!

# List: lưu theo thứ tự và có thể thay đổi
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

list_a = ["banana", "apple", "cherry"]
list_b = list(list_a)
list_a[0] = "watermelon"
print(list_a)  # ['watermelon', 'apple', 'cherry']
print(list_b)  # ['banana', 'apple', 'cherry']

# Tuple: lưu theo thứ tự và không thể thay đổi
coordinates = (10, 20)
print(coordinates)  # (10, 20)  

# 3.Assign Operators
x = 5
print(x)  # 5

x += 3  # x = x + 3
print(x)  # 8

x -= 3  # x = x - 3
print(x)  # 5


x *= 3  # x = x * 3
print(x)  # 15

x/= 3  # x = x / 3
print(x)  # 5.0

x %= 3  # x = x % 3
print(x)  # 2.0


# 4. Relational Operators
a = 10
b = 5

a == b  # False

a != b  # True

a > b  # True

a < b  # False

a >= b  # True

a <= b  # False

# 5. Logical Operators
x = 5
y = 10
print(x < 10 and y > 5)  # True
print(x < 10 or y < 5)   # True
print(not(x < 10))        # False: trả về giá trị ngược lại của biểu thức logic


""" 
Ex1: Viết một chương trình để in thông tin về 1 người gồm tên, tuổi và in ra tuổi của người đó
sau 10 năm với format: "After 10 years, {name} will be {age}"
 """
name = "Thi"
age = 26
print(f"After 10 years, {name} will be {age + 10}")

""" 
Ex2:In ra 2 giá trị a và b, sau đó in ra giá trị của a và b sau khi hoán đổi, 
với yêu cầu không được khởi tạo thêm bất kỳ biến tạm nào.
"""
a = 5
b = 10
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

""" 
Ex3: Viết 1 chương trình nhập 2 giá trị a và b và in ra màn hình true nếu a>b, a<b hoặc false nếu ngược lại
 """
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# if a > b:
#     print("True")
# else:
#     print("False")

# Casting types
# 1. Implicit Casting: Python tự động chuyển đổi kiểu dữ liệu khi cần thiết, 
# ví dụ: int -> float
x = 5  # int
y = 2.5  # float
z = x + y  # int + float -> float
print(z)  # 7.5

# 2. Explicit Casting: Người dùng tự chuyển đổi kiểu dữ liệu bằng cách sử dụng các hàm như int(), float(), str(), list(), tuple(), set()
# int() - chuyển đổi sang kiểu số nguyên
a = "10"
b = int(a)  # chuyển đổi từ string sang int
print(b)  # 10

# float() - chuyển đổi từ int sang kiểu số thực
c = 3
d = float(c)  # chuyển đổi từ int sang float
print(d)  # 3.0

# str() - chuyển đổi sang kiểu chuỗi
e = 5
f = str(e)  # chuyển đổi từ int sang string
print(f)  # "5"

# list() - chuyển đổi sang kiểu danh sách
g = (1, 2, 3)
h = list(g)  # chuyển đổi từ tuple sang list
print(h)  # [1, 2, 3]

# tuple() - chuyển đổi sang kiểu tuple
i = [1, 2, 3]
j = tuple(i)  # chuyển đổi từ list sang tuple
print(j)  # (1, 2, 3)

# set() - chuyển đổi sang kiểu set
k = [1, 2, 2, 3]
l = set(k)  # chuyển đổi từ list sang set
print(l)  # {1, 2, 3}

# sự khác nhau giữa list, tuple và set
# List: lưu theo thứ tự, có thể thay đổi, cho phép trùng lặp
# Tuple: lưu theo thứ tự, không thể thay đổi, cho phép trùng lặp
# Set: lưu trữ các giá trị duy nhất, không theo thứ tự, không cho phép trùng lặp




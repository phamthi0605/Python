# 1. Loop for

for i in range(5):
    print(i)


itemList = ["apple", "banana", "cherry"]

for item in itemList:

    print(item)



# Ex1: Nhập 1 số integer N và in ra các số tư 1 đến N

# N = int(input("Nhập 1 số integer N: "))
N = 10
for i in range(1, N+1):
    print(i)


# Ex2: Nhập 2 số integer a và b. In ra các số từ a đến b
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
a = 1
b = 3
if a < b:

    for i in range(a, b+1):
        print(i)


# Ex3: Nhập 2 số integer a và b. In ra tổng của các số chẵn từ a và b
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
a = 1
b = 6
sum_even = 0

for i in range(a, b+1):

    if i % 2 == 0:

       sum_even += i

print(sum_even)


# Ex4: Nhập 1 số integer và kiểm tra xem số number có nằm trong rang [22-65]
# a = int(input("Nhập a: "))

# if 22 <= a <= 65:

#     print("Có")

# else:

#     print("Không")


# Ex5: Nhập 2 số a và b và in tất cả các số chia hết cho 3 từ a đến b
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# for i in range(a, b+1):
#     if i % 3 == 0:
#         print(i)

# Ex6: Nhập 1 số n và in ra giá trị n! = n*(n-1)*(n-2)*...*1
# n = int(input("Nhập số n: "))
n = 6
factorial = 1
for i in range(1, n+1):
   factorial *= i
print(factorial)

# Ex7: Viết một chương trình để nhập tên một loại trái cây, 
# kiểm tra xem loại trái cây đó có trong giỏ hay không và in kết quả ra màn hình.
list_fruits = ["Apple", "Banana", "Cherry", "Orange", "Pineapple"]

name_fruit = input("Nhập tên một loại trái: ")

if name_fruit in list_fruits:
    print(f"Đúng, {name_fruit} có trong giỏ.")
else:
    print(f"Không, {name_fruit} không có trong giỏ.")

# list_fruits = ["Apple", "Banana", "Cherry", "Orange", "Pineapple"]

# name_fruit = input("Nhập tên một loại trái: ")

# check = False

# for fruit in list_fruits:
#     if name_fruit == fruit:
#         check = True

# if check:
#     print(f"{name_fruit} có trong giỏ.")
# else:
#     print(f"{name_fruit} không có trong giỏ.")
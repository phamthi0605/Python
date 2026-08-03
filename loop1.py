# 1. Loop for
for i in range(5):
    print(i)

itemList = ["apple", "banana", "cherry"]
for item in itemList:
    print(item)


# Ex1: Nhập 1 số integer N và in ra các số tư 1 đến N
# N = int(input("Nhập 1 số integer N: "))
N = 6
for i in range(1, N+1):
    print(i)

# Ex2: Nhập 2 số integer a và b. In ra các số từ a đến b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a < b:
    for i in range(a, b+1):
        print(i)

# Ex3: Nhập 2 số integer a và b. In ra tổng của các số chẵn từ a và b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
sum_even = 0
for i in range(a, b+1):
    if i % 2 == 0:
       sum_even += i
print(sum_even)

# Ex4: Nhập 1 số integer và kiểm tra xem số number có nằm trong rang [22-65]
a = int(input("Nhập a: "))

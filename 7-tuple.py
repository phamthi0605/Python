# tuple: để lưu các giá trị không thay đổi, có thứ tự

# 1. count: đếm số lần xuất hiện của một giá trị
my_tuple =  (1, 2, 3, 4, 1, 1)
print(my_tuple.count(1))
# 3

# 2. index(): tìm vị trí của một giá trị (index bắt đầu là 0)
print(my_tuple.index(1))
# 0

# 3. truy cập phần tử bằng index
tuple_index = ("Hang", "Thi", "Huong")
print(tuple_index[1])
# Thi

# 4. Cắt Tuple
print(tuple_index[1:3])
# ('Thi', 'Huong')

# 5. len(): trả về độ dài của tuple
tuple_len = ("Hang", "Thi", "Huong", "Me")
print(len(tuple_len))
# 4

for name in tuple_len:
    print(name)
# Hang
# Thi
# Huong
# Me


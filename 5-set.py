# 1. Set là một tập hợp có các đặc điểm:
# Không có thứ tự (unordered)
# Không thể thay đổi (unchangeable) giá trị
# Không cho phép các giá trị trùng lặp (no duplicate values)

# Example:
setFruits = {"Banana", "Cherry"}
setFruits.add("Apple")
print(setFruits);

# update: thêm các phần tử hoặc update một tập hợp khác vào một tập hợp khác
setFruits.update(["Orange"])
print(setFruits);

# Thêm các phần tử của set_B vào set_A
set_A = {"a", "b"}
set_B = {"c", "d"}
set_A.update(set_B)
print(set_A); # {'c', 'b', 'a', 'd'}

# Thêm các phần tử của list_A vào set_C
set_C = {"e", "f"}
list_A = ["g", "h"]
set_C.update(list_A)
print(set_C) # {'g', 'e', 'h', 'f'}

# Thêm Tuple vào Set
set_D = {"i", "j"}
tuple_A = ("a", "b")
set_D.update(tuple_A)
print(set_D) # {'j', 'i', 'a', 'b'}

# String → Set
set_E = {"w", "j"}
string_n = ("Hello")
set_E.update(string_n)
print(set_E) # {'l', 'o', 'e', 'H', 'w', 'j'}


# Xử các phần tử trùng qua Set
new_list = [1,2,3,3,4,4,5,6,7,7]
unique_number = set(new_list)
print(unique_number) # {1, 2, 3, 4, 5, 6, 7}

# Remove: Xóa phần tử khỏi Set. Nếu phần tử không có trong Set thì sẽ báo lỗi.
set_move = {"Thi", "Hang", "Huong"}
set_move.remove("Thi")
print(set_move) # {'Huong', 'Hang'}

# Discard: xoá phần tử trong Set nhưng không báo lỗi nếu phần tử không tồn tại
set_move.discard("haha")
print(set_move) # {'Huong', 'Hang'}

# Pop: xoá phần tử cuối cùng.
set_pop = {"Thi", "Hang", "Huong","Hoa"}
print(set_pop) # {'Huong', 'Thi', 'Hang'}

# Clear: xoá hết các phần tử trong Set
set_clear = {"a", "b", "c", "d", "e"}
set_clear.clear()
print(set_clear)
# set()

# Del: xoá set
# set_del = {"a", "b", "c", "d"}
# del set_del # không thể sử dụng sau khi đã xoá

# Union: gộp 2 Set và bỏ các giống nhau
set_1 = {1,2}
set_2 = {2,3,4}
print(set_1.union(set_2))
print(set_1 | set_2)

# Intersection: lấy các phần tử chung của cả 2 Set
set_3 = {1,2,3}
set_4 = {2,3,4}
print(set_3.intersection(set_4)) # {2, 3}
print(set_3 & set_4) # {2, 3}

# Difference: lấy các phần tử chỉ có trong Set thứ nhất
set_5 = {1,2,3,4,5}
set_6 = {5,6,7,8}
print(set_5.difference(set_6)) # {1, 2, 3, 4}
print(set_5 - set_6) # {1, 2, 3, 4}

# Symmetric Difference: lấy các phần tử không chung giữa 2 set
set_7 = {1,2,3,4}
set_8 = {1,2,5,6}
print(set_7.symmetric_difference(set_8)) # {3, 4, 5, 6}
print(set_7 ^ set_8) # {3, 4, 5, 6}

# Exercise:
# Viết 1 chương trình tạo 1 mã công dân mới
# citizen_id = {"123111", "123456","123321", "321123"}
# 1. Thêm 1 mã citizen_id mới
# 2. xoá citizen_id đã tồn tại
citizen_id = {"123111", "123456","123321", "321123"}
citizen_id.add("123457")
print(citizen_id) # {'123456', '123457', '123111', '123321', '321123'}

citizen_id.remove("123456")
print(citizen_id) # {'321123', '123457', '123321', '123111'}


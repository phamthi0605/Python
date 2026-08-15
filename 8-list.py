# List:
# - Dùng để lưu nhiều giá trị
# - Có thứ tự (ordered)
# - Có thể thay đổi (mutable)
# - Có thể truy cập bằng index
# - Có thể chứa giá trị trùng nhau
# - Có thể chứa nhiều kiểu dữ liệu khác nhau

# 1. Tạo List
my_list = [1, 2, 3,4, 5]

# 2. Appending: Thêm một phần tử vào cuối
my_list.append(6)
print(my_list)
# [1, 2, 3, 4, 5, 6]

# 3. Inserting: Thêm một phần tử vào vị trí cụ thể
my_list.insert(2, 7) # Thêm 7 vào vị trí 2
print(my_list)
# [1, 2, 7, 3, 4, 5, 6]

# 4. Removing: Xóa một phần tử khỏi list
my_list.remove(7) 
print(my_list)
# [1, 2, 3, 4, 5, 6]

# 5. Extend: Thêm một list vào cuối list
my_list.extend([7, 8, 9])
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 6. Pop(): xoá theo index và trả về phần tử bị xoá
my_list.pop(1)
print(my_list)
# [1, 3, 4, 5, 6, 7, 8, 9]

# 7. Clear: xoá toàn bộ list
my_list.clear()
print(my_list)
# []

# 8. Index(): tìm vị trí của một giá trị
new_list = ["A", "B", "C", "D"]
print(new_list.index("B"))
# 1

new_list.extend(["F", "W", "G"])
print(new_list)
# ['A', 'B', 'C', 'D', 'F', 'W', 'G']

# 9. Sort(): sắp xếp
new_list.sort()
print(new_list)
# ['A', 'B', 'C', 'D', 'F', 'G', 'W']

new_list.reverse()
print(new_list)
# ['W', 'G', 'F', 'D', 'C', 'B', 'A']

# 10. Copy(): tạo 1 bản sao
list1 = new_list.copy()
print("List copy: ",list1)
# List copy:  ['W', 'G', 'F', 'D', 'C', 'B', 'A']



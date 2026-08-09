# Dictionary là một tập hợp không có thứ tự,
# có thể thay đổi và không cho phép các giá trị bị trùng lặp.

# 1. Add: thêm phần tử mới
dict_user = {
    "name" : "Thi",
    "options" :{
        "age" : 27,
        "male": "female"
    } 
}
dict_user["options"]["status"] = "single"
print(dict_user)
# {'name': 'Thi', 'options': {'age': 27, 'male': 'female', 'status': 'single'}}

# 2. Update với key values đã tồn tại
dict_user["name"] = "Pham Thi"
print(dict_user)
# {'name': 'Pham Thi', 'options': {'age': 27, 'male': 'female', 'status': 'single'}}

# 3. Update: thêm 1 phần tử mới hoặc update một phần tử đã tồn tại.
# Hoặc có thể update dict với dict khác
dict_student = {
   "student_id" : "abc12",
   "infor": {
        "name": "Thi",
        "age" : 27,
        "address": "Ha Noi"
   }
}
print(dict_student)
# {'student_id': 'abc12', 'infor': {'name': 'Thi', 'age': 27, 'address': 'Ha Noi'}}

dict_student["infor"].update({"gender":"female"})
print(dict_student)
# {'student_id': 'abc12', 'infor': {'name': 'Thi', 'age': 27, 'address': 'Ha Noi'}}
# {'student_id': 'abc12', 'infor': {'name': 'Thi', 'age': 27, 'address': 'Ha Noi', 'gender': 'female'}}

dict_stu1 = {
    "student_id": "12",
    "name": "Thi cute"
}
dict_stu2 = {
    "age": 27,
    "address": "HN"
}
dict_stu1.update(dict_stu2)
print(dict_stu1)
# {'student_id': '12', 'name': 'Thi cute', 'age': 27, 'address': 'HN'}

# 4. Truy cập element trong dict
my_dict = {
    "name": "Hang Beo",
    "Major": "IT"
}
print(my_dict["name"])
# Hang Beo

my_infor = {
    "name" : "Pham Hang",
    "age" : 33,
    "compnay": "cmc",
    "position": "le ve"
}
for x in my_infor:
    print(x, ": ", my_infor.get(x))
# name :  Pham Hang
# age :  33
# compnay :  cmc
# position :  le ve    

# 5. Remove
# clear: xoá tất cả các phần tử
dict_clear = {
   "nick name" : "Hang phan boi",
   "address" : "BN"
}
dict_clear.clear()
print(dict_clear)
# {}

# Pop: xoá các phần tử với key cụ thể
dict_pop = {
    "name" : "abc1",
    "greeting": "Xin chao",
    "age" : 20
}
dict_pop.pop("age")
print(dict_pop)

# popitem(): loại bỏ cặp key-value được chèn gần nhất
dict_popItem = {
    "name" : "test",
    "infor": "abc",
    "languague": "english"
}
dict_popItem.popitem()
print(dict_popItem)

# Del dict: xoá 1 phần tử hoặc xoá 1 dict
dict_del = {
    "name": "test del",
    "test": "abc xyz",
    "exam": "math"
}
del dict_del["exam"]
print(dict_del)

# del dict_del
# print(dict_del) 
# Result: NameError: name 'dict_user' is not defined
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

# values: trả về list tất cả các giá trị của dict
dict_values = {
    "name": "Hang beo",
    "status": "single",
    "address": "HN"
}
print(dict_values.values());
# dict_values(['Hang beo', 'single', 'HN'])

#  keys(): trả về list tất cả các khóa của dict
dict_key = {
    "name": "Hang beo",
    "status": "single",
    "address": "HN",
    "company": "abc"
}
print(dict_key.keys()); 
# dict_keys(['name', 'status', 'address', 'company'])

# items(): trả về list tất cả các cặp khóa

dict_items ={
    "name": "Thi",
    "abc" : "Hi",
    "pos" : "12"
}
print(dict_items.items()); 
# dict_items([('name', 'Thi'), ('abc', 'Hi'), ('pos', '12')])

# copy: tạo một bản sao của dict
dict_copy = {
    "name" : "Hang",
    "status" : "single",
    "company" : "abc",
    "add" : "HN",
    "sport" : "no"
}
new_dict = dict_copy.copy()
print("dict copy: ", new_dict)
#  {'name': 'Hang', 'status': 'single', 'company': 'abc', 'add': 'HN', 'sport': 'no'}

# setdefault(key, default= None): trả về 1 list của tất cả các giá trị trong dict
dict_samp = {
    "name" : "Hang béo",
    "gender" : "female"
}
dict_samp.setdefault("age")
print(dict_samp)
# {'name': 'Hang béo', 'gender': 'female', 'age': None}
#  Hoặc có thể truyền dict_samp.setdefault("age", 20)

# fromKeys(seq, value): trả về 1 dict với các key là các phần tử trong seq và giá trị là value
values = "one"
dict_check = {
    "name" : "Hang beo",
    "Hobby": "Eat",
    "gender" : "female"
}
new_dict = dict.fromkeys(dict_check, values)
print(new_dict)
# {'name': 'one', 'Hobby': 'one', 'gender': 'one'}

# Use in or not in to check elements is or not exist in dict:
dict_1 ={
    "name" : "Pham Hang", 
    "Hobby" : "Sleep",
    "gender" : "female"
}
if "name" in dict_1:
    print("Keys is exist in dict")
else:
    print("Not exist in dict")
# Keys is exist in dict

if "address" not in dict_1:
    print("True")
else:
    print("False")
# True


# Exercise 1:
#  Viết 1 chương trình để tìm books:
# Title, Author, Publisher
myBooks = [
    {
        "Title": "Doraemon",
        "Author": "Fujiko F. Fujio",
        "Publisher": "Shogakukan"
    },
    {
        "Title": "Harry Potter",
        "Author": "J.K. Rowling",
        "Publisher": "Bloomsbury"
    },
    {
        "Title": "Conan",
        "Author": "Gosho Aoyama",
        "Publisher": "Shogakukan"
    }
]
for book in myBooks:
    print("Title: ", book["Title"])
    print("Author:", book["Author"])
    print("Publisher:", book["Publisher"])
    print()
# Title:  Doraemon
# Author: Fujiko F. Fujio
# Publisher: Shogakukan

# Title:  Harry Potter
# Author: J.K. Rowling
# Publisher: Bloomsbury

# Title:  Conan
# Author: Gosho Aoyama
# Publisher: Shogakukan

# Exercise 2:
# Viết 1 chương trình để tìm user có số điện thoại kết thúc là 1 hoặc email trống
userdata  = [
    {
        "name" : "Jack",
        "age" : "12",
        "phone": "555-1316",
        "email": "jack12@gmail.com"
    },
    {
        "name": "Thi",
        "age": "14",
        "phone": "555-1112",
        "email": ""
    }
]
for user in userdata:
    if user["phone"].endswith("1") or user["email"] == "":
        print(user)
# {'name': 'Thi', 'age': '14', 'phone': '555-1112', 'email': ''}

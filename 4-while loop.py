# Ex1: Input interger n and display all odd numbers from n to 100.
# n = int(input("Enter an integer: "))
n = 90
print("Odd numbers from ", n, "to 100:")
while n <= 100:
    if n % 2 != 0:
         print(n, end =" ")
    n += 1  
    
# Ex2: Input interger n and display all integers divisible by 3 and 7 from n to 100.
# n = int(input("Enter an integer: "))
n = 1
print("\nIntegers divisible by 3 and 7 from ", n, "to 100")
while n <= 100:
    if n %3 == 0 and n %7 == 0:
         print(n, end=" ")
    n += 1

# Ex3: Calculate the sum of even number from 1 to 20
print("\n Sum of even numbers from 1 to 20: ")
sum= 0
i = 1
while i <= 20:
    if i %2 == 0 :
        sum += i
    i += 1
print(sum)

# Ex4: Input an integer n and checks if n is the ranges 22-65.
# if n is beween 22-65, print "Have a good day". Otherwise print "Enjoy".

n = int(input("Enter an integer: "))
if 22 <= n <= 65:
    print("Have a good day")
else:
    print("Enjoy")


#  Ex5: Input integer n, check if from 0 to n exist an integer divisible by 3.
n = int(input("Enter an integer:"))
for i in range(n):
    if i % 3 != 0:
        continue    
    print(i)
       
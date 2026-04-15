# oops: Object Oriented Programming System
#class: collections of variables and functions 
 

# Example -1 
# class test:
#     def wish(self):
#         print('Welcome to oops !!')

# t1 = test()
# t1.wish()

#Example -2 

# class test:

#     def add1(self):
#         num1 = 200
#         num2 = 100
#         res = num1+num2
#         print(f'Addition : {res}')

#     t1 = test()
#     t1.add()
#     x=


#Example- 3
#Insatnce Variable 
# __init__ is called constructor
# It will execute only once 
# Whenerv we create the object the constructor will execute 



# class test:
#     def __init__(self):
#         self.num1 = 10
#         self.num2 = 20 

# t1 = test()
# t2 = test()
# t1.num1 = 100
# t1.num2 = 200

# print(f't1 object data : {t1.num1}...{t1.num2}')
# print(f't2 object data : {t2.num1}...{t2.num2}')

# Example - 4 
# share common data to multiple objects

# class test:
#     company = "tcs...!"
#     def __init__(self,name):
#         self.name = name

# t1= test("Emp1")
# print(f'name of the employee{t1.name} and company name {t1.company}')

# t2= test("Emp2")
# print(f'name of the employee{t2.name} and company name {t2.company}')

#Example - 5 

# class test:
#     name = "TCS...!"

# t1 = test()
# t2 = test()
# print(f'Name...{t1.name}')
# print(f'Name...{t2.name}')

# test.name = "Oracle...!"
# print(f'Name...{t1.name}')
# print(f'Name...{t2.name}')

# Example 6 

# class test:
#     name = "Microsoft...!"

# t1 = test()
# t2 = test()

# print(f'Name...{t1.name}')
# print(f'Name...{t2.name}')

#example -7 

# example 8 

#example - 9

# class test:
#     def __init__(self):
#         self.__amount = 5000
#         def display_amount(self):
#             return self.__amount
        
# t1 = test()
# print(t1.display_amount())

#example - 10 

# class parent:
#     def test1(self):
#         print("Parent..!")

# class child(parent):
#     def test2(self):
#         print("Child...!")

# obj = child()
# obj.test1()
# obj.test2()


#Example 11 

# class parent:
#     def test1(self):
#         print("Parent..!")

# class child(parent):
#     def test2(self):
#         print("Child...!")

# class subchild(child):
#     def test3(self):
#         print("SubChild...!")

# obj = subchild()
# obj.test1()
# obj.test2()
# obj.test3()


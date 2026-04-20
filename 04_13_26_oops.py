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

#Example -13
# multiple inheritance 

# class parent1:
#     def test(self):
#         print("parent1...")

# class parent2:
#     def test(self):
#         print("parent2...")

# class child(parent1,parent2):
#     pass

# obj = child()
# obj.test()

#Example -14

#polymorphism (behaves like many)
# 1. overriding 2. overloading

#overriding
# class parent:
#     def db_conn(self):
#         print("SQL conn soon ...!")

# class child:
#     def db_conn(self):
#         print("NOSQL conn soon...!")

# # obj = child()
# # obj.db_conn()

# obj = parent()
# obj.db_conn()

# overriding is nothing but by passing pareent and getting child class
#overloading is nothing but getting the parent class

# class test:
#     def addition(self,a,b=0,c=0):
#         print(a+b+c)

# obj = test()
# obj.addition(10)
# obj.addition(10,20)
# obj.addition(10,20,30)


# args have capability to store more than 1 value 

# class test:
#     def addition(self,*args):  # if we put * it will convert to tuple
#         print(sum(args))

# obj = test()
# obj.addition(10)
# obj.addition(10,20,40,50)

# example -16 
# overloading

# class test:
#     def addition(self,num1 = None,num2 = None, num3 = None):
#         if num1 and num2 and num3:
#             print(num1+num2+num3)

#         elif num1 and num2:
#             print(num1+num2)
#         elif num1:
#             print(num1)
#         else:
#             print(0)

# obj = test()
# obj.addition(10)
# obj.addition(10,20,30)
# obj.addition()

#example - 17 

# class number:
#     def __init__(self,num1):
#         self.num1 = num1
#     def __add__(self, other):
#         return self.num1+other.num1
# n1= number(10)
# n2 = number(20)

# print(n1+n2)

#example - 18 
# dunder method 

# class test:
#     pass

# obj = test()
# print(obj)

# # passing dunder method
# class test:
#     def __str__(self):
#        return "Welcome"

# obj = test()
# print(obj)

# Example 19
#Abstract method

# from abc import ABC,abstractmethod
# class business(ABC):
#     @abstractmethod
#     def start_business(self):
#         pass

# class friend(business):
#     def start_business(self):
#             print("start AI business")
# obj = friend()
# obj.start_business()


#Example 20 
# passs self is called instance method 
# pass cls is called class method 
# pass empty is called static method 

#child calling parent using super function

# class parent:
#     def test1(self):
#         print("Hey !!")

# class child(parent):
#     def test2(self):
#         super().test1()

# obj = child()
# obj.test2()

# child class function calling parent class using constructor

# class parent:
#     def __init__ (self,param1):
#         self.param1 = param1
    
# class child(parent):
#     def __init__(self, param1,param2):
#         super().__init__(param1)
#         self.param2=param2
# obj = parent()
# print(obj.param1 + obj.param2)




import numpy as np

print (np.zeros((2,3)))




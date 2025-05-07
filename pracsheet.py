# Addition using Lambda function
# f = lambda a,b : a+b
# r = f(3,7)
# print(r)
## OR
# print((lambda a,b:a+b)(3,7))

# List Compression(to create a list in single line)
# l1 = [2*e for e in range(1, 10)]
# print(l1)
# list = [23,56,65,22,62,32,65,76,33,99]
# l2 = [e for e in list if e%2==0]
# print(l2)

#Global and Local variable
# x = 5
# def f1():
#     global x
#     x = 15
#     y = 10
#     print("x=%d y=%d"%(x,y))
# f1()
# print(x)

#Global functions
# x = 5
# def fun():
#     x = 10
#     d = globals()
#     print( "local x=%d global x=%d"%(x,d['x']))
# fun()

#type conversion
# x = int('123')
# a = float('123.42')
# b = complex('3+4j')
# c = str(12)
# d = bool('True')
# e = bin(25)
# f = oct(25)
# g = hex(25)
# h = ord('A')
# i = chr(98)
# print(x,a,b,c,d,e,f,g,h,i,sep="\n")

#What is python decor?
# def welcome(fx):
#     def mfx(*t,**d):
#         print(*t,**d)
#         fx(*t,**d)
#         print("Thanks for using the function")
#     return mfx
# @welcome
# def hello():
#     print("Hello !")
# @welcome
# def add(a,b):
#     print(a+b)
# hello()
# add(1,3)

#What are iterators in python
# x = [23,65,22,76,34,98,43]
# it = iter(x)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

#SORTED
# t1 = (34, 64, 32, 78, 88, 83, 95, 64)
# s_t1 = sorted(t1)
# print(s_t1)
# type(s_t1)
# print(type(t1))

#SORT
# l1 = [34, 64, 32, 78, 88, 83, 95, 64]
# l1.sort()
# print(type(l1))
# print(l1)

#What is init method in python
# class test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
# t1 = test()
# print(t1.a, t1.b)

#Accept a number user check whether it is prime or not
# num=int(input("enter number"))
# for i in range(2,num):
#     if num%i==0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")

#Write a program to print the following pattern
# *
# **
# ***
# ****
# *****
# s = int(input("Enter a number"))
# for i in range(1,s+1):
#     print("* "*i)
#     i+=1

#Write a program to create pyramid
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#Find the factors of numbers
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

#Find if the number ia an abudant number or deficient.
# here the sum of factors of the number is greater
# than the number itself?
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum>n:
#     print("Abundant number")
# else:
#     print("Deficient number")

#Geometric series-Every term is derived by multiplying
# previous term by a fixed number?
# N=int(input("Enter N: "))
# sum=0
# a=2
# for i in range(1,N+1):
#     sum=sum + a*2
#     a=a*2
# print("sum of series: ",sum)g
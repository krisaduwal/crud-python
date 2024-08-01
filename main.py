# print ("hello world")
# x = 1
# if x == 1:
#     print("x is 1.")

# age = 22
# print (age)
# float = 7.0
# print(float)
# myfloat = float(7)
# print(myfloat)
# mymy = "hehehehehe"
# print(mymy)
# one = 1
# two = 2
# three = one + two
# print(three)

# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)
# n1, n2 = 3, 4
# print(n1, n2)

# mystring = "hello"
# myfloat = 10.0
# myint = 20

# if mystring == "hello":
#     print("string: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("float: %f" % myfloat)

# if isinstance(myint, int) and myint == 20:
#     print("integer: %d" % myint)
# mylist = []
# mylist.append(2)
# mylist.append(9)
# mylist.append(4)
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])

# for x in mylist:
#     print(x)
# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# strings = []
# strings.append("hello")
# strings.append("world")

# names = ["John", "eric", "jessica"]

# second_name = names[1]
# print(second_name)
# print(numbers)
# print(strings)
# print("the second name on the name list is %s" % second_name)
# number = 1 + 2 * 3 / 4.0
# print(number)
# remainder = 11 % 3
# print(remainder)
# squared = 7 ** 2
# cubed = 2 ** 3
# print(squared)
# print(cubed)

# helloworld = "hello" + " " + "world"
# print(helloworld)
# lotsofhellos = "hello" * 10
# print(lotsofhellos)
# even_num = [2, 4, 6, 8]
# odd_num = [1, 3, 5, 7]
# all_num = odd_num + even_num
# print(all_num)
# print([1, 2, 3] * 3)

# x = object()
# y = object()

# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list

# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))

# name = "krisa"
# age = 22
# print("helllo, %s is %d years old" % (name, age))

# mylist = [1, 2, 3]
# print(" a list: %s " % mylist)

# data = ("john", "doe", 53.44)
# format_string = "hello %s %s. Your current balance is %s"
# print(format_string % data)

# astring = "hello world!"
# print("single quotes are ''")
# print(len(astring))
# print(astring.upper())
# print(astring.startswith("hello"))
# print(astring.endswith("asdfdfsd"))
# afewwords = astring.split(" ")

# s = "hey there! what should this string be?"
# print("length of s = %d" % len(s))

# print("the first occurence of the letter a = %d" % s.index("a"))

# print("a occurs %d times" %s .count("a"))

# print("the first five characters are '%s'" % s[:5])

# print("the thirteenth character is '%s'" %s[12])

# print("the characters with odd index are '%s'" %s[1::2])

# print("the last five characters are '%s'" % s[-5:])
# name = "krisa"
# age = 22

# if name in ["krisa", "john"]:
#     print("ypur name is either krisa or john")
# statement = False
# another_statement = False
# if statement is True:
    # print("it is tru")
    # pass
# elif another_statement is True:
    # print("another true")
    # pass
# else:
    # print("arkooo")
    # pass
# number = 100
# second_number = 10
# first_array = [1, 3]
# second_array = [1, 2]

# if number > 15:
#     print("1")
# if first_array:
#     print("2")
# if len(second_array) == 2:
#     print("3")
# if len(first_array) + len(second_array) == 4:
#     print("4")
# if first_array and first_array[0] == 1:
#     print("5")

# primes = [2, 3, 5, 7]
# for prime in primes:
#     print(prime)
# for x in range(5):
#     print(x)

# for x in range(3, 6):
#     print(x)

# for x in range(3, 8, 3):
#     print(x)

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
# for x in range(10):
#     if x % 2 == 0:
#         continue
#     print(x)

# count = 0
# while(count < 5):
#     print(count)
#     count +=1
# else:
#     print("count value reached %d" %(count))

# for i in range(1, 10):
#     if(i%5 == 0):
#         break
#     print(i)
# else:
#     print("not printed")
# def my_function():
#     print("hello function")
# my_function()
# def my_function(username, age):
#     print("hello, %s you are %d years old" %(username, age))
# my_function('krisa', 22)
# def sum(a, b):
#     s= a + b
#     print(s)
# sum(10, 4)
# def list_benefits():
#     return []

# def build_sentence(benefit):
#     return ""

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#     name_the_benefits_of_functions()


# def my_function(country = "norway"):
#     print("i am from " + country)

# my_function()
# my_function("nepal")

# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def my_function(x):
#     return 5 * x
# print(my_function(4)) 
# print(my_function(6))
# print(my_function(5))
# print(my_function(9))

# class MyClass:
#     variable = "bleh"

#     def function(self):
#         print("msg inside class")

# object = MyClass()
# object.function()
# # object.variable
# print(object.variable)
# object.variable = "yuck"
# print(object.variable)

# class Person:
#     def __init__(mee, name, age):
#         mee.name = name
#         mee.age = age

    # def __str__(self):
    #     return f"{self.name}({self.age})"
    # def myfunc(self):
    #     print("hello my name is " + self.name)

# p1 = Person("krisa", 22)

# print(p1.n)
# print(p1.age)
# p1.myfunc()
# p1.myfunc()
# p1.age = 50
# del p1.age
# print(p1.age)

# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.year = 2024
        # mee.name = name
        # mee.age = age
    # pass
    # def myinfo(self):
        # print("hello I'm " + self.name)

# obj = Student("manika", 23)
# print(obj.year)


# from draw import *

# def play_game():
#     print("play game")
# def main():
#     result = play_game()
#     draw_game(result)

# # if __name__ == '__main__':
# #     main()


# main()
# from mymodule import person1
# import platform

# x = dir(platform)
# print(x)
# print(person1["age"])
# a = mymodule.person1["age"]
# print(a)
# mymodule.greeting("krisa")
import json

x = '{"name": "krisa", "age": 22, "city": "new york"}'





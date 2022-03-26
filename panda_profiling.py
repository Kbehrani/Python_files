#  print("hello")

# import pandas as pd
# print(pd.__version__)
# df=pd.read_csv('~/Documents/Python_files/test_file.csv')
# df=pd.read_csv('~/Documents/Python_files/test_file1.csv')
# print(df)

# x = 5
# y = "John"
# print(x)
# print(y)

# import pandas as pd 
# from pandas_profiling import ProfileReport
# data=pd.read_csv('~/Documents/Python_files/Clean_Dataset.csv')
# print(data)
# print(data.head())
# data.info()
# data.describe()
# data.isnull()
# profile=ProfileReport(data,title="Airline data", html={'style': {'full_width': True}})
# profile
# profile.to_file("Airline analysis.html")
# print("feeling excited - wow! I nailed it, let's do something new")

# name=input("enter name:")
# print(name)

# number=input("enter number: ")
# number=int(number)
# print(type(number))

# number=int(input("enter number: "))
# number=float(input("enter number: "))
# print(type(number))


# print(type(number))

# number1=5
# print(type(number1))
# number2=5.5
# print(type(number2))

#assignment operators
# x=5
# results =x//2
# print(results)
# #concatenate two strings
# str1="Hey "
# str2="Jude"
# print(str1+str2)
# x,y=5,6

#problem solving

# distance_km=564.5
# distance_miles=0.62137*distance_km
# print(distance_miles)

# number=15
# print(number<10)

# score=int(input("Enter your score:"))
# if score>50:
#     print("You have passed your Exam")
#     print("Congratulations")

# if score<50:
#     print("Sorry you have failed your exam")

# if score>50:
#     print("You have passed your Exam")
#     print("Congratulations")
# else:
#     print("Sorry, you have failed your exam")


# while loop

# count=5

# while count<10:
#     print("Counting is interesting")
#     count=count+1

# For loop

# sequence in python is collection of things in an order
# text="Python"

# for chracter in text:
#     print(chracter)

# languages =["English", "French","German"]

# for language in languages:
#     print(language)

#python range function

# count=1

# while count<=5:
#     print(count)
#     count=count+1

# easier way use range function

# for count in range (1,6):
#     print(count)

# number=int(input("Enter an integer:"))
# for count in range(1,11):
#     # product=number*count
#     # print(number,"x", count,"=", product)
#     result=count+1
#     print(result)

total=0

#looping from 1 to 100
# for number in range (1,101):
#     total=total+number
#     print(total)


# while repeats block of code until specified test condition is false
# for loop repeats the block of code until the last item in a seq is reached

#break and continue in python 

# for item in range (1,6):
#     print(item)
#     break

# when we encouter break, loop exits

# for item in range (1,6):
#     break
#     print(item)


# for item in range (1,6):
#     if item==3:
#         break
#     print(item)
# print("The end")

#while loop

# while True:
#     number=float(input("Enter a number:"))
#     if number<0:
#         break
#     print("You entered:", number)

# for i in range(1,5):
#     number=float(input("Enter a number: "))
#     if number<0:
#         continue
#     print(number)

# languages = ["Python", "Java", "Swift", "C", "C++"]

# for language in languages:
#     if language == "Swift" or language == "C++":
#         continue
#     print(language)

#pass statement - pass statement does nothing, its just a placeholder for something that you'll do in future
# counter=1
# max = 10
# if counter <= max:
#     counter += 1
# else:
#     pass

# functions - group of related statments that perform a specific task
#functions begin with keyword def

# def greet(name):
#     print("Hello",name)
#     print("How do you do", name)
# greet("Jack")#Jack is an argument
# def add_numbers (n1,n2):
#     result=n1+n2
#     print("The sum is",result)
# n1=5.4
# n2=6.1

# add_numbers(n1,n2)

# when we encouter return the programme is terminated 
#built in functions

marks=[55,64,56,78]
length=len(marks)
print("Length is", length)
marks_sum=sum(marks)
print("The total marks is", marks_sum)

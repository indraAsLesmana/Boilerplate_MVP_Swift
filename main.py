# import keyword
#
# name = "indra"
# age = 20
# numbers = []
# pi = 3.14
# isAdult = True
# brand: str = "Amigoscode"
# isAdult: bool = False
#
#
# def hello() -> str:
#     return "hello"
#
#
# print(type(name))
# print(type(age))
# print(type(numbers))
# print(type(pi))
# print(brand.replace('A','a'))
# print(len(brand))
# print("code" not in brand)
#
# comment = f"""
# indra agus lesmana
# agus lesmana
# lesmana {"yesa nala"}
# """
#
# print(comment)
#
# # Reserved keyword
# print(keyword.kwlist)
#
# print((3 > 2) and (4 > 3))
import datetime

# number = 10
# if not(number > 0):
#     print(f"{number} is positive")
# elif number == 0:
#     print(f"{number}")
# else:
#     print(f"{number} is negative")

# print(not (0 > number))

# lattersA = {"A", "B", "C", "D"}
# lattersB = {"E", "A", "B", "H"}
#
# myList = list(lattersA | lattersB)
# myList.sort()
#
# differences = lattersB - lattersA
# print(differences)

# numbers = [1, 3, 5, 6, 7, 9]
# result = 0
# for number in numbers:
#     result += number
#
# print(result)

# def great(name: str = "Yesa", age: int = 13):
#     print(f"""Hello how are you {name}?
# my name {name} im {age} years old
# """)
#
#
# great()


# def is_adult(age: int) -> str:
#     return "adult" if age >= 16 else "not yet"
#
#
# print(f"im {is_adult(15)}")


# class Phone:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def call(self, phoneNumber):
#         print(f"{self.brand} we are on the call {phoneNumber}")
#
#     def __str__(self) -> str:
#         return f"Brand {self.brand}\nprice {self.price}"
#
#
# iphone = Phone("iphone", 400)
#
# print(iphone)
from datetime import datetime
from datetime import date

print(datetime.now())
print(date.today())
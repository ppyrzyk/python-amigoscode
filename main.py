
# print("Hello to python")

# name = "Jamila"
# age: int = 20
# print(age)

# name, age = "Pawel", 20
#
# print(name, age)

# name = "James"
# fullName = " J James"
# PI = 3.14 # Uppercase name for variables tht do not change
# print(PI)

# brand = "AmigosCode"
# age = 20
# numbers = []
# isAdult = False
# print(type(brand))
# print(type(age))
# print(type(numbers))
# print(type(isAdult))

# brand: str = "AmigosCode" # you can specify what type it is but it isnt necessary
# isAdult: bool = False
# def hello() -> int: # specyfying what does methpd return but its isnt necessary
#     return 1

""" long comment can
be written between
3 double quotes
on each side
"""
import keyword

# brand = "Amigoscode"
#
# print("code" in brand) #return boolean true  or false
# print("code" not in brand)

# comment = """ you can write a long
# variable and
# it prints out in the same
# paragraphs """
#
# print(comment)
#
# name = "Pawel"
# age = 35
# email = f"""
# Hello {name},
# I know yor are {age} years old
# Best Regards {name.upper()} """
#
# print(email)

# # resrved keywords
# print(keyword.kwlist)

# print(1+2)
# print(10 - 3)
# print(3*3)
# print(3/3)
# print(3**2)
# print(10 % 6)

# print(10 > 5)
# print(10 >= 5)
# print(10 < 5)
# print(10 <= 5)
# print(10 != 5)
# print(10 == 10)

# print((10 > 5) and (1 > 3)) # both expressions need to be true to return 'TRUE'
#
# print(10 > 5 or 1 > 3 or "A" == "c") # at least one expression need to be right to return true
#
# print(not ("A" == "c")) #returns true because these expressions are not equal to each other

# brand = "AA"
# brand = "nike"
#
# print(brand) # it prints out the latter assignment of the variable

# number = 4
# number += 1 #number = number + 1
# number -= 1 #number = number - 1
# number *= 2 #number = number * 2
# number /= 2 #number = number /2
# number **= 2 #number = number^2
# print(number)

# number = -7
#
# if number > 0:
#     print(f"Number {number} is positive")
# elif number == 0:
#     print(f"Number {number} is zero")
# else:
#     print(f"Number {number} is negative")

# number = 10 # to be used ehen there are only 2 possibilities
# message = "positive" if number > 0 else "0 or negative"
# print(message)

# numbers = [1, 2, 3, 4, -1, -20, ["A", "B"]]
# print(numbers[0]) # printing number at specified index within [] from the list

# numbers = [1, 2, 3, 4, -1, -20, ["A", "B"]]
# print(numbers[6][1]) # at index 6 there is another list within the list
# #and at index 0 is the first sign of the list within a list

# numbers = [1, 2, 3, 4, -1, -20]
# numbers.sort()
# numbers.reverse()
# numbers.clear()
# numbers.append(10) # adding a number to a list
# print(len(numbers))  # prints out the ;ength of the list - jow many elements
# print ( 5 in numbers) # checks if the element is in the list
# print( 5 not in numbers)
# print(numbers)
# numbers.remove(3)
# numbers.pop() #removes last element from the list
# del numbers[0] #deleting element from the numbers list at specific index
# del numbers[0:2] # deleting elements within the specified range
# print(numbers)

#
# numbersList = [1, 1, 2, 3, 4, 5, 6] #order is guaranteed
# numbersSet = {1, 1, 2, 3, 4, 5, 6} # within set does not allow duplicates
# letterSet = { "A", "A", "B", "C", "D"} # within set duplicates are
# # not allowed (will only print out an instance of duplicates once)
# # and the order is random
# print(numbersList)
# print(numbersSet)
# print(letterSet)

# lettersA = {"A", "B", "C", "D"}
# lettersB = {"E", "F", "B", "A"}
# union = lettersA | lettersB #merges both sets
# intersection = lettersA & lettersB #finds the common element in both sets
# difference = lettersA - lettersB #shows the elements tht are in set A but not in set B
# print(f"Union {union}")
# print(f"Intersection {intersection}")
# print(f"Difference= {difference}")

# Dictionaries
# person = {
#     "name": "Jamal",
#     "age": 20,
#     "address": "USA"
# }
# print(person["name"])
# print(person.keys())
# print(person.values())
# # person.clear()
# person["age"] = 100
# person["name"] = "Pawel"
# print(person)

# Loops
# names = ["Ahmed", "Anna", "James"]
# for loop
# for name in names:
#     print(name)

# person = {
#     "name": "Jamal",
#     "age": 20,
#     "address": "USA"
# }
# for key in person:
#     print(f"key: {key} value: {person[key]} ")
#
# for key, value in person.items():
#     print(f"key: {key} value:{value}")

sum = 0
numbers = [1, 3, 5, 6, 7, 9]

for number in numbers:
    sum += number
print(sum)
average_numbers = sum/len(numbers)
print(round(average_numbers,2))



# import calculator
#
# print(calculator.add(2,2))

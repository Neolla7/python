"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
"""
# name = input("Please, enter your name: ")
# age = input("please, enter your age: ")
# if age.isdigit():
#     age = int(age)
# else:
#     print("Wrong value")
#     exit()

# print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")

# print(len(name))

# """
# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'phonebook'
# Expected Result : 'mymy'
# Sample String: 'x'
# Expected Result: Empty String
# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters
# """
# input_string = input("Enter some string: ")
# if len(input_string) < 2:
#     print("")
# else:
#     new_string = input_string[:2] + input_string[-2:]
#     print(new_string)

"""
The valid phone number program.
Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is 
only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
"""
# input_number = input("Enter a valid phone number: ")

# if input_number.isdigit() and len(input_number) == 10:
#    print("success")
# else:
#    print("wrong value")

"""
The math quiz program.
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
"""
# math_exp = "2 + 3"
# math_res = 5
# msg = input(f"How much will be if {math_exp}: ")

# if msg.isdigit():
#     msg = int(msg)
# else:
#     print("wrong input")
#     exit()

# if msg == math_res:
#     print("correct")
# else:
#     print("think harder")

""" 
The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""
name = "iryna"
input_name = input("Enter a name: ")

print(input_name.lower() == name)

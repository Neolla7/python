# user_input = int(input("Enter some number: "))
# user_msg = input("Enter some message: ")

# for i in range(user_input):
#     print(user_msg, i)

# for letter in user_msg:
#     print(letter)

# count = 0

# while count < user_input:
#     print(user_msg, count)
#     count += 1

# index = 0
# while index < len(user_msg):
#     print(user_msg[index])
#     index += 1

# n = 5

# for i in range(n):
#     print(i)

# for i in range(n):
#     print(i + n)

# for i in range(n):
#     print("Ira")

# for i in ["123", 2, 3]:
#     print(i)


number = int(input("enter a number: "))
stars = 1
spaces = number - stars
for i in range(number):
    print(" " * spaces, "*" * stars, sep="")
    stars += 2
    spaces -= 1 


#     *  
#    ***
#   *****
#  *******
# *********


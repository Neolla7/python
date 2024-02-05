# my_string = input("Enter some text: ")

# l = len(my_string)
# print(l)
# print(my_string)
# print(my_string[l - 1])
# print(my_string[-1])

string_2 = "i LoVE dogs"

print(string_2.capitalize())

print(string_2.count("o"))

print(string_2.center(25, "*"))

print(string_2.endswith("dogs "))

print(string_2.upper())

print(string_2.lower())

print(string_2.title())

words = string_2.split()
print(words)

print("-".join(words))

print(string_2.strip("*"))

print(string_2.isnumeric())

print(string_2.isalpha())

print(string_2.find("VE"))
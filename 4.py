""" дано два числа 10 и 2, а также стринга, которая содержит имя и фамилию.
необходимо:
1. вывести в консоль только имя если 1е число больше второго, но меньше 5
2. вывести фамилию и имя (в такой последовательности) если сумма 2х чисел меньше 15
3. заменить имя на любое другое и вывести имя и фамилию если 1е число больше 20 или 1-е число больше 2-го
это все в одной программе"""

number1 = 10
number2 = 2
full_name = "Iryna Shushemoina"

# if 5 > number1 > number2:
#     print(full_name[:5])

# if number1 + number2 < 15:
#         print(full_name[6:], full_name[:5])

# if  number2 < number1 or number1 > number2:
#         full_name = "Ira Shushemoina"
#         print(full_name)

# number = input("Please, enter a value: ")
# print(number * 5)
# print(type(number))

# number = int(number)
# number += 5
# print(number)
# print(type(number))

# number = str(number)
# print(number * 5)
# print(type(number))

# number = float(number)
# print(number * 5)
# print(type(number))

a = 10
b = 2
c = a / 2
d = 9 // 2
e = 9 % 2
print(c, type(c))
print(d, type(d))
print(e, type(e))

print(type(c) is int)
print(type(c) is float)

print("0" > "?")
print("0" < "?")
print(ord("0"))
print(ord("?"))

if "Swan " > "Swan":
    print("swan")
else:
    print("Swan")
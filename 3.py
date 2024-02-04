full_name = "Iryna Shushemoina"
first_name = full_name[:5]
last_name = full_name[6:]
print(full_name, first_name, last_name, sep="\n")

first_name_1 = "Vova"
last_name_1 = "Dukhanin" 
full_name_1 = first_name_1 + " " + last_name_1
print((full_name_1 + " ") * 3)
first_name_x3 = first_name * 3 
print(first_name_x3)
addition = 2 + 3 
substraction = 2 - 3
multiplication = 2 * 3
dividing = 2 / 3
div_int = 2 // 3
modulus = 2 % 3
power = 2 ** 3
print(addition, substraction, multiplication, dividing, div_int, modulus, power, sep="\n")
a = 9
b = 5
result = a > b
print(result)
print(a < b)
print(a == b)
print(a >= b)
print(a != b)
b = 9
print()
result = a > b
print(result)
print(a < b)
print(a == b)
print(a >= b)
print(a != b)
print(type(a))
print(type(result))
print(type(first_name))
print(type(dividing))

a = 10
b = 5

if not a < b:
    print("inside if")

    if a == 10:
        print("a = 10")
        
    elif a > 1:
        print("a > 1")
    elif a == 5:
        print("a = 5")
    else:
        print("else")
        

print("after if")

print(first_name is not "Iryna")
print(a is 10)
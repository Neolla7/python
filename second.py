string = "text"
print("string:", string, sep=" ")
integer_ = 31
print("integer:", integer_, sep=" ")
float_ = 0.9 
print("float:", float_, sep=" ")
bool_ = True
print("bool:", bool_, sep=" ")
list_ = [1, 2, 3, 5, 6]
print("list:", list_, sep=" ")
one = "onest"
tuple_ = (1,2,4, one)
print("tuple:", tuple_,)
dict_ = {"pass": "qwerty", "log": 12345}
print("dict:", dict_)
set_ = {1, 3, 5, 7}
print("set:", set_)
none = None
print("none:", none)
all_data_types = [string, integer_, float_, bool_, list_, tuple_, dict_, set_, none]
print(all_data_types)
alphabet = "abcdefghijklmnopqrstuvwxyz" 
print(alphabet[8], alphabet[14], sep="")
print(alphabet[:3])
print(alphabet[10::-1])
print(alphabet[::-1])
print(id(list_))
list_[4] = 10

print(id(list_))
list_ = [1, 2, 3, 4, 5, 10]
print(id(list_))
print(id(list_[2]))
print(id(alphabet))
print(id(alphabet[0]))
print(list_[::-1])
letter = "a"
print(id(letter))
print(id(letter[0]))
print(dict_["log"])
print()
print(all_data_types[0][1])
print(string[1])
print(alphabet[8:1:-1])
dict_["log"] = "neolla"
print(dict_)

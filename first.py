string = "text"
integer = 9
integer2 = integer
float_ = 0.003303
bool_ = True
bool_ = False
list_ = [1, 0.9, 1, 1]
tuple_ = ('two', 2, "2", 1.9)
dict_ = {'one': 1, 'two': 2, }
set_ = {1, 2, 3, "four", 1}
none = None


print(string, "\n", integer, "\n", float_, "\n", bool_, "\n", list_, "\n", tuple_, "\n", dict_, "\n", set_, "\n", none, sep="")
print(dict_["one"])
print(string, integer, float_, bool_, list_, tuple_, dict_, set_, none, sep="\n")
print(string[1:3], end=" ")
print(list_[3:])

suma = sum(list_)
print(suma) 
rez= print(set_)
print(rez)
print("string=",string, sep="")
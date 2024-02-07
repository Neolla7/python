data = [1, 10, 3, 14]
data.append(5)
print(len(data))
print(data)

data_2 = data
print(id(data), id(data_2))

data3 = [1, 2, 3]
print(data_2.append("word"))
print(data_2)

res = print(data.count(3))
print(res)

data.extend("word")
print(data)

print(data.index(5))

data.insert(0, -10)
print(data)

print(data.pop())
print(data)

print(data.pop())
print(data)

data.remove("word")
print(data)

data.reverse()
print(data)

# data_r = reversed(data)
# print(data, list(data_r))

data[0] = 12
print(data)

data[1] = data[1] + "er"
print(data)

print(data.pop(1))
print(data)


data.sort()
print(data)

index = 0 
while index < len(data):
    data[index] = str(data[index])
    index = index + 1
    print(index)

print(data)

# for element in data:
#     print(element)

for index in range(7):
    data[index] = int(data[index])
    print(index)

print(data)

word1 = "abcdefghijklmnopqrstuvwxyz"

for letter in word1:
    print(letter)

print(letter)

# word = "Mike"
# word_2 = word
# word = word.upper()

# print(word_2)
# print(word)


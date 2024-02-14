# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_[::2] = [10, 20, 30, 40, 50]
# print(list_)

# msg = "abc"
# msg_1 = msg.rjust(7)
# print(msg_1)

msg = "Zoe like to play all day"

# for letter in msg:
#     print(letter.upper())

# index = 0

# while index < len(msg):
#     print(msg[index].upper())
#     index += 1

# for index in range(len(msg)):
#     print(msg[index].upper())

# for i in range(3, 9, 2):
#     print(i)

# for i in range(10):
#     print(msg)

# try_ = 1
# while try_ <= 10:
#     print(msg)
#     try_ += 1

# try_1 = 10

# while try_1:
#     print(try_1)
#     try_1 -= 1


# for word in msg.split():
#     print(word)
#     for letter in word:
#         print(letter)

index = 0 
list_ = msg.split()

while index < len(list_):
    print(list_[index])
    word = list_[index]
    index += 1

    index_1 = 0
    while index_1 < len(word):
        print(word[index_1])
        index_1 += 1
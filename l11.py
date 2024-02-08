sentence = "big brown fox is jumping over the fence"
print(sentence)
# word = input("choose the word you want to change: ")
# new_word = input("and to which: ")



# # start_index = a.find(b)
# # end_index = start_index + len(b)
# # print(a[start_index:end_index])

# a_list = sentence.split()
# # print(a_list)
# a_index = a_list.index(word)
# # print(a_list[a_index])
# a_list[a_index] = new_word
# sentence = " ".join(a_list)
# print(sentence)

list_letters = []

for letter in sentence:
    list_letters.append(letter)

print(list_letters)

list_2 = []
i = 0

while i < len(sentence):
    letter = sentence[i]
    i += 1
    list_2.append(letter)

print(list_2)

for a in list_2:
    print(a)
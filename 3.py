import string

stri = str(input("Введіть текст:\n"))
words = stri.split()
unique = []

for word in words:
    if word[len(word)-1] in string.punctuation:
        word = word[:-1]
    if word[0] in string.punctuation:
        word = word[1:]
    if word not in unique:
        unique.append(word)

print("Унікальні слова:")

for word in unique:
    print(word)
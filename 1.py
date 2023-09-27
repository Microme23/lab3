string = str(input("Введіть текст: \n"))
while (len(string) < 3):
    string = str(input("Введіть текст: \n"))
print("Останні 3 символи рядку:", string[len(string)-3:len(string)])
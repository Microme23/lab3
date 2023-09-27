string = str(input("Введіть текст:\n"))
kil = 0
for i in range (0,len(string)):
    if string[i]== "_":
        kil += 1
if kil == 0:
    print("Символа '_' немає")
else:
    print("Кількість знаків '_':", kil)
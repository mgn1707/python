my_words = input("Введите различные слова через пробел: ").split()
for i in range(len(my_words)):
    print(f"{i+1}: {my_words[i][:10]}")
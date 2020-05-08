def int_func(spl_words):
    #spl_words = words.split()
    upper_words_list = []
    for i in range(len(spl_words)):
        for j in spl_words[i]:
            if ord(j) >= 97 and ord(j) <= 122:
                continue
            else:
                print("Yo should enter the words in Latin alphabet")
                spl_words[i] = 'Error'
                '''Если пользователь введет не латиницей, то вместо введенного слова в списке появится Error'''
                break
        upper_words = spl_words[i].title()
        upper_words_list.append(upper_words)
    return upper_words_list
print(int_func(input("Enter any word ").split()))
with open("lesson5_task2.txt", "r") as second_file:
    print(f"\nСодержимое файла:\n")
    for line in second_file:
        print(line, end="")

    second_file.seek(0)
    content = second_file.readlines()
    line_qnt = len(content)
    print(f"\n\nФайл содержит {line_qnt} строк\n")

    second_file.seek(0)
    i = 0
    for line in second_file:
        i += 1
        words_qnt = len(line.split())
        print(f"В {i}-й строке {words_qnt} слов")

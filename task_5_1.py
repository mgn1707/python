file_text = open("first_task.txt", "w")
line = True
while line == True:
    line = input("Enter some information you want to write to file: \n")
    if line == '':
        break
    file_text.write(line)
file_text.close()
file_text = open("first_task.txt", "r")
content = file_text.readlines()
print(content)
file_text.close()

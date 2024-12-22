info = ''
while info != "stop":
    info = input("Введите информацию, вводимую в файл: ")
    if info != 'stop':
        with open("user_input.txt", "a+") as file:
            file.write(info + "\n")
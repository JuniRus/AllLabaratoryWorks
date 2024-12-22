def print_file(filename, mode):
    try:
        with open(filename, 'r') as file:
            if mode == 0:
                print("Чтение всего файла.")
                print(file.read())
            else:
                print("Построчное чтение файла.")
                for line in file:
                    print(line, end='')
    except FileNotFoundError:
        print("Файл " + filename + " не существует!")


print_file("example.txt", 0)
print()
print_file("text.txt", 2)

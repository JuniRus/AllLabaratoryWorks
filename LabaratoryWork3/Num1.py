def print_file(filename, mode):
    with open(filename, 'r') as file:
        if mode == 0:
            print("Чтение всего файла.")
            print(file.read())
        else:
            print("Построчное чтение файла.")
            for line in file:
                print(line, end='')


print_file("example.txt", 0)
print()
print_file("example.txt", 2)
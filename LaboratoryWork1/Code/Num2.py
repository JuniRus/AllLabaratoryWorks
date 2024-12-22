num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Большее число:", end=' ')
if(num1 > num2):
    print(num1)
elif(num1 <= num2):
    print(num2)

first = float(input("Введите первое число: "))
second = float(input("Введите второе число число: "))

operation = input("Что сделать(+, -, :, *): ")
result = 0

if operation == "-":
    result = first - second
elif operation == "+":
    result = first + second
elif operation == "*":
    result = first * second
elif operation == ":":
    result = first / second


print(f"Результат: {result}")
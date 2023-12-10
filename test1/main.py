import numexpr

expr = input("Введіть приклад: ")
result = numexpr.evaluate(expr)

print(f"Результат: {result}")
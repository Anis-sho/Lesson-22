while True:
    s = input("Введите знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print(a + b)
        elif s == '-':
            print(a - b)
        elif s == '*':
            print(a * b)
        elif s == '/':
            if b != 0:
                print((a / b))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

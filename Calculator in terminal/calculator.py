
num = 0
operation = None
reset = True
result = None
calcOpertaions = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbę startową:"))
        reset = False

    operation = input("Podaj operację arytmetyczną jak np. " +
                      str(calcOpertaions) + " lub exit jeśli koniec lub reset:")
    if operation == "exit":
        break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOpertaions:
        print("Wprowadzona została błędna operacja.")
        continue

    secondNum = int(input("Podaj drugą liczbę:"))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print("Wynik operacji " + str(num) + " " + operation +
          " " + str(secondNum) + " = " + str(result))

    num = result
    result = None

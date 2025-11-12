def calculadora(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

print("=== Calculadora Simples ===")

    n1 = float(input("Digite o primeiro número: "))

    n2 = float(input("Digite o segundo número: "))

    op = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(n1, n2, op)

print("Resultado:", resultado)

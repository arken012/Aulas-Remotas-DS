
nome = input("Qual é o seu nome? ")

idade_texto = input("Qual é a sua idade? ")

idade = int(idade_texto)

    if idade >= 18:
        print(f"Olá, {nome}, você é maior de idade.")
    else:
        print(f"Olá, {nome}, você é menor de idade.")
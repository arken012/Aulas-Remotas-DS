class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")

print("=== Cadastro de Carro ===")

    marca = input("Digite a marca do carro: ")

    modelo = input("Digite o modelo do carro: ")

    portas = input("Digite o número de portas: ")

    meu_carro = Carro(marca, modelo, portas)

print("\n--- Informações do Carro ---")

    meu_carro.exibir_info()
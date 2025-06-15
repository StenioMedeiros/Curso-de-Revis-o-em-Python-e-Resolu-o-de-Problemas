# ---------------------------
# Herança e Especialização em Classes
# ---------------------------

# ---------------------------
# Classe Base (Superclasse)
# ---------------------------
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("🔧 Ligando o motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: " + \
               f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# ---------------------------
# Classes Derivadas (Subclasses)
# ---------------------------

# Motocicleta herda de Veiculo, mas não altera nenhum comportamento
class Motocicleta(Veiculo):
    pass

# Carro herda de Veiculo, também sem alterações por enquanto
class Carro(Veiculo):
    pass

# Caminhao herda de Veiculo, mas adiciona novo atributo e método
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # chama o construtor da superclasse
        self.carregado = carregado  # novo atributo específico de Caminhao

    def esta_carregado(self):
        print(f"O caminhão está carregado? {' Sim' if self.carregado else '❌ Não'}")


# ---------------------------
# Instanciando os Objetos
# ---------------------------

print("\n🚀 Criando os veículos...\n")

moto = Motocicleta("preta", "ABC-1234", 2)
carro = Carro("branco", "XDE-0098", 4)
caminhao = Caminhao("roxo", "GFD-8712", 8, True)

# ---------------------------
# Exibindo os Objetos com __str__
# ---------------------------

print("Detalhes da Motocicleta:")
print(moto)

print("\nDetalhes do Carro:")
print(carro)

print("\nDetalhes do Caminhão:")
print(caminhao)

# ---------------------------
# Testando Método Especializado da Subclasse
# ---------------------------

print("\nVerificando se o caminhão está carregado:")
caminhao.esta_carregado()

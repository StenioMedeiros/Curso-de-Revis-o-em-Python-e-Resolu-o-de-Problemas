# ---------------------------
# Conceitos de Classes e Objetos
# ---------------------------

class Bicicleta:
    # ---------------------------
    # Método Construtor (__init__)
    # ---------------------------
    # O método __init__ é chamado automaticamente quando uma nova instância (objeto) é criada.
    # Aqui definimos os atributos da bicicleta.
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # ---------------------------
    # Métodos da Classe
    # ---------------------------

    def buzinar(self):
        print(f"[{self.modelo.upper()}] Plim plim... 🚲🔔")

    def parar(self):
        print(f"[{self.modelo.upper()}] Parando bicicleta... ⛔")
        print(f"[{self.modelo.upper()}] Bicicleta parada! ✅")

    def correr(self):
        print(f"[{self.modelo.upper()}] Vrummmmm... 🏁")

    # ---------------------------
    # Representação do Objeto (__str__)
    # ---------------------------
    # Este método define como o objeto será impresso quando usarmos `print(objeto)`
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# ---------------------------
# Instanciando Objetos (Criando Bicicletas)
# ---------------------------

print("\n🔧 Criando bicicleta vermelha...\n")
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# ---------------------------
# Chamando Métodos do Objeto
# ---------------------------

print("\n🚴 Interações com b1 (Caloi):\n")
b1.buzinar()
b1.correr()
b1.parar()

# ---------------------------
# Acessando Atributos Individualmente
# ---------------------------

print("\n📋 Detalhes da bicicleta b1 (acesso direto aos atributos):")
print(f"Cor: {b1.cor}")
print(f"Modelo: {b1.modelo}")
print(f"Ano: {b1.ano}")
print(f"Valor: R$ {b1.valor:.2f}")

# ---------------------------
# Criando Nova Bicicleta
# ---------------------------

print("\n🔧 Criando bicicleta verde...\n")
b2 = Bicicleta("verde", "monark", 2000, 189)

# ---------------------------
# Exibindo o Objeto com __str__
# ---------------------------

print("\n📦 Representação da bicicleta b2:")
print(b2)

# ---------------------------
# Chamando Método em b2
# ---------------------------

print("\n🚴 Interações com b2 (Monark):")
b2.correr()
b2.buzinar()
b2.parar()
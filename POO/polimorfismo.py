# -----------------------------------
# Polimorfismo e Herança em Python
# -----------------------------------

class Passaro:
    def voar(self):
        print("Voando... (comportamento genérico de um pássaro)")

# -------------------------
# Classes filhas (especializações)
# -------------------------

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar (correção necessária: deveria herdar de outra classe)")

# -------------------------------------------
# Exemplo ruim: Avião não é pássaro, mas herda Passaro
# -------------------------------------------

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando... (exemplo ruim de herança)")

# -------------------------------------------
# Função que usa polimorfismo para chamar método 'voar'
# -------------------------------------------

def plano_voo(obj):
    obj.voar()

# -------------------------------------------
# Testando o polimorfismo
# -------------------------------------------

plano_voo(Pardal())    # Pardal pode voar
plano_voo(Avestruz())  # Avestruz não pode voar
plano_voo(Aviao())     # Avião está decolando

# -------------------------------------------
# Comentário:
# Avião não é um pássaro e não deveria herdar Passaro.
# Ideal criar uma interface ou classe base "Voador"
# para compartilhar método voar entre pássaros e aviões.

# -------------------------------
# Herança Simples e Múltipla em Python
# -------------------------------

# -------------------------------
# Classe Base
# -------------------------------
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: " + \
               f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# -------------------------------
# Subclasse Mamífero
# -------------------------------
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)  # Passa argumentos restantes para a superclasse


# -------------------------------
# Subclasse Ave
# -------------------------------
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


# -------------------------------
# Gato: uma especialização de Mamífero
# -------------------------------
class Gato(Mamifero):
    pass  # Usa os métodos e atributos herdados de Mamifero e Animal


# -------------------------------
# Ornitorrinco: herança múltipla de Mamifero e Ave
# -------------------------------
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # A chamada de super() segue a ordem do MRO (Method Resolution Order)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


# -------------------------------
# Criando Instâncias e Testando
# -------------------------------

print("\n Criando um Gato:")
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

print("\n Criando um Ornitorrinco:")
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco)

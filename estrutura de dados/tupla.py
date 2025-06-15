# ----------------------------------
# CRIAÇÃO DE TUPLAS
# ----------------------------------

# Tupla com frutas
frutas = ("laranja", "pera", "uva")
print(frutas)  # ('laranja', 'pera', 'uva')

# Tupla a partir de uma string (cada caractere vira um elemento)
letras = tuple("python")
print(letras)  # ('p', 'y', 't', 'h', 'o', 'n')

# Tupla a partir de uma lista
numeros = tuple([1, 2, 3, 4])
print(numeros)  # (1, 2, 3, 4)

# Tupla com um único elemento (vírgula obrigatória)
pais = ("Brasil",)
print(pais)  # ('Brasil',)

# ----------------------------------
# ACESSANDO ELEMENTOS
# ----------------------------------

frutas = ("maçã", "laranja", "uva", "pera")
print(frutas[0])   # maçã
print(frutas[2])   # uva

# Acesso com índice negativo (do fim para o início)
print(frutas[-1])  # pera
print(frutas[-3])  # laranja

# ----------------------------------
# TUPLAS ANINHADAS (MATRIZ)
# ----------------------------------

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])        # (1, 'a', 2)
print(matriz[0][0])     # 1
print(matriz[0][-1])    # 2
print(matriz[-1][-1])   # 'c'

# ----------------------------------
# FATIAMENTO DE TUPLAS (slicing)
# ----------------------------------

tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:])     # ('t', 'h', 'o', 'n')
print(tupla[:2])     # ('p', 'y')
print(tupla[1:3])    # ('y', 't')
print(tupla[0:3:2])  # ('p', 't')
print(tupla[::])     # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1])   # ('n', 'o', 'h', 't', 'y', 'p')  # invertida

# ----------------------------------
# PERCORRENDO TUPLAS COM for
# ----------------------------------

carros = ("gol", "celta", "palio")

# Loop simples
for carro in carros:
    print(carro)

# Loop com índice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# ----------------------------------
# MÉTODOS ÚTEIS: count() e index()
# ----------------------------------

cores = ("vermelho", "azul", "verde", "azul")

# Contagem de elementos
print(cores.count("vermelho"))  # 1
print(cores.count("azul"))      # 2
print(cores.count("verde"))     # 1

# Índice da primeira ocorrência
linguagens = ("python", "js", "c", "java", "csharp")

print(linguagens.index("java"))    # 3
print(linguagens.index("python"))  # 0

# ----------------------------------
# TAMANHO DA TUPLA
# ----------------------------------

print(len(linguagens))  # 5



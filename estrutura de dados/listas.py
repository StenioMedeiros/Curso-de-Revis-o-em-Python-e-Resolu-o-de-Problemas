# ---------------------------
# Conceitos Básicos de Listas
# ---------------------------

# Criando uma lista de frutas
frutas = ["laranja", "maca", "uva"]
print("Lista de frutas:", frutas)

# Criando uma lista vazia
frutas = []
print("Lista vazia:", frutas)

# Criando uma lista a partir de uma string
letras = list("python")
print("Lista de letras a partir da palavra 'python':", letras)

# Criando uma lista de números com range
numeros = list(range(10))
print("Lista de números de 0 a 9:", numeros)

# Lista com diferentes tipos de dados
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print("Informações sobre o carro:", carro)

# -------------------------------
# Acessando Elementos da Lista
# -------------------------------

frutas = ["maçã", "laranja", "uva", "pera"]
print("\nAcessando elementos da lista de frutas:")
print("Primeira fruta:", frutas[0])      # maçã
print("Terceira fruta:", frutas[2])      # uva
print("Última fruta:", frutas[-1])       # pera
print("Penúltima fruta:", frutas[-3])    # laranja

# -------------------------------
# Listas Aninhadas (Matrizes)
# -------------------------------

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print("\nMatriz completa:", matriz)
print("Primeira linha da matriz:", matriz[0])
print("Primeiro elemento da primeira linha:", matriz[0][0])
print("Último elemento da primeira linha:", matriz[0][-1])
print("Último elemento da última linha:", matriz[-1][-1])

# -------------------------------
# Fatiamento de Listas
# -------------------------------

lista = ["p", "y", "t", "h", "o", "n"]

print("\nFatiamento da lista:")
print("Elementos do índice 2 até o final:", lista[2:])
print("Elementos do início até o índice 1:", lista[:2])
print("Elementos do índice 1 ao 2:", lista[1:3])
print("Elementos do índice 0 ao 2, pulando de 2 em 2:", lista[0:3:2])

# -------------------------------
# Iterando Sobre Listas
# -------------------------------

print("\nIterando sobre a lista com for:")
for letra in lista:
    print(letra)

print("\nIterando com índices usando enumerate:")
for indice, letra in enumerate(lista):
    print(f"Índice {indice}: {letra}")

# -------------------------------
# Compreensões de Lista
# -------------------------------

# Filtrando números pares
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print("\nNúmeros pares na lista:", pares)

# Criando uma nova lista com o quadrado de cada número
quadrado = [numero**2 for numero in numeros]
print("Quadrado de cada número da lista:", quadrado)

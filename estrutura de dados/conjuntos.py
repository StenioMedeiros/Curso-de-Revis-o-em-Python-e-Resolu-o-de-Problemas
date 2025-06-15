# ---------------------------
# Conceitos Básicos de Conjuntos
# ---------------------------

# Conjuntos automaticamente removem elementos duplicados
numeros = set([1, 2, 3, 1, 3, 4])
print(f"Conjunto de números (sem duplicatas): {numeros}")  # {1, 2, 3, 4}

letras = set("abacaxi")
print(f"Conjunto de letras únicas: {letras}")  # {'b', 'a', 'c', 'x', 'i'}

carros = set(("palio", "gol", "celta", "palio"))
print(f"Conjunto de carros (sem repetição): {carros}")  # {'gol', 'celta', 'palio'}


# ---------------------------
# Conversão de Conjunto para Lista
# ---------------------------

numeros = {1, 2, 3, 2}
numeros = list(numeros)  # Agora podemos acessar por índice
print(f"Primeiro número da lista convertida: {numeros[0]}")


# ---------------------------
# Iterando sobre Conjuntos
# ---------------------------

carros = {"gol", "celta", "palio"}

print("\nCarros no conjunto:")
for carro in carros:
    print(f"- {carro}")

print("\nCarros com índice (usando enumerate):")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# ---------------------------
# União de Conjuntos
# ---------------------------

conjunto_a = {1, 2}
conjunto_b = {3, 4}
resultado = conjunto_a.union(conjunto_b)
print(f"\nUnião dos conjuntos A e B: {resultado}")  # {1, 2, 3, 4}


# ---------------------------
# Interseção de Conjuntos
# ---------------------------

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
resultado = conjunto_a.intersection(conjunto_b)
print(f"Interseção entre A e B: {resultado}")  # {2, 3}


# ---------------------------
# Diferença entre Conjuntos
# ---------------------------

resultado = conjunto_a.difference(conjunto_b)
print(f"Elementos em A que não estão em B: {resultado}")  # {1}

resultado = conjunto_b.difference(conjunto_a)
print(f"Elementos em B que não estão em A: {resultado}")  # {4}


# ---------------------------
# Subconjunto (issubset)
# ---------------------------

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"\nA é subconjunto de B? {conjunto_a.issubset(conjunto_b)}")  # True
print(f"B é subconjunto de A? {conjunto_b.issubset(conjunto_a)}")  # False


# ---------------------------
# Superconjunto (issuperset)
# ---------------------------

print(f"A é superconjunto de B? {conjunto_a.issuperset(conjunto_b)}")  # False
print(f"B é superconjunto de A? {conjunto_b.issuperset(conjunto_a)}")  # True


# ---------------------------
# Conjuntos Disjuntos (sem elementos em comum)
# ---------------------------

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(f"\nA e B são disjuntos? {conjunto_a.isdisjoint(conjunto_b)}")  # True
print(f"A e C são disjuntos? {conjunto_a.isdisjoint(conjunto_c)}")  # False


# ---------------------------
# Adicionando Elementos ao Conjunto
# ---------------------------

sorteio = {1, 23}
sorteio.add(25)
print(f"\nSorteio após adicionar 25: {sorteio}")  # {1, 23, 25}

sorteio.add(42)
print(f"Sorteio após adicionar 42: {sorteio}")  # {1, 23, 25, 42}

sorteio.add(25)
print(f"Sorteio após tentar adicionar 25 novamente: {sorteio}")  # sem mudança


# ---------------------------
# Verificando a Existência de Elementos
# ---------------------------

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"\nO número 1 está no conjunto? {'sim' if 1 in numeros else 'não'}")  # True
print(f"O número 10 está no conjunto? {'sim' if 10 in numeros else 'não'}")  # False



# ---------------------------
# Criação e Manipulação Básica de Listas
# ---------------------------

# Criando uma lista vazia
lista = []

# Adicionando elementos com append()
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])  # Lista dentro da lista

print(f"Lista com 3 elementos: {lista}")  # [1, 'Python', [40, 30, 20]]

# Redefinindo a lista manualmente
lista = [1, "Python", [40, 30, 20]]
print(f"Lista redefinida: {lista}")

# Limpando a lista
lista.clear()
print(f"Lista após clear(): {lista}")  # []

# Copiando a lista (sem afetar a original)
lista = [1, "Python", [40, 30, 20]]
copia = lista.copy()
print(f"Lista original copiada: {copia}")

# ---------------------------
# Contando Ocorrências com count()
# ---------------------------

cores = ["vermelho", "azul", "verde", "azul"]
print(f"Quantas vezes 'vermelho': {cores.count('vermelho')}")  # 1
print(f"Quantas vezes 'azul': {cores.count('azul')}")          # 2
print(f"Quantas vezes 'verde': {cores.count('verde')}")        # 1

# ---------------------------
# Adicionando Vários Elementos com extend()
# ---------------------------

linguagens = ["python", "js", "c"]
print(f"\nAntes do extend: {linguagens}")

linguagens.extend(["java", "csharp"])
print(f"Após o extend: {linguagens}")

# ---------------------------
# Buscando Posições com index()
# ---------------------------

print(f"\nÍndice de 'java': {linguagens.index('java')}")    # 3
print(f"Índice de 'python': {linguagens.index('python')}")  # 0

# ---------------------------
# Removendo Elementos com pop() e remove()
# ---------------------------

# Usando pop() para remover por índice (ou o último por padrão)
print(f"\nRemovido com pop(): {linguagens.pop()}")   # csharp
print(f"Removido com pop(): {linguagens.pop()}")     # java
print(f"Removido com pop(): {linguagens.pop()}")     # c
print(f"Removido com pop(0): {linguagens.pop(0)}")   # python

# Redefinindo lista
linguagens = ["python", "js", "c", "java", "csharp"]

# Usando remove() para remover por valor
linguagens.remove("c")
print(f"Lista após remove('c'): {linguagens}")

# ---------------------------
# Invertendo e Ordenando Listas
# ---------------------------

# Revertendo ordem com reverse()
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(f"\nLista invertida: {linguagens}")

# Ordenando alfabeticamente com sort()
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(f"Lista ordenada (crescente): {linguagens}")

# Ordenando em ordem decrescente
linguagens.sort(reverse=True)
print(f"Lista ordenada (decrescente): {linguagens}")

# ---------------------------
# Ordenando por Tamanho dos Itens
# ---------------------------

linguagens = ["python", "js", "c", "java", "csharp"]

# Menor para maior
linguagens.sort(key=lambda x: len(x))
print(f"\nOrdenado por tamanho (crescente): {linguagens}")

# Maior para menor
linguagens.sort(key=lambda x: len(x), reverse=True)
print(f"Ordenado por tamanho (decrescente): {linguagens}")

# ---------------------------
# Ordenando com sorted() (sem modificar a lista original)
# ---------------------------

linguagens = ["python", "js", "c", "java", "csharp"]

print(f"\nOriginal: {linguagens}")
print(f"sorted() crescente por tamanho: {sorted(linguagens, key=lambda x: len(x))}")
print(f"sorted() decrescente por tamanho: {sorted(linguagens, key=lambda x: len(x), reverse=True)}")

# ---------------------------
# Tamanho da Lista com len()
# ---------------------------

print(f"\nTamanho da lista: {len(linguagens)}")  # 5

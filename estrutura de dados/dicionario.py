# ======================= DICIONÁRIOS (dict) =======================

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])     # Guilherme
print(dados["idade"])    # 28
print(dados["telefone"]) # 3333-1234

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"
print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}


# ======================= DICIONÁRIO DE DICIONÁRIOS =======================

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)  # 3443-2121


# ======================= ITERAÇÃO =======================

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)


# ======================= MÉTODOS DE DICIONÁRIO =======================

contatos.clear()
print(contatos)  # {}

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia["guilherme@gmail.com"])     # {"nome": "Gui"}

resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)  # {'nome': None, 'telefone': None}

resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)  # {'nome': 'vazio', 'telefone': 'vazio'}


# ======================= get() =======================

resultado = contatos.get("chave")
print(resultado)  # None

resultado = contatos.get("chave", {})
print(resultado)  # {}

resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}


# ======================= items(), keys(), values() =======================

print(contatos.items())   # dict_items([('guilherme@gmail.com', {...})])
print(contatos.keys())    # dict_keys(['guilherme@gmail.com'])

print(contatos.values())  # dict_values([...]) com os dicionários internos


# ======================= pop(), popitem(), del =======================

resultado = contatos.pop("guilherme@gmail.com")
print(resultado)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

resultado = contatos.pop("guilherme@gmail.com", {})
print(resultado)  # {}

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
resultado = contatos.popitem()
print(resultado)  # ('guilherme@gmail.com', {...})

# contatos.popitem()  # KeyError se vazio


# ======================= setdefault() =======================

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # Mantém "Guilherme"
print(contato)

contato.setdefault("idade", 28)  # Adiciona novo campo
print(contato)


# ======================= update() =======================

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)


# ======================= Operador in =======================

print("guilherme@gmail.com" in contatos)  # True
print("megui@gmail.com" in contatos)      # False
print("idade" in contatos["guilherme@gmail.com"])    # False
print("telefone" in contatos["giovanna@gmail.com"])  # True


# ======================= Remoção com del =======================

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]
print(contatos)

#*args coleta os argumentos passados por posição em uma tupla.
def somar_todos(*args):
    return sum(args)

print(somar_todos(1, 2, 3))        # 6
print(somar_todos(10, 20))         # 30
print(" ")


#**kwargs coleta os argumentos passados com nomes em um dicionário.
def saudacao_personalizada(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} diz: {valor}")
       
saudacao_personalizada(Ana="Olá!", João="Oi!", Maria="Bom dia!")
print(" ")



#Ordem importa:
#Primeiro *args
#@Depois **kwargs
def mostrar_argumentos(*args, **kwargs):
    print("Posicionais:", args)
    print("Nomeados:", kwargs)
    print(" ")
mostrar_argumentos(1, 2, 3, nome="Alice", idade=30)




#Usando *args e **kwargs para repassar argumentos
def imprimir_dados(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

dados = ("Carlos", 25)
mais_dados = {"nome": "Ana", "idade": 30}

imprimir_dados(*dados)       # Desempacotando tupla
imprimir_dados(**mais_dados) # Desempacotando dicionário
print(" ")

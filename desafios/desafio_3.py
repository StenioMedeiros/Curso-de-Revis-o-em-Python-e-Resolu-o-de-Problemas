from datetime import datetime
import textwrap

# Utilitário para obter data e hora atual formatada
def verificar_dia():
    hoje = datetime.now()
    return f'{hoje.strftime("%d/%m/%y %H:%M:%S")}'

# Depósito - argumentos apenas por posição
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        dia = verificar_dia()
        deposito = f'Depósito de R$ {valor:.2f} realizado com sucesso! Em {dia}\n\n'
        extrato += deposito
        print(deposito)
    else:
        print('Valor inválido! Tente novamente.')
    return saldo, extrato

# Saque - argumentos apenas por nome
def sacar(*, valor, saldo, limite_saque, numero_de_saques, limite_saque_diario, extrato):
    if valor < 0 or valor > saldo:
        print('Valor inválido ou saldo insuficiente! Tente novamente.')
    elif valor > limite_saque:
        print(f'O valor do saque não pode ser maior que R$ {limite_saque:.2f}. Tente novamente.')
    elif numero_de_saques >= limite_saque_diario:
        print(f'Número máximo de saques diários atingido ({limite_saque_diario}). Tente novamente amanhã.')
    else:
        saldo -= valor
        numero_de_saques += 1
        sac = f'Saque de R$ {valor:.2f} realizado com sucesso! Em {verificar_dia()}\n\n'
        extrato += sac
        print(sac)
    return saldo, extrato, numero_de_saques

# Exibir extrato - argumentos mistos
def exibir_extrato(saldo, *, extrato):
    print("\n=========== EXTRATO ===========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Criar novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já existente!")
        return
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

# Filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Criar nova conta
def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return
    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso!")

# Listar todas as contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        Número da Conta: {conta['numero']}
        Titular: {conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        Número da Conta: {conta['numero']}
        Titular: {conta['usuario']['nome']}
        """
        print( "=" * 40)
        print(textwrap.dedent(linha))

# Menu interativo
def menu():
    menu = """\n========================== MENU ==========================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Criar Usuário
    [7] Listar conas
    [8] Sair
    =>>"""
    return input(textwrap.dedent(menu))

# Função principal
def main():
    print('Bem-vindo ao Sistema Bancário Simples!')

    saldo = 0 
    limite_saque = 500
    extrato = ''
    numero_de_saques = 0
    usuarios = []
    contas = []
    AGENCIA = "0001"
    numero_conta = 1
    LIMITE_SAQUE_DIARIO = 3

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == '2':
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato, numero_de_saques = sacar(
                valor=valor,
                saldo=saldo,
                limite_saque=limite_saque,
                numero_de_saques=numero_de_saques,
                limite_saque_diario=LIMITE_SAQUE_DIARIO,
                extrato=extrato
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_conta(AGENCIA, numero_conta, usuarios, contas)
            numero_conta =+ 1

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '7':
            listar_contas(contas)

        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print('Opção inválida, tente novamente.')

# Ponto de entrada
if __name__ == "__main__":
    main()

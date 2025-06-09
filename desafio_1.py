from datetime import datetime


def verificar_dia():
    hoje = datetime.now()
    return f'{hoje.strftime("%d/%m/%y %H:%M:%S")}'


def depositar(valor, saldo, extrato, limite_saque):
    if valor > 0:
        saldo += valor
        dia = verificar_dia()
        deposito = f'Depósito de R$ {valor:.2f} realizado com sucesso! Em {dia}\n'
        extrato += deposito
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso! Em {dia}')

    else:
        print('valor invalido! tente novamente.')

    return saldo, extrato, limite_saque



def sacar(valor, saldo, limite_saque, numero_de_saques, limite_saque_diario, extrato):
    if valor < 0 or valor > saldo:
        print('Valor inválido ou saldo insuficiente! Tente novamente.')
    
    elif valor > limite_saque:
        print(f'O valor do saque não pode ser maior que R$ {limite_saque:.2f}. Tente novamente')
    
    elif numero_de_saques >= limite_saque_diario:
        print(f'Número máximo de saques diários atingido ({limite_saque_diario}). Tente novamente amanhã.')
    
    else:
        saldo -= valor
        numero_de_saques += 1
        sac = f'Saque de R$ {valor:.2f} realizado com sucesso! Em {verificar_dia()}\n'
        extrato += sac

        print(f'Saque de R$ {valor:.2f} realizado com sucesso!')

    return saldo, extrato, numero_de_saques




# Sistema Bancário Simples

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>>"""

saldo = 0 
limite_saque = 500
extrato = ''
numero_de_saques = 0
limite_saque_dia = 3

while True:
    opicao = input(menu)
    if opicao == '1':
        valor = float(input('Digite o valor do deposito: '))
        saldo, extrato, limite_saque = depositar(valor, saldo, extrato, limite_saque)

    elif opicao == '2':
        valor = float(input('digite o valor d saque: '))
        saldo, extrato, numero_de_saques = sacar(valor, saldo, limite_saque, numero_de_saques, limite_saque_dia, extrato)

    elif opicao == '3':
        print('\n\nSaldo atual: R$ {:.2f}'.format(saldo))
        if extrato:
            print('Extrato:\n')
            print(extrato)

    elif opicao == '4':
        print('Saindo do sistema')
        break
    else:
        print('Opção inválida, tente novamente.')
        

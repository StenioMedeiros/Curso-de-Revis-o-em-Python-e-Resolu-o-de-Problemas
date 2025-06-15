# -------------------------------------
# Encapsulamento em Python (com _ e __)
# -------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular     # público
        self._saldo = saldo_inicial  # protegido (convenção)
        self.__senha = "1234"      # privado (name mangling)

    # ------------------------
    # Métodos públicos
    # ------------------------

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f" Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(" Valor inválido para depósito.")

    def sacar(self, valor, senha):
        if self.__verificar_senha(senha):
            if 0 < valor <= self._saldo:
                self._saldo -= valor
                print(f" Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print(" Valor de saque inválido ou saldo insuficiente.")
        else:
            print(" Senha incorreta. Acesso negado!")

    def ver_saldo(self):
        print(f" Saldo atual de {self.titular}: R$ {self._saldo:.2f}")

    # ------------------------
    # Método "privado" (name mangling)
    # ------------------------

    def __verificar_senha(self, senha):
        return senha == self.__senha

    # ------------------------
    # Método para mudar a senha (controlado)
    # ------------------------

    def alterar_senha(self, senha_antiga, nova_senha):
        if self.__verificar_senha(senha_antiga):
            self.__senha = nova_senha
            print(" Senha alterada com sucesso!")
        else:
            print(" Senha antiga incorreta. Tente novamente.")

# -------------------------------------
# Exemplo de uso da classe ContaBancaria
# -------------------------------------

conta = ContaBancaria("Alice", 1000)

print("\n Tentando acessar diretamente o saldo (protegido):")
print("Saldo (via _saldo):", conta._saldo)  # possível, mas desencorajado

print("\n Tentando acessar senha privada diretamente:")
try:
    print(conta.__senha)
except AttributeError:
    print(" Atributo privado! Acesso negado diretamente.")

print("\n Operações controladas:")
conta.ver_saldo()
conta.depositar(500)
conta.sacar(300, "1234")
conta.ver_saldo()

print("\n Tentando sacar com senha errada:")
conta.sacar(100, "0000")

print("\n Alterando a senha:")
conta.alterar_senha("1234", "abcd")

print("\n Saque com nova senha:")
conta.sacar(100, "abcd")

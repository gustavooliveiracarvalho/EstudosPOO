# Declaração da classe
class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """
    # Atributos da classe
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')

    # Métodos da classe
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}.")

    def sacar(self, valor):
        if valor >= self.saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE.')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} AUTORIZADO na conta {self.id}.\nSaldo atual: {self.saldo:,.2f}')

# Declaração do objeto
c1 = ContaBancaria(112, 'Maria', 3000)
c1.depositar(500)
c1.sacar(1000)
print(c1)

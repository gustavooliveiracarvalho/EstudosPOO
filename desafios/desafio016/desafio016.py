from rich import print
from rich import inspect

class Funcionario:
    # Atributos de classe.
    empresa = "TOTVS"

    def __init__(self, nome, setor, cargo):
        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.'

# Declaração de objetos
c1 = Funcionario("Maria", "Compras", "Analista de Compras")
print(c1.apresentacao())
# inspect(c1, methods = True)

c2 = Funcionario("Matheus", "Administrativo", "Diretor")
print(c2.apresentacao())

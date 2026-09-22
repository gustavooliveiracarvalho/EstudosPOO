# Declaração de Classe
class Funcionario:
    """
    Essa classe cria um Funcionário, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto('nome', idade)
    """
    def __init__(self, nome= 'desconhecido', idade= 0): # Método Contrutor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): #Dunder Method
        return f"{self.nome} é Funcionário(a) e tem {self.idade} anos de idade."

    def __gatestate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}."
#Declaração de Objeto
g1 = Funcionario('Maria', 17)
g1.aniversario()
print(g1)

g2 = Funcionario('Mauro', 53)
g2.aniversario()
print(g2.__gatestate__())
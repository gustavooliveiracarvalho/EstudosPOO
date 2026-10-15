from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'Preço'.center(30, '~')}"
        precoformatado = f"R${self.preco:,.2f}"
        conteudo += f" {precoformatado.center(30, '.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)
# Programa Principal
p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)
p1.etiqueta()
p2.etiqueta()
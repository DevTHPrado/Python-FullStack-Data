from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) #desconto de 8%. Se eu não quiser colocar desconto, é só eu colocar o pass, mas é obrigatório ter essa função por causa do abstractmethod
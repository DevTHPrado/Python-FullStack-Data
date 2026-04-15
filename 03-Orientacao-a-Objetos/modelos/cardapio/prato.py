from modelos.cardapio.item_cardapio import ItemCardapio
#estamos fazendo o processo de Herança da classe ItemCardapio, importando ela para a nossa classe Prato, ela irá herdar os atributos da classe importada
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #o super() permite que nós acessamos as informações de outra classe, no caso, da classe ItemCardapio
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05) #desconto de 5%. Se eu não quiser colocar desconto, é só eu colocar o pass, mas é obrigatório ter essa função por causa do abstractmethod
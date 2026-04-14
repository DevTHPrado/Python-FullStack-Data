from modelos.cardapio.item_cardapio import ItemCardapio
#estamos fazendo o processo de Herança da classe ItemCardapio, importando ela para a nossa classe Prato, ela irá herdar os atributos da classe importada
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #o super() permite que nós acessamos as informações de outra classe, no caso, da classe ItemCardapio
        self.descricao = descricao

    def __str__(self):
        return self._nome
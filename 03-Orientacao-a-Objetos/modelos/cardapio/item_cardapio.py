from abc import ABC, abstractmethod #importando o abc para fazer uma classe abstrata

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod #significa que todas as classes derivadas precisam esse método abstrato aplicado
    def aplicar_desconto(self):
        pass
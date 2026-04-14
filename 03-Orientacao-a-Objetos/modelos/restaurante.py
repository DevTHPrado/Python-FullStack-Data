from modelos.avaliacao import Avaliacao #importa a classe Avaliacao do outro código
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante: #class é uma palavra reservada que cria uma Classe
    '''Representa um restaurante e suas características'''
    restaurantes = []

    def __init__(self, nome, categoria): #o def define uma função e o __init__ (construtor) obriga que a classe tenha os valores 'nome' e 'categoria' já atribuidos
        '''Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante'''
        self._nome = nome.title() #o self é a referencia da instancia que estamos uutilizando naquele momento, o title() é para todos os nomes de restaurantes começarem com a letra maiuscula
        self._categoria = categoria.upper() #o upper() é para todas as categorias de restaurante aparecerem com todas as letras maiusculas
        self._ativo = False #ao colocar o _ antes do ativo mostra o atributo está protegido, que eu não estou eperando que os usuários acessem ele
        self._avaliacao = [] #é uma lista por que cada restaurante pode ter varias avaliações
        self._cardapio = []
        Restaurante.restaurantes.append(self) #toda vez que a gente criar um restaurante, ele irá direto para a nossa lista restaurantes

    def __str__(self): #o __str__ transforma em texto
        '''Retorna uma representação em string do restaurante'''
        return f'{self.nome} | {self.categoria}'

    @classmethod #é uma boa prática indicar que se trata de um método da classe sempre que temos um método que não está referenciado com uma instância, mas sim à classe.
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes'''
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #o ljust é só para 'design', pois ele vai dar 25 espaços. Tivemos que transformar o restaurante.media_avaliacoes em String pois o ljust não funciona para Float

    @property #altera a forma de como o atributo vai ser lido
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante'''
        return '☒' if self._ativo else '☐' #aqui ele está alterando de: se for True para ☒ e se for False para ☐

    def alternar_estado(self):
        '''Alterna o estado de atividade do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5)'''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota) #quem da a avaliação? O cliente, e oq ele dá? A nota
            self._avaliacao.append(avaliacao)

    @property #para poder exibir esse metodo, por ele não ser um metodo comun, usamos o @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante'''
        if not self._avaliacao: #caso o restaurante não tenha nenhuma avaliação (acabou de ser criado)
            return '-' #retorne um - para mostrar que ele ainda não tem avaliação
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #O sum() ele soma tudo que estiver nele. Oq ele vai fazer, vai pegar tofdas a avaliações, e para cada uma, a única informação que eu quero é a nota, e some elas
        quantidade_de_notas = len(self._avaliacao) #ele vai pegar a quantidade de notas que o restaurante que estamos usando tem
        media = round(soma_das_notas / quantidade_de_notas, 1) #o round serve para ele mostrar o resultado dessa equação que montamos com apenas 1 casa decimal (por isso colocamos o 1 no final), ex: 4,5, 2,1, 1,0
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #o isinstance é para verificar se aquele item é uma instancia de ItemCardapio
            self._cardapio.append(item)

    @property #usado para indicar quando a função se trata somente de leitura
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'): #hasattr significa "se tiver atributo x"
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.tamanho}'
                print(mensagem_bebida)

#o comando dir ele mostra todos os métodos da classe que criamos
#o comando virs mostra somente os valores que foram atribuidos a classe
#coolsymbol.com no Google para colocar emojis
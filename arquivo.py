import sys


class Livro:


    def __init__(
            self, titulo: str, autor: str, ano_publicação: int,
            qtd_copias_disponiveis = 90, qtd_copias_totais = 100):

        self._titulo = titulo
        self._autor = autor
        self._ano_publicação = ano_publicação
        self._qtd_copias_disponiveis = qtd_copias_disponiveis
        self._qtd_copias_totais = qtd_copias_totais


    @property
    def get_titulo(self):
        return self._titulo

    @property
    def get_autor(self):
        return self._autor

    @property
    def get_ano_publicação(self):
        return self._ano_publicação

    @property
    def get_qtd_copias_disponiveis(self):
        return self._qtd_copias_disponiveis

    @property
    def get_qtd_copias_totais(self):
        return self._qtd_copias_totais

    def qtd_copias_disponiveis(self, valor: int):
        self._qtd_copias_disponiveis += valor


    def emprestar(self, valor: int):

        valor = valor

        try:

            valor = int(valor)

            if valor <= 0:
                print( f'''
            Infelizmente, o valor digitado é menor do que zero e não será possivel efetuar o emprestimo do livro!.\n
                        ''')
                return False

            if valor > self.get_qtd_copias_disponiveis:
                print(f'''
            Infelizmente, o valor digitado é maior do que a quantidade de livros disponiveis, tente novamente!.\n
                ''')
                return False

            self.qtd_copias_disponiveis(-valor)
            print(f'''
            O livro {self.get_titulo}, teve o total de {valor} emprestimos!.\n
            ''')
            return True

        except ValueError:

            return f'''
            Digite um valor valido para realizar o emprestimo do livro!.\n
            '''

    def mostra_livro(self):
        return f'''
            Livro: {self.get_titulo}, Autor: {self.get_autor}, Ano de publicação: {self.get_ano_publicação}, Quantidade de copias disponiveis: {self.get_qtd_copias_disponiveis}, Quantidade Total de copias: {self.get_qtd_copias_totais}.
            '''


def main():

    menu = f'''
            Digite [1] para emprestar um livro.
    '''

    print(menu)


    option = int(input("Digite aqui: "))

    if option == 1:

        valor = int(input("Digite a quantidade de livros que deseja receber: "))
        nome_livro = input("Digite o nome do livro: ")
        ano_publicação = int(input("Digite o ano de publicação do livro: "))
        autor = input("Digite o autor do livro: ")

        c1 = Livro(titulo=nome_livro, autor=autor, ano_publicação=ano_publicação)

        v1 = c1.emprestar(valor=valor)

        if v1 == True:

            escolha = input(f"Deseja verificar os livros cadastrados?. S para sim, N para n: ").upper()

            if escolha == "S":

                print(c1.mostra_livro())

            else:

                sys.exit(0)

        else:

            sys.exit(0)

    elif option == 2:
        pass


main()
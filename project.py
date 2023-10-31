

def cria_intersecao(col, lin):
    if not (isinstance(col, str) and isinstance(lin, int)):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col, lin)


def obtem_col(intersecao):
    if isinstance(intersecao[0], str):
        return intersecao[0]


def obtem_lin():
    if isinstance(intersecao[1], int):
        return intersecao[1]


def eh_intersecao(arg):
    if isinstance(arg, tuple) and len(arg[0]) == 1 and ('A' <= arg[0] <= 'S') and (1 <= arg[1] <= 19):
        return True
    else:
        return False


def intersecoes_iguais(arg, other):
    if arg[0] == other[0] and arg[1] == other[1]:
        return True
    else:
        return False


def intersecao_para_str(arg):
    return arg[0] + str(arg[1])


@staticmethod
def str_para_intersecao(arg):
    letter = arg[0]
    number_str = arg[1:]

    return (letter, int(number_str))


def obtem_intersecoes_adjacentes(intersecao, leitura):
    column, row = intersecao
    adjacent = []

    possible_adjacent = [
        (chr(ord(column) - 1), row),  # Left
        (chr(ord(column) + 1), row),  # Right
        (column, row - 1),  # Above
        (column, row + 1),  # Below
    ]

    for adj in possible_adjacent:
        if 'A' <= adj[0] <= leitura[0] and 1 <= adj[1] <= leitura[1]:
            adj_str = adj[0] + str(adj[1])
            adjacent.append(adj_str)

    return tuple(adjacent)

def ordena_intersecoes(tuplo_intersecoes):
    # High-level function to sort intersections
    pass

class Pedra:
    def __init__(self, jogador):
        # Constructor to create a stone
        pass

    def eh_pedra(self, arg):
        # Recognizer to check if it's a stone
        pass

    def eh_pedra_branca(self):
        # Recognizer to check if it's a white stone
        pass

    def eh_pedra_preta(self):
        # Recognizer to check if it's a black stone
        pass

    def pedras_iguais(self, other):
        # Tester to check if two stones are equal
        pass

    def pedra_para_str(self):
        # Transformer to convert stone to a string
        pass

def eh_pedra_jogador(pedra):
    # High-level function to check if it's a player's stone
    pass


class Goban:
    def __init__(self, n):
        # Constructor to create an empty Go board
        pass

    def __init__(self, n, ib, ip):
        # Constructor to create a Go board with stones
        pass

    def cria_copia_goban(self):
        # Constructor to create a copy of a Go board
        pass

    def obtem_ultima_intersecao(self):
        # Selector to get the last intersection
        pass

    def obtem_pedra(self, intersecao_i):
        # Selector to get the stone at an intersection
        pass

    def obtem_cadeia(self, intersecao_i):
        # Selector to get a tuple of intersections in a chain
        pass

    def coloca_pedra(self, intersecao_i, pedra):
        # Modifier to place a stone on the board
        pass

    def remove_pedra(self, intersecao_i):
        # Modifier to remove a stone from the board
        pass

    def remove_cadeia(self, tuplo_intersecoes):
        # Modifier to remove a chain of stones
        pass

    def eh_goban(self, arg):
        # Recognizer to check if it's a Go board
        pass

    def eh_intersecao_valida(self, intersecao_i):
        # Recognizer to check if an intersection is valid on the board
        pass

    def gobans_iguais(self, other):
        # Tester to check if two Go boards are equal
        pass

    def goban_para_str(self):
        # Transformer to convert the Go board to a string
        pass

def obtem_territorios(goban):
    # High-level function to get territories
    pass

def obtem_adjacentes_diferentes(goban, tuplo_intersecoes):
    # High-level function to get different adjacent intersections
    pass

def jogada(goban, intersecao_i, pedra):
    # High-level function to make a move (place a stone, remove opponent's stones)
    pass

def obtem_pedras_jogadores(goban):
    # High-level function to get the number of stones for each player
    pass


a = cria_intersecao("A", 2)
b = obtem_col(a)
c = eh_intersecao(a)
print(c)

d = intersecao_para_str(a)
print(d)

e = str_para_intersecao(d)
print(e)

f = obtem_intersecoes_adjacentes(a,  cria_intersecao('S', 19))
print(f)



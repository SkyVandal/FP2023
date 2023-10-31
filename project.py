def cria_intersecao(col, lin):
    if not (isinstance(col, str) and isinstance(lin, int)):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col, lin)


def obtem_col(intersecao):
    if isinstance(intersecao[0], str):
        return intersecao[0]


def obtem_lin(intersecao):
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

    def key_func(intersection):
        column, row = intersection
        return (column, row)

    sorted_intersections = sorted(tuplo_intersecoes, key=key_func)

    return sorted_intersections


#PEDRA
def cria_pedra_branca():
    return "O"

def cria_pedra_preta():
    return "X"

def cria_pedra_neutra():
    return "."

def eh_pedra(arg):
    return arg in ["O", "X", " "]

def eh_pedra_branca(pedra):
    return pedra == "O"

def eh_pedra_preta(pedra):
    return pedra == "X"

def pedras_iguais(p1, p2):
    return p1 == p2

def pedra_para_str(pedra):
    return pedra

def eh_pedra_jogador(pedra):
    return pedra in ["O", "X"]


#GOBAN
def cria_goban_vazio(n):
    return [['.' for _ in range(n)] for _ in range(n)]

def cria_goban(n, brancas, pretas):
    goban = cria_goban_vazio(n)
    for tup in brancas:
        col = n - (ord(tup[0]) - 64)
        row = tup[1] - 1

def cria_copia_goban():
    # Constructor to create a copy of a Go board
    pass

def obtem_ultima_intersecao():
    # Selector to get the last intersection
    pass

def obtem_pedra(intersecao_i):
    # Selector to get the stone at an intersection
    pass

def obtem_cadeia(intersecao_i):
    # Selector to get a tuple of intersections in a chain
    pass

def coloca_pedra(intersecao_i, pedra):
    # Modifier to place a stone on the board
    pass

def remove_pedra(intersecao_i):
    # Modifier to remove a stone from the board
    pass

def remove_cadeia(tuplo_intersecoes):
    # Modifier to remove a chain of stones
    pass

def eh_goban(arg):
    # Recognizer to check if it's a Go board
    pass

def eh_intersecao_valida(intersecao_i):
    # Recognizer to check if an intersection is valid on the board
    pass

def gobans_iguais(other):
    # Tester to check if two Go boards are equal
    pass

def goban_para_str():
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

#pretty print
def print_go_board(board):
    labels = "  A B C D E F G H I"
    for row in range(len(board), 0, -1):
        print(f"{row} {' '.join(board[row - 1])} {row}")
    print(labels)

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
print("EXEMPLOS")
i1 = cria_intersecao('A', 2)
i2 = cria_intersecao('B', 13)

z = intersecoes_iguais(i1, i2)
print(z)

x = intersecao_para_str(i2)
print(x)

v = intersecoes_iguais(i1, str_para_intersecao('A2'))
print(v)

n = tuple(intersecao_para_str(i) for i in obtem_intersecoes_adjacentes(i1, cria_intersecao('S',19)))
print(n)

tup = (cria_intersecao('A',1), cria_intersecao('A',3), cria_intersecao('B',1), cria_intersecao('B',2))

m = tuple(intersecao_para_str(i) for i in ordena_intersecoes(tup))
print(m)


print("EXEMPLOS PEDRA")
bb = cria_pedra_branca()
print(eh_pedra(bb))

pp = cria_pedra_preta()
print(pedras_iguais(bb, pp))

print(pedra_para_str(bb), pedra_para_str(pp))

print(eh_pedra_jogador(cria_pedra_neutra()))

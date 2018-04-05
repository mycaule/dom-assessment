import random
import itertools

def allowed_moves(board, color):
    # board: _ empty, b/w piece, B/W king
    # color: b/w next to play
    positions = []
    for i,j in itertools.product(range(8), range(8)):
        if board[i][j].lower() == color and (i + j) % 2 == 1:
            positions.append((i, j))

    M1 = reduce(lambda a,v: a+v, map(lambda p: simple_moves(p, board, color), positions), [])
    M2 = reduce(lambda a,v: a+v, map(lambda p: capture_moves(p, board, color), positions), [])

    print('M2', M2)
    return M2 if len(M2) else M1

def sigma(pos):
    return (7-pos[0], 7-pos[1])

def white_to_black(board):
    return map(
        lambda l:
            l[::-1].replace('b', 't').replace('B', 'T').replace('w', 'b').replace('W', 'B'),
        board[::-1]
    )

def checkerboard_physics(pos, board, color, add_if):
    # Assume the pieces are black
    moves = []
    if pos[0] == 7:  # Become king in the last row
        if pos[1] == 0:
            add_if(moves, -1, +1)
        else:
            add_if(moves, -1, -1)
            add_if(moves, -1, +1)
    else:            # In the six first rows
        # Case where the piece is already a king
        if board[pos[0]][pos[1]] == color.upper() and pos[0] > 0:
            if pos[1] == 0:
                add_if(moves, -1, +1)
            elif pos[1] == 7:
                add_if(moves, -1, -1)
            else:
                add_if(moves, -1, -1)
                add_if(moves, -1, +1)

        if pos[1] == 0:
            add_if(moves, +1, +1)
        elif pos[1] == 7:
            add_if(moves, +1, -1)
        else:
            add_if(moves, +1, -1)
            add_if(moves, +1, +1)
    return moves

def simple_moves(pos, board, color):
    def add_if_empty(l, i, j):
        if board[pos[0]+i][pos[1]+j] == '_':
            l.append([pos, (pos[0]+i, pos[1]+j)])

    if color == 'b':
        return checkerboard_physics(pos, board, color, add_if_empty)
    else: # Apply a symmetry to switch from white to black
        return map(lambda x: map(sigma, x), simple_moves(sigma(pos), white_to_black(board), 'b'))

def capture_moves(pos, board, color):
    def add_if_neighbor(l, i, j):
        ngh = board[pos[0]+i][pos[1]+j]
        if ngh != '_' and ngh.lower() != color:
            if pos[0]+2*i in range(8) and pos[1]+2*j in range(8):
                if board[pos[0]+2*i][pos[1]+2*j] == '_':
                    l.append([pos, (pos[0]+2*i, pos[1]+2*j)])

    if color == 'b':
        return checkerboard_physics(pos, board, color, add_if_neighbor)
    else: # Apply a symmetry to switch from white to black
        return map(lambda x: map(sigma, x), capture_moves(sigma(pos), white_to_black(board), 'b'))

def play(board, color):
    return random_play(board, color)

def random_play(board, color):
    moves = allowed_moves(board, color)
    return random.choice(moves)

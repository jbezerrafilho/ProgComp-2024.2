
def is_pawn_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento do peão é válido.
    """
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto
    direction = -1 if piece_color == 'w' else 1  # Direção do movimento: brancos movem para cima, pretos para baixo

    # Verifica se o movimento é para frente
    if col == target_col:
        # Movimento para frente
        if target_row == row + direction:
            # Movimento de uma casa
            return board[target_row][target_col] == ''
        elif target_row == row + 2 * direction and (row == 6 or row == 1):
            # Movimento de duas casas no primeiro movimento
            return board[row + direction][col] == '' and board[target_row][target_col] == ''
    # Verifica se é uma captura diagonal
    elif abs(target_col - col) == 1 and target_row == row + direction:
        target_piece = board[target_row][target_col]
        return target_piece != '' and target_piece[0] != piece_color

    return False

def is_rook_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento da torre é válido.
    """
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto

    # Verifica se o movimento é em linha reta (horizontal ou vertical)
    if row != target_row and col != target_col:
        return False

    # Verifica se o caminho está livre
    if row == target_row:
        # Movimento horizontal
        step = 1 if target_col > col else -1
        for c in range(col + step, target_col, step):
            if board[row][c] != '':
                return False
    else:
        # Movimento vertical
        step = 1 if target_row > row else -1
        for r in range(row + step, target_row, step):
            if board[r][col] != '':
                return False

    # Verifica se a casa de destino está vazia ou contém uma peça adversária
    target_piece = board[target_row][target_col]
    return target_piece == '' or target_piece[0] != piece_color


def is_knight_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento do cavalo é válido.
    O cavalo move-se em "L": duas casas em uma direção e uma casa na direção perpendicular.
    Ele pode pular sobre outras peças.
    """
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto

    # Verifica se o movimento é em "L"
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
        return False

    # Verifica se a casa de destino está vazia ou contém uma peça adversária
    target_piece = board[target_row][target_col]
    return target_piece == '' or target_piece[0] != piece_color

# rules.py

def is_bishop_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento do bispo é válido.
    O bispo move-se em diagonais, por qualquer número de casas desocupadas.
    Ele não pode pular sobre outras peças.
    """
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto

    # Verifica se o movimento é diagonal
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    if row_diff != col_diff:
        return False

    # Verifica se o caminho está livre
    row_step = 1 if target_row > row else -1
    col_step = 1 if target_col > col else -1
    current_row, current_col = row + row_step, col + col_step
    while current_row != target_row and current_col != target_col:
        if board[current_row][current_col] != '':
            return False
        current_row += row_step
        current_col += col_step

    # Verifica se a casa de destino está vazia ou contém uma peça adversária
    target_piece = board[target_row][target_col]
    return target_piece == '' or target_piece[0] != piece_color

# rules.py

def is_queen_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento da rainha é válido.
    A rainha combina os movimentos da torre e do bispo.
    """
    # Verifica se o movimento é válido como torre ou bispo
    return is_rook_move_valid(board, selected_piece, selected_pos, target_pos) or \
           is_bishop_move_valid(board, selected_piece, selected_pos, target_pos)


# rules.py

def is_king_move_valid(board, selected_piece, selected_pos, target_pos):
    """
    Verifica se o movimento do rei é válido.
    O rei move-se uma casa em qualquer direção (horizontal, vertical ou diagonal).
    """
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto

    # Verifica se o movimento é de uma casa em qualquer direção
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    if row_diff > 1 or col_diff > 1:
        return False

    # Verifica se a casa de destino está vazia ou contém uma peça adversária
    target_piece = board[target_row][target_col]
    return target_piece == '' or target_piece[0] != piece_color

def move_piece(board, selected_piece, selected_pos, target_pos, success_sound, error_sound):
    """
    Move a peça no tabuleiro se o movimento for válido.
    """
    piece_type = selected_piece[1]
    is_valid_move = False

    if piece_type == 'p':
        is_valid_move = is_pawn_move_valid(board, selected_piece, selected_pos, target_pos)
    elif piece_type == 'r':
        is_valid_move = is_rook_move_valid(board, selected_piece, selected_pos, target_pos)
    elif piece_type == 'n':
        is_valid_move = is_knight_move_valid(board, selected_piece, selected_pos, target_pos)
    elif piece_type == 'b':
        is_valid_move = is_bishop_move_valid(board, selected_piece, selected_pos, target_pos)
    elif piece_type == 'q':
        is_valid_move = is_queen_move_valid(board, selected_piece, selected_pos, target_pos)
    elif piece_type == 'k':
        is_valid_move = is_king_move_valid(board, selected_piece, selected_pos, target_pos)

    if is_valid_move:
        target_piece = board[target_pos[0]][target_pos[1]]
        if target_piece != '' and selected_piece[0] != target_piece[0]:
            success_sound.play()
        board[target_pos[0]][target_pos[1]] = selected_piece
        board[selected_pos[0]][selected_pos[1]] = ''
    else:
        error_sound.play()
        board[selected_pos[0]][selected_pos[1]] = selected_piece

    return is_valid_move
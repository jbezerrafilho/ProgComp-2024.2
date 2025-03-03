
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
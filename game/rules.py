import pygame

# EXTRAI DETALHES DO MOVIMENTO: POSIÇÃO INICIAL - FINAL, POSIÇÃO DESTINO E COR DA PEÇA 
def get_move_details(selected_piece, selected_pos, target_pos):
    row, col = selected_pos
    target_row, target_col = target_pos
    piece_color = selected_piece[0]  # 'w' para branco, 'b' para preto
    return row, col, target_row, target_col, piece_color

# VERIFICA SE A CASA DE DESTINO ESTÁ VAZIA OU CONTÉM PEÇA ADVERSÁRIA 
def is_target_square_valid(board, target_row, target_col, piece_color):
    target_piece = board[target_row][target_col]  
    return target_piece == '' or target_piece[0] != piece_color  

""" CADA FUNÇÃO A SEGUIR VERIFICA SE O MOVIMENTO DE UMA DETERMINADA PEÇA É VÁLIDO """

# PEÃO
def is_pawn_move_valid(board, selected_piece, selected_pos, target_pos):
    row, col, target_row, target_col, piece_color = get_move_details(selected_piece, selected_pos, target_pos)
    step = -1 if piece_color == 'w' else 1 

    # Movimento para frente
    if col == target_col:
        # Movimento de uma casa
        if target_row == row + step:
            return board[target_row][target_col] == ''
        # Movimento de duas casas no primeiro movimento
        elif target_row == row + 2 * step and (row == 6 or row == 1):
            return board[row + step][col] == '' and board[target_row][target_col] == ''
    
    # Captura diagonal
    elif abs(target_col - col) == 1 and target_row == row + step:
        target_piece = board[target_row][target_col]
        return target_piece != '' and target_piece[0] != piece_color

    return False

# TORRE
def is_rook_move_valid(board, selected_piece, selected_pos, target_pos):
    row, col, target_row, target_col, piece_color = get_move_details(selected_piece, selected_pos, target_pos)

    # Verifica se o movimento é em linha reta (horizontal ou vertical)
    if row != target_row and col != target_col:
        return False

    # Verifica o movimento horizontal 
    if row == target_row:
        step = 1 if target_col > col else -1
        for c in range(col + step, target_col, step):
            if board[row][c] != '':
                return False
    # Verifica o movimento vertical
    else:
        step = 1 if target_row > row else -1
        for r in range(row + step, target_row, step):
            if board[r][col] != '':
                return False

    return is_target_square_valid(board, target_row, target_col, piece_color)

# CAVALO
def is_knight_move_valid(board, selected_piece, selected_pos, target_pos):
    row, col, target_row, target_col, piece_color = get_move_details(selected_piece, selected_pos, target_pos)
    # Verifica se o movimento é em "L"
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
        return False

    return is_target_square_valid(board, target_row, target_col, piece_color)

# BISPO
def is_bishop_move_valid(board, selected_piece, selected_pos, target_pos):
    row, col, target_row, target_col, piece_color = get_move_details(selected_piece, selected_pos, target_pos)

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

    return is_target_square_valid(board, target_row, target_col, piece_color)

# RAINHA
def is_queen_move_valid(board, selected_piece, selected_pos, target_pos):
    return is_rook_move_valid(board, selected_piece, selected_pos, target_pos) or \
           is_bishop_move_valid(board, selected_piece, selected_pos, target_pos)

# REI
def is_king_move_valid(board, selected_piece, selected_pos, target_pos):
    row, col, target_row, target_col, piece_color = get_move_details(selected_piece, selected_pos, target_pos)

    # Verifica se o movimento é de uma casa em qualquer direção
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    if row_diff > 1 or col_diff > 1:
        return False

    return is_target_square_valid(board, target_row, target_col, piece_color)

# MOVE A PEÇA SE O MOVIMENTO FOR VÁLIDO
def move_piece(board, selected_piece, selected_pos, target_pos, success_sound, error_sound):
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
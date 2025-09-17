def checkmate(board):
    """Board Setup"""
    
    #Turn input into 2D grid
    lines = board.strip().split('\n')
    if not lines:
        print('Fail')
        return
    
    #Validate square board
    board_size = len(lines)
    for line in lines:
        if len(line) != board_size:
            print('Fail')
            return
    
    grid = [list(line) for line in lines]

    king_pos = find_king(grid, board_size)
    if king_pos is None:
        print('Fail')
        return

    if is_king_in_check(grid, king_pos, [0], king_pos[1], board_size):
        print('Success')
    else:
        print('Fail')

def find_king(grid,)
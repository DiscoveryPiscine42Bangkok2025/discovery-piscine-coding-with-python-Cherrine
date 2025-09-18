def checkmate(board):
    """Board Setup"""
    
    #Turn input into 2D grid
    lines = board.strip().split('\n')
    if not lines:
        print('Fail (invalid board)')
        return
    
    #Validate square board
    board_size = len(lines)
    for line in lines:
        if len(line) != board_size:
            print('Fail (invalid board)')
            return
    
    grid = [list(line) for line in lines]

    king_pos = find_king(grid, board_size)
    if king_pos is None:
        print('Fail (no King or multiple Kings on board)')
        return

    if is_king_in_check(grid, king_pos[0], king_pos[1], board_size):
        print('Success')
    else:
        print('Fail')

def find_king(grid, board_size):
    """Find and validate King Position"""
    king_pos = None
    for i in range(board_size):
        for j in range(board_size):
            if grid[i][j] == 'K':
                if king_pos is not None:
                    return None
                
                king_pos = (i, j)

    return king_pos

# Check if king is in the position of Checkmate
def is_king_in_check(grid, king_row, king_col, board_size):
    return (check_pawn_attacks(grid, king_row, king_col, board_size) or
            check_rook_or_queen_attacks(grid, king_row, king_col, board_size) or
            check_bishop_or_queen_attacks(grid, king_row, king_col, board_size))

# Check if Pawn can attack the King
def check_pawn_attacks(grid, king_row, king_col, board_size):
    # เช็กว่า มี pawn อยู่ตำแหน่งที่ทำให้ king โดน check ไหม (ซ้ายล่าง และ ขวาล่าง)
    check_pos = [(king_row + 1, king_col -1), (king_row + 1, king_col + 1)]
    for row, col in check_pos:
        if 0 <= row < board_size and 0 <= col < board_size:
        # เช็กว่าตำแหน่งนั้นอยู่ภายในตาราง
            if grid[row][col] == 'P':
                return True
    return False

# เช็กแนวตรงทั้ง 4 ด้านจาก K ว่ามี Rook หรือ Queen ไหม ถ้ามีแสดงว่า king โดน check
# เนื่องจาก Queen คือการรวมการเดินของ Rook(แนว+) + Bishop(แนวX) อยู่แล้ว จึงเช็ก Queen ด้วยเลย
def check_rook_or_queen_attacks(grid, king_row, king_col, board_size):
    # เริ่มเช็กด้านบนจาก 'K' ให้สุดก่อนว่ามี 'R' หรือ 'Q' ไหม จากนั้นก็เช็กด้านขวา, ล่าง, ซ้าย ตามลำดับ
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di_row, di_col in directions:
        row, col = king_row + di_row, king_col + di_col
        #ถ้าตำแหน่ง (row, col) มี 'R' หรือ 'Q' => king โดน check
        while 0 <= row < board_size and 0 <= col < board_size:
        # loop จนกว่าว่าตำแหน่งนั้นจะเกินหรือออกนอกตาราง (0 <= row,col < board_size)
            piece = grid[row][col]
            if piece != '.':
                if piece in ('R', 'Q'):
                    return True
                break #ถ้าไม่ใช่ทั้ง 'R', 'Q' และ '.' แสดงว่ามีตัวอื่นบังอยู่ 'R' หรือ 'Q' ที่อาจอยู่ข้างหลังจะไม่สามารถกินได้ => ออกจาก loop เลย
            row += di_row
            col += di_col
    return False

# เช็กแนวทแยงจาก K ว่ามี Bishop หรือ Queen ไหม ถ้ามีแสดงว่า king โดน check check
# เนื่องจาก Queen คือการรวมการเดินของ Rook(แนว+) + Bishop(แนวX) อยู่แล้ว จึงเช็ก Queen ด้วยเลย
def check_bishop_or_queen_attacks(grid, king_row, king_col, board_size):
    # เริ่มเช็กซ้ายบนจาก 'K' ให้สุดก่อนว่ามี 'B' ไหม จากนั้นก็เช็กบนขวา, ล่างขวา, ล่างซ้าย ตามลำดับ
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for di_row, di_col in directions:
        row, col = king_row + di_row, king_col + di_col
        #ถ้าตำแหน่ง (row, col) มี 'B' หรือ 'Q' => king โดน check
        while 0 <= row < board_size and 0 <= col < board_size:
        # loop จนกว่าว่าตำแหน่งนั้นจะกินหรือออกนอกตาราง (0 <= row,col < board_size)
            piece = grid[row][col]
            if piece != '.':
                if piece in ('B', 'Q'):
                    return True
                break #ถ้าไม่ใช่ทั้ง 'B', 'Q' และ '.' แสดงว่ามีตัวอื่นบังอยู่ 'B' หรือ 'Q' ที่อาจอยู่ข้างหลังจะไม่สามารถกินได้ => ออกจาก loop เลย
            row += di_row
            col += di_col
    return False
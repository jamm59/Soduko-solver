board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
from time import sleep
def print_board(bd):
    for row in range(len(bd)):
        if row % 3 == 0 and row != 0:
            print('___________________________')

        for col in range(len(bd[0])):
            if col % 3 == 0 and col != 0:
                print('|',end='')

            if col == 8:
                print(f'{bd[row][col]}')
            else:
                print(f'{bd[row][col]}  ',end='')

print_board(board)
def find_empty(bd):
    for row in range(len(bd)):
        for col in range(len(bd[0])):
            if bd[row][col] == 0:
                return (row,col)
    return None

    
def is_valid(bd,num,pos):
    #check for row
    for col in range(len(bd[0])):
        if bd[pos[0]][col] == num and pos[1] != col:
            return False
    #check for column
    for row in range(len(bd)):
        if bd[row][pos[1]] == num and pos[0] != row:
            return False
    #check for box
    box_row =  pos[0] // 3 
    box_col =  pos[1] // 3
    
    for row in range(box_row * 3, box_row*3 + 3):
        for col in range(box_col * 3, box_col*3 + 3):
            if bd[row][col] == num and (row,col) != pos:
                return False

    return True

def solve(bd,count):
    find = find_empty(bd)
    if not find:
        print_board(bd)
        return True
    else:
        row,col = find

    print(f'solve {count}')
    count+= 1
    sleep(1)
    print_board(bd)
    for element in range(1,10):
        if is_valid(board,element,(row,col)):
            bd[row][col] = element

            if solve(bd,count):
                return True
            
            bd[row][col] = 0

# print('before')
# print_board(board)
# print('after')
solve(board,1)
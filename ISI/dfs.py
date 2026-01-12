from tile import NoChangedTile, ChangedTile
from time import sleep

def search_row_and_col(field, row, col):
    rows: int = 0
    for r in range(row, -1, -1):
        if isinstance(field[r, col], NoChangedTile):
            rows = r + 1
            break

    cols: int = 0
    for c in range(col, -1, -1):
        if isinstance(field[row, c], NoChangedTile):
            cols = c + 1
            break

    return rows, cols


def check(field, row, col, num):

    rows, cols = search_row_and_col(field, row, col)
    
    arr_row = [0] * (len(field)-1)
    i = 0
    for r in range(rows, len(field)):
        if isinstance(field[r, col], ChangedTile):
            arr_row[i] = field[r, col].result
            i+=1

    # print(f'sum_row = {sum(arr_row)}, {i}')
    if num in arr_row:
        return False

    arr_col = [0] * (len(field)-1)
    j = 0
    for c in range(cols, len(field)):
        if isinstance(field[row, c], ChangedTile):
            arr_col[j] = field[row, c].result
            j+=1

    if num in arr_col:
        return False
    # print(f'{row} = {max_r}')

    return True




def dfs(field, row, col, rows, cols):
    if col == cols:
        if field.win():
            return True
        return False

    field.write_field()

    next_row = row
    next_col = col
    if row < rows-1:
        next_row = row + 1
    elif col < cols:
        next_row = 0
        next_col = col + 1


    if isinstance(field.field[row, col], NoChangedTile):
        return dfs(field, next_row, next_col, rows, cols)

    for num in range(1, 10):
        if check(field.field, row, col, num):
            field.field[row, col].result = num
            field.write_field()
            if dfs(field, next_row, next_col, rows, cols):
                return True
            field.field[row, col].result = 0

    return False
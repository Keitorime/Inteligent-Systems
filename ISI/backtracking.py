
from tile import NoChangedTile, ChangedTile

def search_row_and_col(field, rows, cols):
    row: int = 0
    for r in range(rows, -1, -1):
        if isinstance(field[r, cols], NoChangedTile):
            row = r + 1
            break

    max_row: int = 0
    for r in range(row, len(field)):
        if isinstance(field[r, cols], NoChangedTile):
            max_row = r - 1
            break
        max_row = r

    col: int = 0
    for c in range(cols, -1, -1):
        if isinstance(field[rows, c], NoChangedTile):
            col = c + 1
            break

    max_col: int = 0
    for c in range(col, len(field)):
        if isinstance(field[rows, c], NoChangedTile):
            max_col = c - 1
            break
        max_col = c

    return row, max_row, col, max_col


def check(field, row, col, num):

    rows, max_r, cols, max_c = search_row_and_col(field, row, col)

    arr_row = [0] * (max_r - rows + 1)
    i = 0
    for r in range(rows, max_r+1):
        if isinstance(field[r, col], ChangedTile):
            arr_row[i] = field[r, col].result
            i+=1


    if num in arr_row:
        return False

    arr_col = [0] * (max_c - cols + 1)
    j = 0
    for c in range(cols, max_c + 1):
        if isinstance(field[row, c], ChangedTile):
            arr_col[j] = field[row, c].result
            j+=1

    if num in arr_col:
        return False

    #print(f'{row} = {rows}, {max_r}')
    #print(f'{col} = {cols}, {max_c}')

    #print(num)
    if row == max_r:
        #print(f'field[{rows-1},{col}].vertical[{field[rows-1, col].vertical}] != {sum(arr_row)+num}')
        # sleep(1)
        if field[rows-1, col].vertical != sum(arr_row)+num:
            return False

    if col == max_c:
        #print(f'field[{row},{cols-1}].horizontal[{field[row, cols-1].horizontal}] != {sum(arr_col)+num}')
        if field[row, cols-1].horizontal != sum(arr_col)+num:
            return False




    return True




def backtraking(field, row, col, rows, cols):
    if col == cols:
        return True

    # field.write_field()
    # sleep(1)
    next_row = row
    next_col = col
    if row < rows-1:
        next_row = row + 1
    elif col < cols:
        next_row = 0
        next_col = col + 1


    if isinstance(field.field[row, col], NoChangedTile):
        return backtraking(field, next_row, next_col, rows, cols)

    for num in range(1, 10):
        if check(field.field, row, col, num):
            field.field[row, col].result = num
            field.write_field()
            if backtraking(field, next_row, next_col, rows, cols):
                return True
            field.field[row, col].result = 0

    return False
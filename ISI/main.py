#from KakuroGUI import KakuroGUI
from GUIFULL import KakuroGUI
from backtracking import backtraking
from field import Field
import tkinter as tk
from visualization import ArrayGridVisualizer
from dfs import dfs, check
from time import sleep









if __name__ == '__main__':
    # rows = 5
    # cols = 5
    #
    # field = Field(rows, cols)
    # win = True
    # # while win:
    # #field.generate()
    # field.write_field_custome_1_4x4()
    # field.write_field()
    # # sleep(10)
    # # print(check(field.field, 3, 4))
    # #dfs(field, 1, 1, rows, cols)
    # backtraking(field, 1, 1, rows, cols)
    # field.write_field()
    # win = field.win()
    #
    # if win:
    #     print("You Win!")
    # else:
    #     print("You Lose!")
    # app = KakuroGUI(field)
    # app.backtracking()

    app = KakuroGUI(Field(3, 3))  # Початкове поле буде 3x3
    app.window.mainloop()

    # print("You Win!")

    # root = tk.Tk()
    # root.title("Grid Array Visualization")
    # visualizer = ArrayGridVisualizer(root, field, 5, 5)
    # root.mainloop()
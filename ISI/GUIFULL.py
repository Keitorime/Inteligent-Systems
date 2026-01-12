import timeit
import tkinter as tk
from field import Field
from backtracking import backtraking
from field import Field
from forward_checking import forward_checking
from tile import NoChangedTile, ChangedTile
from dfs import dfs

class KakuroGUI:
    def __init__(self, field):
        self.field = field
        self.window = tk.Tk()
        self.window.title("Kakuro Solver")
        self.window.geometry("800x600")

        self.rows = len(field.field)
        self.cols = len(field.field[0])
        self.grid = []

        # Додано меню для вибору алгоритму і рівня
        self.create_menu()

        # Додано прокручувану область для відображення сітки
        self.canvas = tk.Canvas(self.window, width=500, height=400)
        self.scroll_y = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.scroll_x = tk.Scrollbar(self.window, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        # Використовуємо grid для розташування елементів
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Створення сітки на полотні
        self.grid_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.grid_frame, anchor="nw")
        self.grid_frame.bind(
            "<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.create_grid()

    def create_menu(self):
        """Створення меню для вибору алгоритму та рівня"""
        menu_frame = tk.Frame(self.window)
        menu_frame.grid(row=2, column=0, columnspan=self.cols)

        self.algorithm_var = tk.StringVar(value="dfs")
        self.level_var = tk.StringVar(value="3x3")

        # Меню вибору алгоритму
        algorithm_label = tk.Label(menu_frame, text="Select Algorithm:")
        algorithm_label.grid(row=0, column=0, padx=5, pady=5)

        algorithm_menu = tk.OptionMenu(menu_frame, self.algorithm_var, "dfs", "backtracking", "forward checking")
        algorithm_menu.grid(row=0, column=1, padx=5, pady=5)

        # Меню вибору рівня
        level_label = tk.Label(menu_frame, text="Select Level:")
        level_label.grid(row=1, column=0, padx=5, pady=5)

        level_menu = tk.OptionMenu(menu_frame, self.level_var, "3x3", "4x4", "1_5x5","2_5x5","8x8", "wrong")
        level_menu.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка для запуску алгоритму
        start_button = tk.Button(menu_frame, text="Start", command=self.run_algorithm)
        start_button.grid(row=1, column=2, padx=5, pady=5)

    def create_grid(self):
        """Створення сітки для відображення масиву в Tkinter"""
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                value = ""
                style = {"width": 5, "height": 2, "relief": "solid", "anchor": "center"}

                # Перевіряємо, чи є сума (horizontal або vertical)
                if isinstance(self.field.field[i, j], NoChangedTile):  # Чорна клітинка
                    value = "#"
                    style["bg"] = "black"
                    style["fg"] = "white"  # Білі числа на чорному фоні
                    style["font"] = ("Arial", 12, "bold")  # Жирний шрифт
                elif isinstance(self.field.field[i, j], ChangedTile):  # Клітинка, яку можна змінити
                    value = self.field.field[i, j].result
                    style["bg"] = "white"
                    style["fg"] = "black"
                elif self.field.field[i, j] is not None:  # Якщо клітинка не є None
                    # Якщо є вертикальна сума
                    if self.field.field[i, j].vertical is not None:
                        value = str(self.field.field[i, j].vertical)
                    # Якщо є горизонтальна сума
                    elif self.field.field[i, j].horizontal is not None:
                        value = str(self.field.field[i, j].horizontal)

                # Створення мітки для кожної клітинки
                label = tk.Label(self.grid_frame, text=value, **style)
                label.grid(row=i, column=j, padx=1, pady=1)  # Додано невеликі відступи для кращого вигляду
                row.append(label)

            # Додаємо рядок до загальної сітки
            self.grid.append(row)

    def update_grid(self):
        """Оновлення сітки після зміни значень"""
        for i in range(self.rows):
            for j in range(self.cols):
                tile = self.field.field[i, j]

                # Якщо клітинка має значення (число)
                if isinstance(tile, ChangedTile):
                    value = tile.result
                # Якщо клітинка містить вертикальну або горизонтальну суму
                elif isinstance(tile, NoChangedTile):
                    value = ""
                    # Перевірка на наявність горизонтальної суми
                    if tile.horizontal is not None and tile.horizontal != 0:
                        value += str(tile.horizontal)  # Додаємо горизонтальну суму
                    # Перевірка на наявність вертикальної суми
                    if tile.vertical is not None and tile.vertical != 0:
                        if value:
                            value += "\n"  # Додаємо розрив рядка, якщо вже є горизонтальна сума
                        value += str(tile.vertical)  # Додаємо вертикальну суму
                    if not value:
                        value = "#"  # Якщо сум немає, ставимо "#"
                else:
                    value = "#"

                # Оновлюємо текст в клітинці
                self.grid[i][j].config(text=value)

    def run_algorithm(self):
        """Запуск вибраного алгоритму і оновлення інтерфейсу"""
        selected_algorithm = self.algorithm_var.get()
        selected_level = self.level_var.get()

        # Визначення розміру поля за рівнем
        if selected_level == "3x3":
            rows, cols = 3, 3
        elif selected_level == "4x4":
            rows, cols = 4, 4
        elif selected_level == "1_5x5":
            rows, cols = 5, 5
        elif selected_level == "wrong":
            rows, cols = 3, 3
        elif selected_level == "2_5x5":
            rows, cols = 5, 5
        elif selected_level == "8x8":
            rows, cols = 8, 8

        # Оновлення поля тільки після зміни розміру
        self.field = Field(rows, cols)  # Створюємо нове поле з новими розмірами

        # Генерація поля для нового рівня
        if selected_level == "3x3":
            self.field.write_field_custome3x3()
        elif selected_level == "4x4":
            self.field.write_field_custome_1_4x4()
        elif selected_level == "1_5x5":
            self.field.write_field_custome_1_5x5()
        elif selected_level == "wrong":
            self.field.write_field_custome_wrong()
        elif selected_level == "2_5x5":
            self.field.write_field_custome_2_5x5()
        elif selected_level == "8x8":
            self.field.write_field_custome_8x8()

        # Запуск алгоритму
        solved = False
        if selected_algorithm == "dfs":
            print("Starting dfs...")
            solved = dfs(self.field, 0, 0, rows, cols)
            execution_time = timeit.timeit(lambda: dfs(self.field, 1, 1, rows, cols), number=1)
            print(execution_time)

        if selected_algorithm == "backtracking":
            print("Starting backtracking...")
            #solved = backtraking(self.field, 0, 0, rows, cols)
            execution_time = timeit.timeit(lambda: backtraking(self.field, 1, 1, rows, cols), number=1)
            print(execution_time)
            win = self.field.win()


        if selected_algorithm == "forward checking":
            print("Starting forward checking...")
            #solved = forward_checking(self.field, 0, 0, rows, cols)
            execution_time = timeit.timeit(lambda: forward_checking(self.field, 1, 1, rows, cols), number=1)
            print(execution_time)

        # Оновлення розмірів сітки
        self.rows = rows
        self.cols = cols

        # Очищення попередніх елементів
        for row in self.grid:
            for label in row:
                label.destroy()

        # Оновлення сітки
        self.grid.clear()
        self.create_grid()
        self.update_grid()  # Оновлюємо відображення масиву

        # Відображення результату
        result_message = f"Win" if self.field.win() else "Lose"
        result_label = tk.Label(self.window, text=f"Result: {result_message}", font=("Arial", 16),
                                fg="green" if self.field.win() else "red")
        result_label.grid(row=3, column=0, columnspan=self.cols, pady=10)

if __name__ == '__main__':

    app = KakuroGUI(Field(3, 3))  # Початкове поле буде 3x3
    app.window.mainloop()
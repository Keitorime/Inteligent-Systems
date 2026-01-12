import tkinter as tk
import random

from tile import ChangedTile, NoChangedTile


class ArrayGridVisualizer:
    def __init__(self, root, array, rows, cols):
        self.rows, self.cols = rows, cols
        self.root = root
        self.array = array
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()
        self.cell_size = 600 // rows*cols
        self.draw_grid()
        self.fill_grid()

    def draw_grid(self):
        # Малюємо сітку
        n = self.rows * self.cols
        for i in range(n + 1):
            # Горизонтальні лінії
            self.canvas.create_line(0, i * self.cell_size, 600, i * self.cell_size, fill="lightgray")
            # Вертикальні лінії
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, 600, fill="lightgray")

    def fill_grid(self):
        # Розставляємо значення з масиву в клітинках
        for i in range(self.rows):
            for j in range(self.cols):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # Малюємо текст у центрі клітинки
                if isinstance(self.array.field[i,j], ChangedTile):
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(self.array.field[i,j].result), fill="black", font=("Arial", 14))
                elif isinstance(self.array.field[i,j], NoChangedTile):
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(str(self.array.field[i,j].vertical) + ',' + str(self.array.field[i,j].horizontal)), fill="black", font=("Arial", 14))
# Генеруємо випадковий масив розміру n x n
n = 10
array = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]



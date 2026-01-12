import random
from dataclasses import field

import numpy as np
from tile import NoChangedTile, ChangedTile


class Field:
    def __init__(self, rows, cols):
        self.field = np.full((rows, cols), None)
        self.fake_field = np.full((rows, cols), None)
        self.rows = rows
        self.cols = cols
        self.loop = 0

    def generate(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        # Рандомно розставляємо чорні клітинки
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if random.random() < 0.4:
                    self.field[i,j] = NoChangedTile(i,j,False)

        # Розставляємо білі клітинки
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i,j] is None:
                    self.field[i,j] = ChangedTile(i,j)

        # Перевіряємо чи немає білої клітинки яку легко відгадати (бо вона закрита з двох сторін чорними клітинками)
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if i < self.rows-1 and isinstance(self.field[i-1,j], NoChangedTile)  and isinstance(self.field[i+1,j],NoChangedTile) and isinstance(self.field[i,j],ChangedTile):
                    self.field[i+1,j] = ChangedTile(i+1,j)
                elif i == self.rows-1 and isinstance(self.field[i-1,j], NoChangedTile)  and isinstance(self.field[i,j],ChangedTile):
                    self.field[i-1,j] = ChangedTile(i-1,j)
                if j < self.cols-1 and isinstance(self.field[i,j-1], NoChangedTile)  and isinstance(self.field[i,j+1],NoChangedTile) and isinstance(self.field[i,j],ChangedTile):
                    self.field[i,j+1] = ChangedTile(i,j+1)
                elif j == self.cols-1 and isinstance(self.field[i,j-1], NoChangedTile)  and isinstance(self.field[i,j],ChangedTile):
                    self.field[i,j-1] = ChangedTile(i,j-1)

        # Цикл для заповнення матриці
        loop = True
        while loop:
            loop = False

            # Рандомно розкладаємо значення на матриці
            for i in range(self.rows):
                for j in range(self.cols):
                    if isinstance(self.field[i,j], ChangedTile):
                        self.field[i,j].result = random.randint(1, 9)

            # Перевіряємо чи нормально розставлені числа в стовпчиках і чи не має однакових чисел
            for i in range(self.rows):
                for j in range(self.cols):
                    if i < self.rows-1 and isinstance(self.field[i,j], NoChangedTile) and isinstance(self.field[i+1,j],ChangedTile):
                        arr = []
                        for k in range(i+1, self.rows):
                            if isinstance(self.field[k,j], NoChangedTile):
                                break
                            elif self.field[k, j].result in arr:
                                loop = True
                            arr.append(self.field[k, j].result)

                        # Записуємо суму стовпчиків
                        self.field[i,j].vertical = sum(arr)

            # Перевіряємо чи нормально розставлені числа в рядках і чи не має однакових чисел
            for i in range(self.rows):
                for j in range(self.cols):
                    if j < self.cols-1 and isinstance(self.field[i,j], NoChangedTile) and isinstance(self.field[i,j+1],ChangedTile):
                        arr = []
                        for k in range(j+1, self.cols):
                            if isinstance(self.field[i,k], NoChangedTile):
                                break
                            elif self.field[i, k].result in arr:
                                loop = True
                            arr.append(self.field[i, k].result)

                        # Записуємо суму рядків
                        self.field[i, j].horizontal = sum(arr)
        self.fake_field = self.field
        self.write_field()

        for i in range(self.rows):
            for j in range(self.cols):
                if isinstance(self.field[i,j], ChangedTile):
                    self.field[i,j].result = 0
                    # pass





    def write_field_custome_1_5x5(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i,j] is None:
                    self.field[i,j] = ChangedTile(i,j)


        self.field[4, 3] = NoChangedTile(5, 1, False)
        self.field[4, 4] = NoChangedTile(5, 2, False)
        self.field[1, 2] = NoChangedTile(1, 2, True)
        self.field[1, 1] = NoChangedTile(1, 2, True)

        self.field[0, 3].vertical = 6
        self.field[0, 4].vertical = 23
        self.field[1, 1].vertical = 7
        self.field[1, 2].vertical = 6
        self.field[1, 2].horizontal = 11
        self.field[2, 0].horizontal = 15
        self.field[3, 0].horizontal = 12
        self.field[4, 0].horizontal = 4

    def write_field_custome_2_5x5(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i,j] is None:
                    self.field[i,j] = ChangedTile(i,j)


        self.field[3, 1] = NoChangedTile(3, 1, True)
        self.field[4, 1] = NoChangedTile(4, 1, True)
        self.field[1, 4] = NoChangedTile(1, 4, False)
        self.field[2, 4] = NoChangedTile(2, 4, True)

        self.field[0, 1].vertical = 16
        self.field[0, 2].vertical = 11
        self.field[0, 3].vertical = 29
        self.field[1, 0].horizontal = 19
        self.field[2, 0].horizontal = 14
        self.field[3, 1].horizontal = 14
        self.field[4, 1].horizontal = 12
        self.field[2, 4].vertical = 3

    def write_field_custome3x3(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i,j] is None:
                    self.field[i,j] = ChangedTile(i,j)


        self.field[0, 1].vertical = 4
        self.field[0, 2].vertical = 3
        self.field[1, 0].horizontal = 4
        self.field[2, 0].horizontal = 3

    def write_field_custome_wrong(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i,j] is None:
                    self.field[i,j] = ChangedTile(i,j)


        self.field[0, 1].vertical = 5
        self.field[0, 2].vertical = 3
        self.field[1, 0].horizontal = 4
        self.field[2, 0].horizontal = 3


    def write_field_custome_1_4x4(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i, j] is None:
                    self.field[i, j] = ChangedTile(i, j)

        self.field[0, 1].vertical = 23
        self.field[0, 2].vertical = 20
        self.field[0, 3].vertical = 7
        self.field[1, 0].horizontal = 20
        self.field[2, 0].horizontal = 19
        self.field[3, 0].horizontal = 11

    def write_field_custome_8x8(self):
        self.loop = 0
        # Розставляємо чорні клітинки з ліва
        for i in range(self.rows):
            self.field[i, 0] = NoChangedTile(i, 0, False)

        # Розставляємо чорні клітинки з веру
        for j in range(self.cols):
            self.field[0, j] = NoChangedTile(0, j, False)

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if self.field[i, j] is None:
                    self.field[i, j] = ChangedTile(i, j)

        self.field[1, 3] = NoChangedTile(1, 3, False)
        self.field[2, 3] = NoChangedTile(2, 3, True)
        self.field[1, 4] = NoChangedTile(1, 4, True)
        self.field[4, 1] = NoChangedTile(4, 1, True)
        self.field[5, 1] = NoChangedTile(5, 1, True)
        self.field[5, 2] = NoChangedTile(5, 2, True)
        self.field[7, 4] = NoChangedTile(7, 4, False)
        self.field[6, 5] = NoChangedTile(6, 5, True)
        self.field[7, 5] = NoChangedTile(7, 5, True)
        self.field[4, 4] = NoChangedTile(4, 4, True)
        self.field[3, 6] = NoChangedTile(3, 6, True)
        self.field[3, 7] = NoChangedTile(3, 7, False)
        self.field[4, 7] = NoChangedTile(4, 7, True)

        self.field[0, 1].vertical = 23
        self.field[0, 2].vertical = 30
        self.field[0, 5].vertical = 27
        self.field[0, 6].vertical = 12
        self.field[0, 7].vertical = 16
        self.field[1, 0].horizontal = 16
        self.field[2, 0].horizontal = 17
        self.field[3, 0].horizontal = 35
        self.field[6, 0].horizontal = 21
        self.field[7, 0].horizontal = 6
        self.field[2, 3].vertical = 15
        self.field[1, 4].vertical = 17
        self.field[5, 1].vertical = 11
        self.field[5, 2].vertical = 10
        self.field[4, 4].vertical = 7
        self.field[3, 6].vertical = 12
        self.field[4, 7].vertical = 7
        self.field[1, 4].horizontal = 24
        self.field[2, 3].horizontal = 29
        self.field[4, 1].horizontal = 7
        self.field[4, 4].horizontal = 8
        self.field[5, 2].horizontal = 16
        self.field[6, 5].horizontal = 5
        self.field[7, 5].horizontal = 3





    def write_field(self):
        self.loop = self.loop + 1
        for row in range(self.rows):
            for col in range(self.cols):
                if isinstance(self.field[row, col], ChangedTile):
                    print(self.field[row, col].result, end=" ")
                elif isinstance(self.field[row, col], NoChangedTile):
                    print("#", end=" ")
                else:
                    print(self.field[row, col], end=" ")

            print(" ")
        print()

    def win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if row < self.rows-1 and isinstance(self.field[row,col], NoChangedTile) and isinstance(self.field[row+1,col],ChangedTile):
                        arr = []
                        for k in range(row+1, self.rows):
                            if isinstance(self.field[k,col], NoChangedTile):
                                break
                            elif self.field[k, col].result in arr:
                                return False
                            arr.append(self.field[k, col].result)

                        if self.field[row,col].vertical != sum(arr):
                            return False

        for row in range(self.rows):
            for col in range(self.cols):
                if col < self.cols-1 and isinstance(self.field[row,col], NoChangedTile) and isinstance(self.field[row,col+1],ChangedTile):
                        arr = []
                        for k in range(col+1, self.cols):
                            if isinstance(self.field[row,k], NoChangedTile):
                                break
                            elif self.field[row, k].result in arr:
                                return False
                            arr.append(self.field[row, k].result)

                        if self.field[row, col].horizontal != sum(arr):
                            return False
        print(f"Loop = {self.loop}")
        self.loop = 0
        return True


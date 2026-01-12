
Depth-First Search (DFS)
In our code, DFS is implemented in such a way that the algorithm fills numbers starting from position (1,1), then descends to the bottom of the column and moves to the next one. This process continues until the last cell is reached.
Before assigning a value from 1 to 9, the algorithm checks whether the number already exists in the current row or column to avoid duplicates. If the number is not present, the cell is assigned this value. If the value is incorrect or all possible values have been tried, the algorithm returns False, causing a full backtrack to the first cell, ensuring that every cell is checked.
This algorithm is relatively slow because it iterates through all possible values and traverses every loop until the very end.
________________________________________
Backtracking
In our code, backtracking is implemented by filling numbers starting from position (1,1), then descending to the bottom of the column and moving to the next one. At the end of each column, the algorithm checks whether the sum of the values in the column matches the required sum.
Before assigning a value from 1 to 9, the algorithm verifies that the number does not already appear in the row or column, thus preventing duplicates. If the algorithm is processing the last column, it additionally checks whether the sum of the values matches the required sum.
If the values in the grid do not match the constraints, the algorithm backtracks to the previous cell and continues this process until a valid column is completed. If a value is invalid or all possible values have been exhausted, the algorithm returns False and backtracks to the first cell of the column, ensuring that every cell in the column is examined.
This algorithm is significantly faster than DFS and performs efficiently. It is well suited for solving large grids.


________________________________________
Forward Checking
In our code, forward checking is implemented by filling numbers starting from position (1,1), then descending to the bottom of the column and moving to the next one. At the end of each column, the algorithm checks whether the sum of the values in the column matches the required sum.
Before assigning a value, all possible candidate values for the required sum are determined. The algorithm retrieves all valid possibilities for a cell and iterates through them until a suitable value is found. It then checks whether the value already exists in the row or column to avoid duplicates. If the algorithm is processing the last column, the column sum is compared with the required sum.
If the grid values do not satisfy the constraints, the algorithm backtracks to the previous cell and continues this process until a valid column is formed. If a value is invalid or all possible values have been tried, the algorithm returns False and backtracks to the first cell of the column, ensuring that every cell in the column is checked.
Under normal circumstances, when correctly implemented, this method is the fastest. However, in our case, since the elimination of already used values is not implemented, the algorithm runs slightly slower than expected.
________________________________________












                                                       Comparison Table

	3x3	4x4	1_5x5	2_5x5	8x8	wrong
DFS      Time:	0,0395	Several hours	-	-	-	0.4591
Iterations:	534	Thousands	-	-	-	-
Backtracking Time: 	0.000494	0.04713	0.1107722	0.176592	11.0093	0.0011
Iterations:	8	660	453	763	22215	-
Forward Checking Time:	0.00037	0.07929	0.0137185	0.0362681	-	0.0005
Iterations:	6	1047	65	137	-	-

We tested three methods on different grid sizes. We decided not to test the DFS method on larger grids, as even a 4×4 grid requires hours of computation time. On an 8×8 grid, forward checking resulted in an infinite loop due to a minor implementation issue.


import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            temp_list = []
            for j in range(self.num_cols):
                cell = Cell(self.win)
                temp_list.append(cell)
            self._cells.append(temp_list)
        for columns in self._cells:
            for c in columns:
                self._draw_cell(self._cells.index(columns), columns.index(c))
    
    def _draw_cell(self, i, j):
        #print(i, j)
        x1 = j*self.cell_size_x + self.x1
        y1 = i*self.cell_size_y + self.y1
        x2 = j*self.cell_size_x + self.cell_size_x + self.x1
        y2 = i*self.cell_size_y + self.cell_size_y + self.y1
        self._cells[i][j].draw(x1, x2, y1, y2)
        #c.draw(x1, x2, y1, y2)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

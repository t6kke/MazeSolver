import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = window
        self._cells = []
        self._create_cells()
        #self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            temp_list = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                temp_list.append(cell)
            self._cells.append(temp_list)
        for columns in self._cells:
            for c in columns:
                self._draw_cell(self._cells.index(columns), columns.index(c))
        #TODO improve when the entrance and exit are set to false
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        #not boot.dev method of making maze entrance and exit, they recommend using "_break_entrance_and_exit" function.
        #not using it since it might cause problems in the future of the project
        if i == 0 and j == 0:
            self._cells[i][j].has_top_wall = False
        if i == self.num_cols-1 and j == self.num_rows-1:
            self._cells[i][j].has_bottom_wall = False

        x1 = i*self.cell_size_x + self.x1
        y1 = j*self.cell_size_y + self.y1
        x2 = i*self.cell_size_x + self.cell_size_x + self.x1
        y2 = j*self.cell_size_y + self.cell_size_y + self.y1
        print(i, j, x1, x2, y1, y2, self._cells[i][j].has_top_wall ,self._cells[i][j].has_bottom_wall)
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

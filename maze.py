import time
import random
from random import randrange
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = window
        self._cells = []
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)
        self._create_cells()
        #self._break_entrance_and_exit()
        #self._break_walls_r(0,0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        for i in range(self.num_cols):
            temp_list = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                temp_list.append(cell)
            self._cells.append(temp_list)
        #self._break_entrance_and_exit()
        self._break_walls_r(0,0)
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
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        #print(i, j , self._cells)
        #print(i, j, self._cells[i][max(0,j-1)].visited)
        #print(i, j, self._cells[min(self.num_cols-1,i+1)][j].visited)
        #print(i, j, self._cells[i][min(self.num_rows-1,j+1)].visited)
        #print(i, j, self._cells[max(0,i-1)][j].visited)
        while True:
            temp_list = []
            if self._cells[i][max(0,j-1)].visited == False: #top
                temp_list.append([i,max(0,j-1),0])
            if self._cells[min(self.num_cols-1,i+1)][j].visited == False: #left
                temp_list.append([min(self.num_cols-1,i+1),j,1])
            if self._cells[i][min(self.num_rows-1,j+1)].visited == False: #bottom
                temp_list.append([i,min(self.num_rows-1,j+1),2])
            if self._cells[max(0,i-1)][j].visited == False: #right
                temp_list.append([max(0,i-1),j,3])
                
            #print(temp_list)
            if len(temp_list) == 0:
                #boot.dev asks to draw cell but because I'm calling this funtion not from initilization but when after creating cells and before actually drawing them I don't need to draw anything here.
                return
            rand_dir = randrange(len(temp_list))
            next_cell = temp_list[rand_dir]
            #print("Im at cell:", i, j, "--- options:", temp_list, "--- roll index:", rand_dir, "--- moving to val:",next_cell[2], "--- cell:", next_cell[0], next_cell[1])
            if next_cell[2] == 0:
                #topgit 
                #print("moving top", next_cell)
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            elif next_cell[2] == 1:
                #left
                #print("moving right", next_cell)
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            elif next_cell[2] == 2:
                #bottom
                #print("moving bottom", next_cell)
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            elif next_cell[2] == 3:
                #right
                #print("moving left", next_cell)
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            self._break_walls_r(next_cell[0],next_cell[1])

    def _reset_cells_visited(self):
        for columns in self._cells:
            for cell in columns:
                cell.visited = False

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
        #print(i, j, x1, x2, y1, y2, self._cells[i][j].has_top_wall ,self._cells[i][j].has_bottom_wall, self._cells[i][j].visited)
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

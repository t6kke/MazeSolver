from window import Line, Point

class Cell:
    def __init__(self, window, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            lef_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(lef_line)
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line)
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line)
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line)
    
    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        half_height = abs(self._y2 - self._y1) // 2
        line_color = ""
        if undo == False:
            line_color = "red"
        else:
            line_color = "gray"
        line = Line(Point(self._x1+half_length, self._y1+half_height), Point(to_cell._x1+half_length, to_cell._y1+half_height))
        self._win.draw_line(line, line_color)

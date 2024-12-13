from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    #test_draw_line(win)
    #test_draw_boxes(win)
    #test_draw_linebetweenboxes(win)
    test_draw_maze(win)
    win.wait_for_close()

def test_draw_line(win):
    n_line = Line(Point(50, 30), Point(400, 380))
    win.draw_line(n_line, "red")

def test_draw_boxes(win):
    cell = Cell(win)
    cell.draw(50, 100, 50, 100)

    cell = Cell(win, has_left_wall = False)
    cell.draw(150, 200, 100, 150)

    cell = Cell(win, has_top_wall = False)
    cell.draw(200, 150, 400, 450)

    cell = Cell(win, has_right_wall = False)
    cell.draw(200, 250, 300, 350)

    cell = Cell(win, has_bottom_wall = False)
    cell.draw(300, 350, 300, 350)

    cell = Cell(win, has_bottom_wall = False, has_top_wall = False)
    cell.draw(600, 650, 300, 350)

    cell = Cell(win, has_left_wall = False, has_right_wall = False)
    cell.draw(600, 650, 100, 150)

def test_draw_linebetweenboxes(win):
    cell_01 = Cell(win)
    cell_01.draw(50, 100, 50, 100)
    cell_02 = Cell(win)
    cell_02.draw(100, 150, 50, 100)
    cell_01.draw_move(cell_02)

    cell_03 = Cell(win)
    cell_03.draw(150, 200, 250, 300)
    cell_04 = Cell(win)
    cell_04.draw(100, 150, 250, 300)
    cell_03.draw_move(cell_04, undo=True)

def test_draw_maze(win):
    maze = Maze(10, 10, 10, 15, 50, 50, win)
    #maze = Maze(10, 10, 10, 10, 60, 40, win)
    #maze = Maze(10, 10, 100, 100, 5, 5, win)

main()
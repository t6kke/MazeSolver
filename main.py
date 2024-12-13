from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    #test_draw_line(win)
    test_draw_boxes(win)
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

main()
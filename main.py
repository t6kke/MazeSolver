from window import Window, Line, Point

def main():
    win = Window(800, 600)
    n_line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(n_line, "red")
    win.wait_for_close()


main()
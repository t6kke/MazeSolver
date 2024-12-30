import unittest
from maze import Maze

class Tests(unittest.TestCase):

    #boot.dev example test case
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    #boot.dev resolution tests
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    #my custom tests
    def test_maze_create_cells_01(self):
        columns = 1
        rows = 1
        maze = Maze(0, 0, rows, columns, 10, 10)
        self.assertEqual(
            len(maze._cells),
            columns,
        )
        self.assertEqual(
            len(maze._cells[0]),
            rows,
        )
    
    def test_maze_create_cells_02(self):
        columns = 10
        rows = 20
        maze = Maze(0, 0, rows, columns, 10, 10)
        self.assertEqual(
            len(maze._cells),
            columns,
        )
        self.assertEqual(
            len(maze._cells[0]),
            rows,
        )
    
    def test_maze_cells_visited_01(self):
        columns = 10
        rows = 20
        maze = Maze(0, 0, rows, columns, 10, 10)
        self.assertEqual(
            maze._cells[0][0].visited, False,
        )
    
    def test_maze_cells_visited_02(self):
        columns = 10
        rows = 20
        maze = Maze(0, 0, rows, columns, 10, 10)
        for columns in maze._cells:
            for cell in columns:
                self.assertEqual(
                    cell.visited, False,
                )

if __name__ == "__main__":
    unittest.main()

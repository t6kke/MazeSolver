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
        columns = 100
        rows = 1000
        maze = Maze(0, 0, rows, columns, 10, 10)
        self.assertEqual(
            len(maze._cells),
            columns,
        )
        self.assertEqual(
            len(maze._cells[0]),
            rows,
        )

if __name__ == "__main__":
    unittest.main()

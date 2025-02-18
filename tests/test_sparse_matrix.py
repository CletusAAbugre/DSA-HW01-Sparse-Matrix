import unittest
from src.sparse_matrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        """Set up a sample sparse matrix for testing."""
        self.matrix = SparseMatrix(3, 3)
        self.matrix.insert(0, 1, 5)
        self.matrix.insert(2, 2, 10)

    def test_insert_and_get(self):
        """Test inserting and retrieving values."""
        self.assertEqual(self.matrix.get(0, 1), 5)
        self.assertEqual(self.matrix.get(2, 2), 10)
        self.assertEqual(self.matrix.get(1, 1), 0)  # Empty cell

    def test_display(self):
        """Test if the display function prints correctly."""
        expected_output = "[0, 5, 0]\n[0, 0, 0]\n[0, 0, 10]\n"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.matrix.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_transpose(self):
        """Test transposing the sparse matrix."""
        transposed = self.matrix.transpose()
        self.assertEqual(transposed.get(1, 0), 5)
        self.assertEqual(transposed.get(2, 2), 10)
        self.assertEqual(transposed.get(0, 1), 0)  # Should be empty after transpose

if __name__ == "__main__":
    unittest.main()



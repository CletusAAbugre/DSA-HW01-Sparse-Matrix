import unittest
from src.sparse_matrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        """Initialize test matrices"""
        self.matrix1 = SparseMatrix(3, 3)
        self.matrix2 = SparseMatrix(3, 3)

        self.matrix1.insert(0, 1, 5)
        self.matrix1.insert(2, 2, 10)

        self.matrix2.insert(0, 1, 3)
        self.matrix2.insert(2, 2, 2)

    def test_addition(self):
        """Test matrix addition."""
        result = self.matrix1.add(self.matrix2)
        expected_values = {(0, 1): 8, (2, 2): 12}
        self.assertEqual(result.data, expected_values)

    def test_subtraction(self):
        """Test matrix subtraction."""
        result = self.matrix1.subtract(self.matrix2)
        expected_values = {(0, 1): 2, (2, 2): 8}
        self.assertEqual(result.data, expected_values)

    def test_multiplication(self):
        """Test matrix multiplication."""
        result = self.matrix1.multiply(self.matrix2)
        self.assertIsInstance(result, SparseMatrix)

    def test_invalid_operations(self):
        """Test operations with incompatible matrices."""
        matrix3 = SparseMatrix(2, 2)
        with self.assertRaises(ValueError):
            self.matrix1.add(matrix3)

if __name__ == "__main__":
    unittest.main()










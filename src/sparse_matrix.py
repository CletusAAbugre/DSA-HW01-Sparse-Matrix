class SparseMatrix:
    def __init__(self, rows, cols):
        """Initialize a sparse matrix with given rows and columns."""
        self.rows = rows
        self.cols = cols
        self.data = {}  # Store non-zero elements in a dictionary

    def insert(self, row, col, value):
        """Insert a value at a specific row and column."""
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]  # Remove if value is zero

    def get(self, row, col):
        """Retrieve a value from the matrix."""
        return self.data.get((row, col), 0)

    def display(self):
        """Display the full matrix in dense format."""
        for i in range(self.rows):
            row_data = [self.get(i, j) for j in range(self.cols)]
            print(row_data)

    def transpose(self):
        """Return a new transposed matrix."""
        transposed = SparseMatrix(self.cols, self.rows)
        for (i, j), value in self.data.items():
            transposed.insert(j, i, value)
        return transposed



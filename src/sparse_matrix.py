class SparseMatrix:
    def __init__(self, rows, cols):
        """Initialize an empty sparse matrix."""
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store (row, col) -> value

    def insert(self, row, col, value):
        """Insert a value into the matrix."""
        if value != 0:
            self.data[(row, col)] = value

    def display(self):
        """Prints the sparse matrix in a readable format."""
        print("Sparse Matrix:")
        for r in range(self.rows):
            row_values = []
            for c in range(self.cols):
                row_values.append(str(self.data.get((r, c), 0)))
            print(" ".join(row_values))

    @classmethod
    def from_file(cls, file_path):
        """Load a sparse matrix from a file, handling encoding issues."""
        try:
            with open(file_path, "r", encoding="utf-8-sig") as file:
                lines = file.readlines()

            rows, cols = None, None

            for line in lines:
                line = line.strip()
                if line.startswith("rows="):
                    rows = int(line.split("=")[1].strip())
                elif line.startswith("cols="):
                    cols = int(line.split("=")[1].strip())

            if rows is None or cols is None:
                raise ValueError("❌ Invalid file format: Missing row or column information.")

            matrix = cls(rows, cols)

            for line in lines:
                line = line.strip()
                if line.startswith("(") and line.endswith(")"):
                    try:
                        row, col, value = map(int, line.strip("()").split(","))
                        matrix.insert(row, col, value)
                    except ValueError:
                        print(f"⚠️ Skipping invalid line: {line}")

            return matrix

        except FileNotFoundError:
            print(f"❌ Error: File '{file_path}' not found.")
            exit(1)
        except ValueError as e:
            print(f"⚠️ Error in file format: {e}")
            exit(1)

    def add(self, other):
        """Adds two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = SparseMatrix(self.rows, self.cols)
        for key, value in self.data.items():
            result.insert(key[0], key[1], value + other.data.get(key, 0))

        for key, value in other.data.items():
            if key not in self.data:
                result.insert(key[0], key[1], value)

        return result

    def subtract(self, other):
        """Subtracts two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result = SparseMatrix(self.rows, self.cols)
        for key, value in self.data.items():
            result.insert(key[0], key[1], value - other.data.get(key, 0))

        for key, value in other.data.items():
            if key not in self.data:
                result.insert(key[0], key[1], -value)

        return result

    def multiply(self, other):
        """Multiplies two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Matrix multiplication not possible: Incompatible dimensions.")

        result = SparseMatrix(self.rows, other.cols)

        for (r1, c1), v1 in self.data.items():
            for c2 in range(other.cols):
                if (c1, c2) in other.data:
                    result.insert(r1, c2, result.data.get((r1, c2), 0) + v1 * other.data[(c1, c2)])

        return result



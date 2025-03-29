import os
from src.sparse_matrix import SparseMatrix

if __name__ == "__main__":
    print("Sparse Matrix Operations")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_inputs_dir = os.path.join(base_dir, "sample_inputs")
    file1 = os.path.join(sample_inputs_dir, "matrix1.txt")
    file2 = os.path.join(sample_inputs_dir, "matrix2.txt")

    if not os.path.exists(file1) or not os.path.exists(file2):
        print("❌ Error: Matrix input files not found.")
        exit(1)

    matrix1 = SparseMatrix.from_file(file1)
    matrix2 = SparseMatrix.from_file(file2)

    print("\nMatrix 1:")
    matrix1.display()
    print("\nMatrix 2:")
    matrix2.display()

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    choice = input("Enter choice (1/2/3): ")

    try:
        if choice == "1":
            print("\nAddition Result:")
            matrix1.add(matrix2).display()
        elif choice == "2":
            print("\nSubtraction Result:")
            matrix1.subtract(matrix2).display()
        elif choice == "3":
            print("\nMultiplication Result:")
            matrix1.multiply(matrix2).display()
        else:
            print("❌ Invalid choice.")
    except ValueError as e:
        print(f"⚠️ Error: {e}")






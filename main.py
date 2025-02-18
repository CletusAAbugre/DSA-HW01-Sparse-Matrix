from src.sparse_matrix import SparseMatrix

def main():
    print("Creating a Sparse Matrix...")
    sm = SparseMatrix(3, 3)
    sm.insert(0, 1, 5)
    sm.insert(2, 2, 10)

    print("\nSparse Matrix Representation:")
    sm.display()

    print("\nTranspose of Sparse Matrix:")
    sm.transpose().display()

if __name__ == "__main__":
    main()

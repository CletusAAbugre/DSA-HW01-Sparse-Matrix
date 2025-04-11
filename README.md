 DSA HW01 - Sparse Matrix Operations

This project is part of the Data Structures and Algorithms (DSA) course. It implements operations on sparse matrices, including:
- Loading a sparse matrix from a file
- Performing matrix addition, subtraction, and multiplication
- Saving the result to an output file

The solution is implemented in JavaScript using ES modules.

 Folder Structure


dsa_hw01_sparse_matrix/
├── dsa/
│   └── sparse_matrix/
│       └── code/
│           └── src/
│               ├── main.js               Main script to run matrix operations
│               ├── sparse_matrix.js      SparseMatrix class implementation
│               ├── package.json          Node package configuration
│               ├── package-lock.json     Auto-generated lock file
│               └── sample_inputs/        Folder containing matrix input files
│                   ├── matrixfile1.txt
│                   ├── matrixfile3.txt
│                   └── (other sample input files)
├── README.md                           Project documentation (this file)


 Getting Started

 1. Clone the Repository


git clone https://github.com/CletusAAbugre/DSA-HW01-Sparse-Matrix.git


2. Navigate to the Project Directory


cd DSA-HW01-Sparse-Matrix/dsa/sparse_matrix/code/src


3. Install Dependencies


npm install


 4. Running the Application

Use the following command format to run the operations:


node main.js <operation> <matrix1_file> <matrix2_file> <output_file>


For example, to add two matrices:


node main.js add sample_inputs/matrixfile1.txt sample_inputs/matrixfile3.txt sample_inputs/result.txt


Available operations:
- add` – matrix addition
- subtract` – matrix subtraction
- multiply` – matrix multiplication

 5. Output

The result of the operation will be saved to the specified output file. For example, after running an addition, check the content of sample_inputs/result.txt` for the result.

 Code Overview

- sparse_matrix.js: Contains the `SparseMatrix` class that supports reading from a file, performing addition, subtraction, multiplication, and converting the matrix back to string format.
- main.js: Provides a command-line interface for selecting matrix files, choosing an operation, and saving the result.
- sample_inputs/: Contains the matrix input files in the expected format:
  
  rows=<number>
  cols=<number>
  (row, col, value)
  (row, col, value)
  

 Sample Input Format

rows=4795
cols=4795
(0, 1, 5)
(2, 2, 10)


 Final Notes

- Ensure your matrix input files are placed inside the `sample_inputs` folder.
- Your code handles whitespace and basic file format errors.
- For any issues or further clarifications, please refer to the course instructions or contact your facilitator.


Sparse Matrix Operations - DSA HW01
Project Overview
This project is part of the Data Structures and Algorithms (DSA) course. It focuses on Sparse Matrix operations, including:

✅ Creating a sparse matrix  
✅ Printing the matrix  
✅ Transposing the matrix  
✅ Performing addition, subtraction, and multiplication of sparse matrices  
✅ Running unit tests to validate functionality  

Folder Structure
DSA_HW01_SparseMatrix/
│── src/
│   ├── sparse_matrix.py        Sparse Matrix implementation
│   ├── __init__.py             Makes 'src' a Python package
│── tests/
│   ├── test_sparse_matrix.py    Unit tests
│   ├── __init__.py             Makes 'tests' a Python package
│── sample_inputs/               Contains sample sparse matrix input files
│── main.py                      Runs the Sparse Matrix operations
│── README.md                    Project documentation
│── .gitignore                   #Files to ignore in Git


Getting Started
1. Clone the Repository

git clone https://github.com/CletusAAbugre/DSA-HW01-Sparse-Matrix.git
cd DSA-HW01-Sparse-Matrix

2.Run the Program
python main.py

3️.Run Unit Tests
python -m unittest discover tests

Example Output:
Sparse Matrix Operations

Matrix 1:
Sparse Matrix:
0 5 0
0 0 0
0 0 10

Matrix 2:
Sparse Matrix:
0 3 0
0 0 0
0 0 2

Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
Enter choice (1/2/3): 3

Multiplication Result:
Sparse Matrix:
0 0 0
0 0 0
0 0 20

Features
- Sparse Matrix Representation: Efficiently stores non-zero elements to optimize memory.
- Matrix Operations: Supports addition, subtraction, multiplication, and transpose.
- Exception Handling: Handles invalid input formats and mismatched dimensions.
- Unit Testing: Ensures the correctness of the matrix operations.

Contributors
👤 Cletus Abugre Ayeebo  
📌 Course: Data Structures and Algorithms (DSA)  
📌 University: African Leadership University (ALU)  

Acknowledgment
This project is part of the DSA coursework at ALU, and the objective is to improve algorithmic problem-solving skills using efficient data structures.


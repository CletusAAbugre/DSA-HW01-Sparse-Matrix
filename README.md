



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


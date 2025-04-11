🧮 DSA HW01 - Sparse Matrix Operations

This is a JavaScript project for the **Data Structures and Algorithms (DSA)** course. It helps you work with **sparse matrices**—matrices that mostly contain zeros.

The project supports basic operations like loading matrices from files, adding, subtracting, multiplying them, and saving the result to a file. It uses ES Modules and runs with Node.js in the terminal.

---

## ✅ What This Project Can Do

- Load a sparse matrix from a file
- ➕ Add two sparse matrices
- ➖ Subtract one matrix from another
- ✖️ Multiply two sparse matrices
- 💾 Save the result to an output file

---

## 📁 Project Structure

DSA-HW01-Sparse-Matrix/ └── dsa/ └── sparse_matrix/ └── code/ └── src/ ├── main.js # Main script to run operations ├── sparse_matrix.js # SparseMatrix class ├── package.json # Project dependencies ├── sample_inputs/ # Input matrix files │ ├── matrixfile1.txt │ ├── matrixfile3.txt └── result.txt # Output file (auto-generated)

 How to Run the Program

 Step 1: Install Node Modules

Open your terminal, go into the `src/` folder, and run:


npm install
     Commands to run the file
     ➕ To Add Matrices:

npm start -- add ./sample_inputs/matrixfile1.txt ./sample_inputs/matrixfile3.txt result.txt
➖ To Subtract Matrices:

npm start -- sub ./sample_inputs/matrixfile1.txt ./sample_inputs/matrixfile3.txt result_sub.txt
✖️ To Multiply Matrices:

npm start -- mul ./sample_inputs/matrixfile1.txt ./sample_inputs/matrixfile3.txt result_mul.txt
📄 Output Format
The results are saved in a text file you choose. The format looks like this:


rows=7
cols=5000
(6, 13, 672)
(6, 81, 1022)
(6, 178, -630)
(6, 351, -204)
(6, 1000, 679)
(6, 1624, 637)
(6, 2278, -384)
(6, 2394, 415)
(6, 2763, -20)
(6, 4003, 817)
(6, 4285, -657)
The rows= and cols= lines show the matrix size.

Each row after that shows a non-zero value and where it appears in the matrix:
(rowIndex, colIndex, value)

How to View the Output
cat result_add.txt
cat result_subtract.txt
cat result_mul.txt


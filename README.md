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

## How to Run the Program

### Step 1: Install Node Modules

```
npm install
```

### Step 2: Execution


```
node main.js <operation> <file1_name> <file2_name> <result_file>
```

#### Note: the operation section has three options: 
- ```add``` (for addition)
- ```subtract``` (for substraction)
- ```multiply``` (for multiplication)

Here is a existing example of an addition:
```
node main.js add .\sample_inputs\matrixfile1.txt .\sample_inputs\matrixfile3.txt result1-2.txt
```
#### Note: The sample files are all in the ```sample_inputs``` folder as said in the instructions 

### Step 3: Open result
Look for the file with the name that you put as a result file and open it and voila!
Example:
```
rows=4795
cols=4795
(0, 775, 517)
(0, 1425, -127)
(0, 8463, -290)
(0, 2617, -394)
(0, 441, -692)
(0, 6598, 292)
(0, 5177, -840)
(0, 3791, 289)
(0, 1444, -642)
(0, 3458, -893)
(0, 4254, 723)
(0, 990, -580)
(0, 9041, -945)
(0, 2324, -596)
(0, 1194, -1005)
...
```



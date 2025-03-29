import fs from "fs";

class SparseMatrix {
  constructor(rows, cols) {
    this.rows = rows;
    this.cols = cols;
    this.data = new Map(); // Store matrix values efficiently
  }

  static async loadFromFile(filePath) {
    try {
      const content = await fs.promises.readFile(filePath, "utf8");
      const lines = content.trim().split("\n");

      const numRows = parseInt(lines[0].split("=")[1]);
      const numCols = parseInt(lines[1].split("=")[1]);

      const matrix = new SparseMatrix(numRows, numCols);

      for (let i = 2; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;

        const [row, col, value] = line
          .slice(1, -1)
          .split(",")
          .map(Number);

        matrix.set(row, col, value);
      }

      return matrix;
    } catch (error) {
      throw new Error(`Error reading file: ${error.message}`);
    }
  }

  get(row, col) {
    return this.data.get(row)?.get(col) || 0;
  }

  set(row, col, value) {
    if (value === 0) {
      this.data.get(row)?.delete(col);
      if (this.data.get(row)?.size === 0) {
        this.data.delete(row);
      }
    } else {
      if (!this.data.has(row)) this.data.set(row, new Map());
      this.data.get(row).set(col, value);
    }
  }

  add(matrix) {
    if (this.rows !== matrix.rows || this.cols !== matrix.cols) {
      throw new Error("Matrix dimensions must be the same for addition.");
    }

    const result = new SparseMatrix(this.rows, this.cols);

    for (const [row, rowData] of this.data) {
      for (const [col, value] of rowData) {
        result.set(row, col, value);
      }
    }

    for (const [row, rowData] of matrix.data) {
      for (const [col, value] of rowData) {
        result.set(row, col, result.get(row, col) + value);
      }
    }

    return result;
  }

  subtract(matrix) {
    if (this.rows !== matrix.rows || this.cols !== matrix.cols) {
      throw new Error("Matrix dimensions must be the same for subtraction.");
    }

    const result = new SparseMatrix(this.rows, this.cols);

    for (const [row, rowData] of this.data) {
      for (const [col, value] of rowData) {
        result.set(row, col, value);
      }
    }

    for (const [row, rowData] of matrix.data) {
      for (const [col, value] of rowData) {
        result.set(row, col, result.get(row, col) - value);
      }
    }

    return result;
  }

  multiply(matrix) {
    if (this.cols !== matrix.rows) {
      throw new Error("Invalid dimensions for multiplication.");
    }

    const result = new SparseMatrix(this.rows, matrix.cols);

    for (const [rowA, rowDataA] of this.data) {
      for (const [colA, valueA] of rowDataA) {
        const rowDataB = matrix.data.get(colA);
        if (rowDataB) {
          for (const [colB, valueB] of rowDataB) {
            result.set(rowA, colB, result.get(rowA, colB) + valueA * valueB);
          }
        }
      }
    }

    return result;
  }

  toString() {
    let output = `rows=${this.rows}\ncols=${this.cols}\n`;
    for (const [row, rowData] of this.data) {
      for (const [col, value] of rowData) {
        output += `(${row}, ${col}, ${value})\n`;
      }
    }
    return output;
  }
}

async function execute() {
  if (process.argv.length < 6) {
    console.log("Usage: node main.js <operation> <matrix1> <matrix2> <output>");
    process.exit(1);
  }

  try {
    const operation = process.argv[2];
    const matrixA = await SparseMatrix.loadFromFile(process.argv[3]);
    const matrixB = await SparseMatrix.loadFromFile(process.argv[4]);
    const outputPath = process.argv[5];

    let result;
    switch (operation) {
      case "add":
        result = matrixA.add(matrixB);
        break;
      case "subtract":
        result = matrixA.subtract(matrixB);
        break;
      case "multiply":
        result = matrixA.multiply(matrixB);
        break;
      default:
        throw new Error("Invalid operation. Choose: add, subtract, or multiply.");
    }

    await fs.promises.writeFile(outputPath, result.toString());
    console.log(`Result saved to ${outputPath}`);
  } catch (error) {
    console.error("Error:", error.message);
    process.exit(1);
  }
}

await execute();

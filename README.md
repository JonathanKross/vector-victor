# Vector Victor
Vector and Matrix Math
Implement various vector and matrix math functions without using third-party math libraries and loops.

## Objectives
After completing this assignment, you will...

- Understand list comprehensions.
- Understand introductory linear algebra concepts.
- Be able to perform mathematical operations on complex list structures.

## Deliverables
- A Git repo named vector-victor containing at least:
- A README.md file explaining how to run your project.
- A linear_algebra.py module with your implementation.
- A linear_algebra_tests.py file containing unit tests.

## Normal Mode
Implement these linear algebra functions:

- vector shape in shape()
- vector addition in vector_add()
- vector subtraction in vector_sub()
- vector sum in vector_sum()
- dot product in dot()
- vector multiplication by a scalar in vector_multiply()
- mean of multiple vectors in vector_mean()
- magnitude in magnitude()

These functions are all defined in the Vector & Matrix Formulas notebook included with this assignment as well as the linear algebra unit tests.

## Requirements
- All unit tests must pass.
- No use of for or while loops - only comprehensions.
- No use of third-party libraries - only built-in + - / * math operators, built-in functions, and the math module.
- However, it is entirely possible to do this without the math module.

## Advanced Mode (optional)
Implement these additional linear algebra functions:

- matrix and vector shape in shape()
- matrix row in matrix_row()
- matrix column in matrix_col()
- matrix addition in matrix_add()
- matrix subtraction in matrix_sub()
- matrix multiplication by a scalar in matrix_scalar_multiply()
- matrix multiplication by a vector in matrix_vector_multiply()
- matrix multiplication by a matrix in matrix_matrix_multiply()

These functions must:

- Check the shape of the incoming vector or matrix before any calculations.
- Refactor any duplicated code in to reused functions.
- Pass all of their corresponding unit tests.

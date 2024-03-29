#!usr/bin/python3
"""function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
  """function that divides all elements of a matrix

  Args:
    matrix: The matric (list of lists)
    div: The number that I want to divide by

  Returns:
    : new matrix that is (matrix mem / dic)

  Raises:
    TypeError: If matrix isn't list or If it's empty
    TypeError: If Elements in matrix is not int or float
    TypeError: If rows of the matrix are not the same size

  """
  if (not isinstance(matrix, list)) or matrix == [] or not all(isinstance(row, list) for row in matrix) or not all((isinstance(i, int) or isinstance(i, float)) for i in [num for row in matrix for num in row]):
    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
  
  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise TypeError('Each row of the matrix must have the same size')
  
  if not isinstance(div, int) and not isinstance(div, float):
    raise TypeError('div must be a number')
  
  if div == 0:
    raise ZeroDivisionError('division by zero')
    
  return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
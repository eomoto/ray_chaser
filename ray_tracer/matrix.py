from math import *

from ray_tracer.base import *

class Matrix:
  def __init__(self, matrix):
    size = len(matrix)

    for row in matrix:
      if len(row) != size:
        raise TypeError

    self.size = size
    self.matrix = matrix

  def __getitem__(self, key):
    return self.matrix[key]

  def __eq__(self, m2):
    size = len(self.matrix)

    if size != len(m2.matrix):
      return False

    for r in range(size):
      for c in range(size):
        if not equals(self.matrix[r][c], m2.matrix[r][c]):
          return False

    return True

  def __mul__(self, other):
    size = 4
    m1 = self.matrix

    if self.size != size or other.size != size:
      return TypeError

    if isinstance(other, Matrix):
      m2 = other.matrix
      result = np.zeros((size, size), float)

      for r in range(size):
        for c in range(size):
          first = m1[r][0] * m2[0][c]
          second = m1[r][1] * m2[1][c]
          third = m1[r][2] * m2[2][c]
          fourth = m1[r][3] * m2[3][c]
          result[r][c] = first + second + third + fourth

      return Matrix(result)
    elif isinstance(other, Tuple):
      result = np.zeros(size, float)

      for r in range(size):
        row = m1[r]
        result[r] = Tuple(row[0], row[1], row[2], row[3]).dot(other)

      return Tuple(result[0], result[1], result[2], result[3])
    else:
      return TypeError

  def transpose(self):
    size = self.size

    if size != 4:
      return TypeError

    result = np.zeros((size, size), float)

    for r in range(size):
      for c in range(size):
        result[c][r] = self.matrix[r][c]

    return Matrix(result)

  def determinant(self):
    m = self.matrix
    d = 0

    if self.size == 2:
      d = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    else:
      for c in range(self.size):
        d = d + (m[0][c] * self.cofactor(0, c))
    return d

  def submatrix(self, row, column):
    size = self.size - 1
    result = np.zeros((size, size), float)
    row_offset = 0

    for r in range(size):
      column_offset = 0

      if r == row:
        row_offset = 1

      for c in range(size):
        if c == column:
          column_offset = 1

        r2 = r + row_offset
        c2 = c + column_offset
        result[r][c] = self.matrix[r2][c2]

    return Matrix(result)

  def minor(self, row, column):
    return self.submatrix(row, column).determinant()

  def cofactor(self, row, column):
    minor = self.minor(row, column)

    if (row + column) % 2 == 1:
      return minor * -1

    return minor

  def is_invertible(self):
    return self.determinant() != 0

  def inverse(self):
    d = self.determinant()

    if d == 0:
      # matrix is not invertible
      return False

    size = self.size
    m2 = np.zeros((size, size), float)

    for r in range(size):
      for c in range(size):
        m2[c][r] = self.cofactor(r, c) / d

    return Matrix(m2)

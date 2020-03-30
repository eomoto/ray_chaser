from ray_tracer.base import *
from ray_tracer.canvas import *
from ray_tracer.matrix import *

def test_matrix():
  # Scenario: Constructing and inspecting a 4x4 matrix

  matrix = [
    [1, 2, 3, 4],
    [5.5, 6.6, 7.5, 8.5],
    [9, 10, 11, 12],
    [13.5, 14.5, 15.5, 16.5]
  ]
  m = Matrix(matrix)

  assert equals(m[0][0], 1)
  assert equals(m[0][3], 4)
  assert equals(m[1][0], 5.5)
  assert equals(m[1][2], 7.5)
  assert equals(m[2][2], 11)
  assert equals(m[3][0], 13.5)
  assert equals(m[3][2], 15.5)

def test_matrix_2x2():
  # Scenario: A 2x2 matrix outght to be representable

  matrix = [
    [-3, 5],
    [1, -2]
  ]
  m = Matrix(matrix)

  assert equals(m[0][0], -3)
  assert equals(m[0][1], 5)
  assert equals(m[1][0], 1)
  assert equals(m[1][1], -2)

def test_matrix_3x3():
  # Scenario: A 3x3 matrix outght to be representable

  matrix = [
    [-3, 5, 0],
    [1, -2, -7],
    [0, 1, 1]
  ]
  m = Matrix(matrix)

  assert equals(m[0][0], -3)
  assert equals(m[1][1], -2)
  assert equals(m[2][2], 1)

def test_comparing_identicle_matrices():
  # Scenario: Matrix equality with identical matrices

  matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
  ]
  a = Matrix(matrix)
  b = Matrix(matrix)

  assert a == b

def test_comparing_different_matrices():
  # Scenario: Matrix equality with different matrices

  matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
  ]
  matrix2 = [
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
  ]
  a = Matrix(matrix1)
  b = Matrix(matrix2)

  assert a != b

def test_matrix_mul():
  # Scenario: Multiplying two matrices

  matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
  ]
  matrix2 = [
    [-2, 1, 2, 3],
    [3, 2, 1, -1],
    [4, 3, 6, 5],
    [1, 2, 7, 8]
  ]
  a = Matrix(matrix1)
  b = Matrix(matrix2)

  answer_matrix = [
    [20, 22, 50, 48],
    [44, 54, 114, 108],
    [40, 58, 110, 102],
    [16, 26, 46, 42]
  ]
  answer = Matrix(answer_matrix)

  assert answer == (a * b)

def test_matrix_tuple_mul():
  # Scenario: A matrix multiplied by a tuple

  matrix = [
    [1, 2, 3, 4],
    [2, 4, 4, 2],
    [8, 6, 4, 1],
    [0, 0, 0, 1]
  ]
  a = Matrix(matrix)
  b = Tuple(1, 2, 3, 1)
  answer = Tuple(18, 24, 33, 1)

  assert answer == (a * b)

def test_identity_matrix_mul():
  # Scenario: Multiplying a matrix by the identity matrix

  matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
  ]
  matrix2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ]
  a = Matrix(matrix1)
  identity_matrix = Matrix(matrix2)
  answer = Matrix(matrix1)

  assert answer == (a * identity_matrix)

def test_identity_matrix_tuple_mul():
  # Scenario: Multiplying the identity matrix by a tuple

  matrix = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ]
  identity_matrix = Matrix(matrix)
  a = Tuple(1, 2, 3, 4)
  answer = a

  assert answer == (identity_matrix * a)

def test_matrix_transpose():
  # Scenario: Transposing a matrix

  matrix = [
    [0, 9, 3, 0],
    [9, 8, 0, 8],
    [1, 8, 5, 3],
    [0, 0, 5, 8]
  ]
  answer_matrix = [
    [0, 9, 1, 0],
    [9, 8, 8, 0],
    [3, 0, 5, 5],
    [0, 8, 3, 8]
  ]
  m = Matrix(matrix)
  answer = Matrix(answer_matrix)

  assert answer == m.transpose()

def test_identity_matrix_transpose():
  # Scenario: Transposing the identity matrix

  matrix = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ]
  identity_matrix = Matrix(matrix)
  answer = identity_matrix

  assert answer == identity_matrix.transpose()

def test_matrix_determinant_2x2():
  # Scenario: Calculating the determinant of a 2x2 matrix

  matrix = [
    [1, 5],
    [-3, 2]
  ]
  m = Matrix(matrix)
  answer = 17

  assert answer == m.determinant()

def test_matrix_submatrix_3x3():
  # Scenario: A submatrix of a 3x3 matrix is a 2x2 matrix

  matrix = [
    [1, 5, 0],
    [-3, 2, 7],
    [0, 6, -3]
  ]
  answer_matrix = [
    [-3, 2],
    [0, 6]
  ]
  a = Matrix(matrix)
  answer = Matrix(answer_matrix)

  assert answer == a.submatrix(0, 2)

def test_matrix_submatrix_4x4():
  # Scenario: A submatrix of a 4x4 matrix is a 3x3 matrix

  matrix = [
    [-6, 1, 1, 6],
    [-8, 5, 8, 6],
    [-1, 0, 8, 2],
    [-7, 1, -1, 1]
  ]
  answer_matrix = [
    [-6, 1, 6],
    [-8, 8, 6],
    [-7, -1, 1]
  ]
  a = Matrix(matrix)
  answer = Matrix(answer_matrix)

  assert answer == a.submatrix(2, 1)

def test_matrix_minor_3x3():
  # Scenario: Calculating a minor of a 3x3 matrix

  matrix = [
    [3, 5, 0],
    [2, -1, -7],
    [6, -1, 5]
  ]
  a = Matrix(matrix)
  b = a.submatrix(1, 0)
  answer1 = 25
  answer2 = 25

  assert answer1 == b.determinant()
  assert answer2 == a.minor(1, 0)

def test_matrix_cofactor_3x3():
  # Scenario: Calculating a cofactor of a 3x3 matrix

  matrix = [
    [3, 5, 0],
    [2, -1, -7],
    [6, -1, 5]
  ]
  a = Matrix(matrix)
  answer1 = -12
  answer2 = -12
  answer3 = 25
  answer4 = -25

  assert answer1 == a.minor(0, 0)
  assert answer2 == a.cofactor(0, 0)
  assert answer3 == a.minor(1, 0)
  assert answer4 == a.cofactor(1, 0)

def test_matrix_determinant_3x3():
  # Scenario: Calculating the determinant of a 3x3 matrix

  matrix = [
    [1, 2, 6],
    [-5, 8, -4],
    [2, 6, 4]
  ]
  a = Matrix(matrix)
  answer1 = 56
  answer2 = 12
  answer3 = -46
  answer4 = -196

  assert answer1 == a.cofactor(0, 0)
  assert answer2 == a.cofactor(0, 1)
  assert answer3 == a.cofactor(0, 2)
  assert answer4 == a.determinant()

def test_matrix_determinant_4x4():
  # Scenario: Calculating the determinant of a 4x4 matrix

  matrix = [
    [-2, -8, 3, 5],
    [-3, 1, 7, 3],
    [1, 2, -9, 6],
    [-6, 7, 7, -9]
  ]
  a = Matrix(matrix)
  answer1 = 690
  answer2 = 447
  answer3 = 210
  answer4 = 51
  answer5 = -4071

  assert answer1 == a.cofactor(0, 0)
  assert answer2 == a.cofactor(0, 1)
  assert answer3 == a.cofactor(0, 2)
  assert answer4 == a.cofactor(0, 3)
  assert answer5 == a.determinant()

def test_matrix_invertible():
  # Scenario: Testing an invertible matrix for invertibility

  matrix = [
    [6, 4, 4, 4],
    [5, 5, 7, 6],
    [4, -9, 3, -7],
    [9, 1, 7, -6]
  ]
  a = Matrix(matrix)
  answer = -2120

  assert answer == a.determinant()
  assert a.is_invertible() == True

def test_matrix_noninvertible():
  # Scenario: Testing an noninvertible matrix for invertibility

  matrix = [
    [-4, 2, -2, -3],
    [9, 6, 2, 6],
    [0, -5, 1, -5],
    [0, 0, 0, 0]
  ]
  a = Matrix(matrix)
  answer = 0

  assert answer == a.determinant()
  assert a.is_invertible() == False

def test_matrix_inverse1():
  # Scenario: Calculating the inverse of a matrix

  matrix = [
    [-5, 2, 6, -8],
    [1, -5, 1, 8],
    [7, 7, -6, -7],
    [1, -3, 7, 4]
  ]
  answer_matrix = [
    [0.21805, 0.45113, 0.24060, -0.04511],
    [-0.80827, -1.45677, -0.44361, 0.52068],
    [-0.07895, -0.22368, -0.05263, 0.19737],
    [-0.52256, -0.81391, -0.30075, 0.30639]
  ]
  a = Matrix(matrix)
  b = a.inverse()
  answer1 = 532
  answer2 = -160
  answer3 = -160/532
  answer4 = 105
  answer5 = 105/532
  answer6 = Matrix(answer_matrix)

  assert answer1 == a.determinant()
  assert answer2 == a.cofactor(2, 3)
  assert answer3 == b[3][2]
  assert answer4 == a.cofactor(3, 2)
  assert answer5 == b[2][3]
  assert answer6 == b

def test_matrix_inverse2():
  # Scenario: Calculating the inverse of another matrix

  matrix = [
    [8, -5, 9, 2],
    [7, 5, 6, 1],
    [-6, 0, 9, 6],
    [-3, 0, -9, -4]
  ]
  answer_matrix = [
    [-0.15385, -0.15385, -0.28205, -0.53846],
    [-0.07692, 0.12308, 0.02564, 0.03077],
    [0.35897, 0.35897, 0.43590, 0.92308],
    [-0.69231, -0.69231, -0.76923, -1.92308]
  ]
  a = Matrix(matrix)
  b = a.inverse()
  answer = Matrix(answer_matrix)

  assert answer == b

def test_matrix_inverse3():
  # Scenario: Calculating the inverse of a third matrix

  matrix = [
    [9, 3, 0, 9],
    [-5, -2, -6, -3],
    [-4, 9, 6, 4],
    [-7, 6, 6, 2]
  ]
  answer_matrix = [
    [-0.04074, -0.07778, 0.14444, -0.22222],
    [-0.07778, 0.03333, 0.36667, -0.33333],
    [-0.02901, -0.14630, -0.10926, 0.12963],
    [0.17778, 0.06667, -0.26667, 0.33333]
  ]
  a = Matrix(matrix)
  b = a.inverse()
  answer = Matrix(answer_matrix)

  assert answer == b

def test_matrix_inverse_product():
  # Scenario: Multiplying a product by its inverse

  matrix1 = [
    [3, -9, 7, 3],
    [3, -8, 2, -9],
    [-4, 4, 4, 1],
    [-6, 5, -1, 1]
  ]
  matrix2 = [
    [8, 2, 2, 2],
    [3, -1, 7, 0],
    [7, 0, 5, 4],
    [6, -2, 0, 5]
  ]
  a = Matrix(matrix1)
  b = Matrix(matrix2)
  c = a * b
  answer = a

  assert answer == c * b.inverse()

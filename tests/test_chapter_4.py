from ray_tracer.transformation import *

def test_translation_matrix_point_mul():
  # Scenario: Multiplying by a translation matrix

  transform = Translation(5, -3, 2)
  p = Point(-3, 4, 5)
  answer = Point(2, 1, 7)

  assert answer == transform * p

def test_inverse_translation_matrix_point_mul():
  # Scenario: Multiplying by the inverse of a translation matrix

  transform = Translation(5, -3, 2)
  inv = transform.inverse()
  p = Point(-3, 4, 5)
  answer = Point(-8, 7, 3)

  assert answer == inv * p

def test_translation_matrix_vector_mul():
  # Scenario: Translation does not affect vectors

  transform = Translation(5, -3, 2)
  v = Vector(-3, 4, 5)
  answer = v

  assert answer == transform * v

def test_scaling_matrix_point_mul():
  # Scenario: A scaling matrix applied to a point

  transform = Scaling(2, 3, 4)
  p = Point(-4, 6, 8)
  answer = Point(-8, 18, 32)

  assert answer == transform * p

def test_scaling_matrix_vector_mul():
  # Scenario: A scaling matrix applied to a vector

  transform = Scaling(2, 3, 4)
  v = Vector(-4, 6, 8)
  answer = Vector(-8, 18, 32)

  assert answer == transform * v

def test_inverse_scaling_matrix_vector_mul():
  # Scenario: Multiplying by the inverse of a scaling matrix

  transform = Scaling(2, 3, 4)
  inv = transform.inverse()
  v = Vector(-4, 6, 8)
  answer = Vector(-2, 2, 2)

  assert answer == inv * v

def test_reflection():
  # Scenario: Reflection is scaling by a negative value

  transform = Scaling(-1, 1, 1)
  p = Point(2, 3, 4)
  answer = Point(-2, 3, 4)

  assert answer == transform * p

def test_x_axis_point_rotation():
  # Scenario: Rotating a point around the x axis

  p = Point(0, 1, 0)
  half_quarter = Rotation_X(pi / 4)
  full_quarter = Rotation_X(pi / 2)
  answer1 = Point(0, sqrt(2) / 2, sqrt(2) / 2)
  answer2 = Point(0, 0, 1)

  assert answer1 == half_quarter * p
  assert answer2 == full_quarter * p

def test_inverse_x_axis_point_rotation():
  # Scenario: The inverse of an x-rotation rotates in the opposite direction

  p = Point(0, 1, 0)
  half_quarter = Rotation_X(pi / 4)
  inv = half_quarter.inverse()
  answer = Point(0, sqrt(2) / 2, (sqrt(2) / 2) * -1)

  assert answer == inv * p

def test_y_axis_point_rotation():
  # Scenario: Rotating a point around the y axis

  p = Point(0, 0, 1)
  half_quarter = Rotation_Y(pi / 4)
  full_quarter = Rotation_Y(pi / 2)
  answer1 = Point(sqrt(2) / 2, 0, sqrt(2) / 2)
  answer2 = Point(1, 0, 0)

  assert answer1 == half_quarter * p
  assert answer2 == full_quarter * p

def test_z_axis_point_rotation():
  # Scenario: Rotating a point around the z axis

  p = Point(0, 1, 0)
  half_quarter = Rotation_Z(pi / 4)
  full_quarter = Rotation_Z(pi / 2)
  answer1 = Point((sqrt(2) / 2) * -1, sqrt(2) / 2, 0)
  answer2 = Point(-1, 0, 0)

  assert answer1 == half_quarter * p
  assert answer2 == full_quarter * p

def test_shearing_transforrmation_x_proportional_to_y():
  # Scenario: A shearing transformation moves x in proportion to y

  transform = Shearing(1, 0, 0, 0, 0, 0)
  p = Point(2, 3, 4)
  answer = Point(5, 3, 4)

  assert answer == transform * p

def test_shearing_transforrmation_x_proportional_to_z():
  # Scenario: A shearing transformation moves x in proportion to z

  transform = Shearing(0, 1, 0, 0, 0, 0)
  p = Point(2, 3, 4)
  answer = Point(6, 3, 4)

  assert answer == transform * p

def test_shearing_transforrmation_y_proportional_to_x():
  # Scenario: A shearing transformation moves y in proportion to x

  transform = Shearing(0, 0, 1, 0, 0, 0)
  p = Point(2, 3, 4)
  answer = Point(2, 5, 4)

  assert answer == transform * p

def test_shearing_transforrmation_y_proportional_to_z():
  # Scenario: A shearing transformation moves y in proportion to z

  transform = Shearing(0, 0, 0, 1, 0, 0)
  p = Point(2, 3, 4)
  answer = Point(2, 7, 4)

  assert answer == transform * p

def test_shearing_transforrmation_z_proportional_to_x():
  # Scenario: A shearing transformation moves z in proportion to x

  transform = Shearing(0, 0, 0, 0, 1, 0)
  p = Point(2, 3, 4)
  answer = Point(2, 3, 6)

  assert answer == transform * p

def test_shearing_transforrmation_z_proportional_to_y():
  # Scenario: A shearing transformation moves z in proportion to y

  transform = Shearing(0, 0, 0, 0, 0, 1)
  p = Point(2, 3, 4)
  answer = Point(2, 3, 7)

  assert answer == transform * p

def test_sequence_transformations():
  # Scenario: Individual transformations are applied in sequence

  p = Point(1, 0, 1)
  A = Rotation_X(pi / 2)
  B = Scaling(5, 5, 5)
  C = Translation(10, 5, 7)

  # apply rotation first
  p2 = A * p
  answer1 = Point(1, -1, 0)

  assert answer1 == p2

  # then apply scaling
  p3 = B * p2
  answer2 = Point(5, -5, 0)

  assert answer2 == p3

  # apply rotation first
  p4 = C * p3
  answer3 = Point(15, 0, 7)

  assert answer3 == p4

def test_chained_transformations():
  # Scenario: Chained transformations must be applied in reverse order

  p = Point(1, 0, 1)
  A = Rotation_X(pi / 2)
  B = Scaling(5, 5, 5)
  C = Translation(10, 5, 7)
  T = C * B * A
  answer = Point(15, 0, 7)

  assert answer == T * p

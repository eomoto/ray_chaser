from ray_tracer.base import *

def test_tuple_is_point():
  # Scenario: A tuple with w=1.0 is a point
  a = Tuple(4.3, -4.2, 3.1, 1.0)
  assert a.x == 4.3
  assert a.y == -4.2
  assert a.z == 3.1
  assert a.w == 1.0
  assert a.is_point() == True
  assert a.is_vector() == False

def test_tuple_is_vector():
  # Scenario: A tuple with w=0 is a vector
  a = Tuple(4.3, -4.2, 3.1, 0)
  assert a.x == 4.3
  assert a.y == -4.2
  assert a.z == 3.1
  assert a.w == 0
  assert a.is_point() == False
  assert a.is_vector() == True

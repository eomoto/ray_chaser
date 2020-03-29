import numpy as np

from ray_tracer.base import *

def test_tuple_is_point():
  # Scenario: A tuple with w=1.0 is a point
  a = Tuple(4.3, -4.2, 3.1, 1.0)
  assert equals(a.x, 4.3)
  assert equals(a.y, -4.2)
  assert equals(a.z, 3.1)
  assert equals(a.w, 1.0)
  assert a.is_point() == True
  assert a.is_vector() == False

def test_tuple_is_vector():
  # Scenario: A tuple with w=0 is a vector
  a = Tuple(4.3, -4.2, 3.1, 0)
  assert equals(a.x, 4.3)
  assert equals(a.y, -4.2)
  assert equals(a.z, 3.1)
  assert equals(a.w, 0)
  assert a.is_point() == False
  assert a.is_vector() == True

def test_point_creates_point_tuple():
  # Scenario: point() creates tuples with w=1
  p = Point(4, -4, 3)
  t = Tuple(4, -4, 3, 1)
  assert equals(p.x, t.x)
  assert equals(p.y, t.y)
  assert equals(p.z, t.z)
  assert equals(p.w, t.w)
  assert p.is_point() == t.is_point()
  assert p.is_vector() == t.is_vector()

def test_vector_creates_vector_tuple():
  # Scenario: vector() creates tuples with w=0
  v = Vector(4, -4, 3)
  t = Tuple(4, -4, 3, 0)
  assert equals(v.x, t.x)
  assert equals(v.y, t.y)
  assert equals(v.z, t.z)
  assert equals(v.w, t.w)
  assert v.is_point() == t.is_point()
  assert v.is_vector() == t.is_vector()

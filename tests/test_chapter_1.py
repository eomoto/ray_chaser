from math import *
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
  assert p.equals(t)

def test_vector_creates_vector_tuple():
  # Scenario: vector() creates tuples with w=0
  v = Vector(4, -4, 3)
  t = Tuple(4, -4, 3, 0)
  assert v.equals(t)

def test_tuple_add():
  # Scenario: Addint two tuples
  a1 = Tuple(3, -2, 5, 1)
  a2 = Tuple(-2, 3, 1, 0)
  answer = Tuple(1, 1, 6, 1)
  assert answer.equals(a1 + a2)

def test_point_sub():
  # Scenario: Subtracting two points
  p1 = Point(3, 2, 1)
  p2 = Point(5, 6, 7)
  answer = Vector(-2, -4, -6)
  assert answer.equals(p1 - p2)

def test_vector_and_point_sub():
  # Scenario: Subtracting a vector from a point
  p = Point(3, 2, 1)
  v = Vector(5, 6, 7)
  answer = Point(-2, -4, -6)
  assert answer.equals(p - v)

def test_vector_sub():
  # Scenario: Subtracting two vectors
  v1 = Vector(3, 2, 1)
  v2 = Vector(5, 6, 7)
  answer = Vector(-2, -4, -6)
  assert answer.equals(v1 - v2)

def test_zero_vector_sub():
  # Scenario: Subtracting a vector from the zero vector
  zero = Vector(0, 0, 0)
  v = Vector(1, -2, 3)
  answer = Vector(-1, 2, -3)
  assert answer.equals(zero - v)

def test_tuple_neg():
  # Scenario: Negating a tuple
  a = Tuple(1, -2, 3, -4)
  answer = Tuple(-1, 2, -3, 4)
  assert answer.equals(-a)

def test_tuple_scalar_multiplication():
  # Scenario: Multiplying a tuple by a scalar
  a = Tuple(1, -2, 3, -4)
  answer = Tuple(3.5, -7, 10.5, -14)
  assert answer.equals(a * 3.5)

def test_tuple_fraction_multiplication():
  # Scenario: Multiplying a tuple by a fraction
  a = Tuple(1, -2, 3, -4)
  answer = Tuple(0.5, -1, 1.5, -2)
  assert answer.equals(a * 0.5)

def test_tuple_scalar_division():
  # Scenario: Dividing a tuple by a scalar
  a = Tuple(1, -2, 3, -4)
  answer = Tuple(0.5, -1, 1.5, -2)
  assert answer.equals(a / 2)

def test_vector_magnitude_1():
  # Scenario: Computing the magnitude of vector(1, 0, 0)
  v = Vector(1, 0, 0)
  assert equals(v.magnitude(), 1)

def test_vector_magnitude_2():
  # Scenario: Computing the magnitude of vector(0, 1, 0)
  v = Vector(0, 1, 0)
  assert equals(v.magnitude(), 1)

def test_vector_magnitude_3():
  # Scenario: Computing the magnitude of vector(0, 0, 1)
  v = Vector(0, 0, 1)
  assert equals(v.magnitude(), 1)

def test_vector_magnitude_4():
  # Scenario: Computing the magnitude of vector(1, 2, 3)
  v = Vector(1, 2, 3)
  assert equals(v.magnitude(), sqrt(14))

def test_vector_magnitude_5():
  # Scenario: Computing the magnitude of vector(-1, -2, -3)
  v = Vector(-1, -2, -3)
  assert equals(v.magnitude(), sqrt(14))

def test_vector_normalization_1():
  # Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0)
  v = Vector(4, 0, 0)
  answer = Vector(1, 0, 0)
  assert v.normalize().equals(answer)

def test_vector_normalization_2():
  # Scenario: Normalizing vector(1, 2, 3)
  v = Vector(1, 2, 3)
  answer = Vector(0.26726, 0.53452, 0.80178)
  assert v.normalize().equals(answer)

def test_vector_normalization_magnitude():
  # Scenario: The magnitude of a normalized vector
  v = Vector(1, 2, 3)
  assert equals(v.normalize().magnitude(), 1)

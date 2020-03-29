from math import *

EPSILON = 0.00001

def equals(x, y):
  if abs(x - y) <= EPSILON:
    return True
  return False

class Tuple:
  def __init__(self, x, y, z, w):
    self.point_value = 1.0
    self.vector_value = 0
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def __add__(self, t2):
    return Tuple(
      self.x + t2.x,
      self.y + t2.y,
      self.z + t2.z,
      self.w + t2.w
    )

  def __sub__(self, t2):
    return Tuple(
      self.x - t2.x,
      self.y - t2.y,
      self.z - t2.z,
      self.w - t2.w
    )

  def __neg__(self):
    return Tuple(
      self.x * -1,
      self.y * -1,
      self.z * -1,
      self.w * -1
    )

  def __mul__(self, scalar):
    return Tuple(
      self.x * scalar,
      self.y * scalar,
      self.z * scalar,
      self.w * scalar
    )

  def __truediv__(self, scalar):
    return Tuple(
      self.x / scalar,
      self.y / scalar,
      self.z / scalar,
      self.w / scalar
    )

  def is_point(self):
    return self.w == self.point_value

  def is_vector(self):
    return self.w == self.vector_value

  def is_color(self):
    return False

  def magnitude(self):
    return sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

  def normalize(self):
    magnitude = self.magnitude()

    return Tuple(
      self.x / magnitude,
      self.y / magnitude,
      self.z / magnitude,
      self.w / magnitude
    )

  def dot(self, t2):
    return self.x * t2.x + self.y * t2.y + self.z * t2.z + self.w * t2.w

  def equals(self, t2):
    has_equal_points = equals(self.x, t2.x) \
      and equals(self.y, t2.y) \
      and equals(self.z, t2.z) \
      and equals(self.w, t2.w)
    has_equal_type = self.is_point() == t2.is_point() \
      and self.is_vector() == t2.is_vector()

    if has_equal_points and has_equal_type:
      return True
    return False

class Point(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 1.0)

class Vector(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 0)

  def cross(self, v2):
    return Vector(
      (self.y * v2.z) - (self.z * v2.y),
      (self.z * v2.x) - (self.x * v2.z),
      (self.x * v2.y) - (self.y * v2.x)
    )

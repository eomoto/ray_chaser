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

  def __add__(self, other):
    return Tuple(
      self.x + other.x,
      self.y + other.y,
      self.z + other.z,
      self.w + other.w
    )

  def __sub__(self, other):
    return Tuple(
      self.x - other.x,
      self.y - other.y,
      self.z - other.z,
      self.w - other.w
    )

  def is_point(self):
    return self.w == self.point_value

  def is_vector(self):
    return self.w == self.vector_value

  def equals(self, other):
    has_equal_points = equals(self.x, other.x) \
      and equals(self.y, other.y) \
      and equals(self.z, other.z) \
      and equals(self.w, other.w)
    has_equal_type = self.is_point() == other.is_point() \
      and self.is_vector() == other.is_vector()

    if has_equal_points and has_equal_type:
      return True
    return False

class Point(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 1.0)

class Vector(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 0)


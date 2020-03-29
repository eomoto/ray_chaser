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

  def is_point(self):
    return self.w == self.point_value

  def is_vector(self):
    return self.w == self.vector_value

class Point(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 1.0)

class Vector(Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 0)


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

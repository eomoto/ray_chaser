from ray_tracer.matrix import *

class Translation(Matrix):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

    matrix = [
      [1, 0, 0, x],
      [0, 1, 0, y],
      [0, 0, 1, z],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

class Scaling(Matrix):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

    matrix = [
      [x, 0, 0, 0],
      [0, y, 0, 0],
      [0, 0, z, 0],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

class Rotation_X(Matrix):
  def __init__(self, r):
    self.r = r

    matrix = [
      [1, 0, 0, 0],
      [0, cos(r), sin(r) * -1, 0],
      [0, sin(r), cos(r), 0],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

class Rotation_Y(Matrix):
  def __init__(self, r):
    self.r = r

    matrix = [
      [cos(r), 0, sin(r), 0],
      [0, 1, 0, 0],
      [sin(r) * -1, 0, cos(r), 0],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

class Rotation_Z(Matrix):
  def __init__(self, r):
    self.r = r

    matrix = [
      [cos(r), sin(r) * -1, 0, 0],
      [sin(r), cos(r), 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

class Shearing(Matrix):
  def __init__(self, X_y, X_z, Y_x, Y_z, Z_x, Z_y):
    self.X_y = X_y
    self.X_z = X_z
    self.Y_x = Y_x
    self.Y_z = Y_z
    self.Z_x = Z_x
    self.Z_y = Z_y

    matrix = [
      [1, X_y, X_z, 0],
      [Y_x, 1, Y_z, 0],
      [Z_x, Z_y, 1, 0],
      [0, 0, 0, 1]
    ]

    super().__init__(matrix)

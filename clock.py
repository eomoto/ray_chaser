import os

from ray_tracer.transformation import *
from ray_tracer.canvas import *

def to_file(filename, ppm_str):
  f = open("output/%s" % filename, "w+")
  f.write(ppm_str)
  f.close()

def create_ppm():
  c = Canvas(800, 800)
  color = Color(0, 1, 0)

  start = Point(0, 200, 0)

  for x in range(0, 12):
    rotation = x * pi / 6
    point = Rotation_Z(rotation) * start
    x = ceil(point.x) + 400
    y = ceil(point.y) + 400

    print(rotation, point.x, point.y, x, y)

    c.write_pixel(x, y, color)

  to_file("clock.ppm", c.canvas_to_ppm())

create_ppm()

import os

from ray_tracer.base import *
from ray_tracer.canvas import *

def tick(env, proj):
  position = proj.position + proj.velocity
  velocity = proj.velocity + env.gravity + env.wind

  return Projectile(position, velocity)

def to_file(filename, ppm_str):
  f = open("output/%s" % filename, "w+")
  f.write(ppm_str)
  f.close()

class Projectile:
  def __init__(self, position, velocity):
    self.position = position
    self.velocity = velocity

class Environment:
  def __init__(self, gravity, wind):
    self.gravity = gravity
    self.wind = wind

def create_ppm():
  # continuing project by creating PPM of trajectory
  start = Point(0, 1, 0)
  velocity = Vector(1, 1.8, 0).normalize() * 11.25
  p = Projectile(start, velocity)

  gravity = Vector(0, -0.1, 0)
  wind = Vector(-0.01, 0, 0)
  e = Environment(gravity, wind)

  c = Canvas(900, 550)
  color = Color(1, 0, 0)

  while p.position.y > 0:
    p = tick(e, p)
    valid_height = p.position.y >= 0 and p.position.y < c.height
    valid_width = p.position.x >= 0 and p.position.x < c.width

    if valid_height and valid_width:
      c.write_pixel(ceil(p.position.x), c.height - ceil(p.position.y), color)

  to_file("projectile.ppm", c.canvas_to_ppm())

def test_projectile():
  # projectile starts one unit above the origin.
  # velocity is normalized to 1 unit/tick.
  p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalize())

  # gravity -0/1 unit/tick, and wind is -0.01 unit/tick.
  e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

  num_ticks = 0

  while p.position.y > 0:
    inputs = (num_ticks, p.position.x, p.position.y, p.position.z, p.position.w)
    print("Number of ticks: %s, Position: (%s, %s, %s, %s)" % inputs)

    p = tick(e, p)
    num_ticks += 1

  inputs = (num_ticks, p.position.x, p.position.y, p.position.z, p.position.w)
  print("Total ticks: %s, Final Position: (%s, %s, %s, %s)" % inputs)

test_projectile()
create_ppm()

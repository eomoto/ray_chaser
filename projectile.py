from ray_tracer.base import *

def tick(env, proj):
  position = proj.position + proj.velocity
  velocity = proj.velocity + env.gravity + env.wind

  return Projectile(position, velocity)

class Projectile:
  def __init__(self, position, velocity):
    self.position = position
    self.velocity = velocity

class Environment:
  def __init__(self, gravity, wind):
    self.gravity = gravity
    self.wind = wind

# projectile starts one unit above the origin.
# velocity is normalized to 1 unit/tick.
p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalize())

# gravity -0/1 unit/tick, and wind is -0.01 unit/tick.
e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

t = tick(e, p)
num_ticks = 1

while t.position.y > 0:
  inputs = (num_ticks, t.position.x, t.position.y, t.position.z, t.position.w)
  print("Number of ticks: %s, Position: (%s, %s, %s, %s)" % inputs)

  t = tick(e, t)
  num_ticks += 1

inputs = (num_ticks, t.position.x, t.position.y, t.position.z, t.position.w)
print("Total ticks: %s, Final Position: (%s, %s, %s, %s)" % inputs)

from ray_tracer.base import *
from ray_tracer.canvas import *

def test_color():
  # Scenario: colors are (red, green, blue) tuples

  c = Color(-0.5, 0.4, 1.7)

  assert equals(c.red, -0.5)
  assert equals(c.green, 0.4)
  assert equals(c.blue, 1.7)
  assert c.is_color() == True

def test_color_add():
  # Scenario: Adding colors

  c1 = Color(0.9, 0.6, 0.75)
  c2 = Color(0.7, 0.1, 0.25)
  answer = Color(1.6, 0.7, 1.0)

  assert answer == (c1 + c2)

def test_color_sub():
  # Scenario: Subtracting colors

  c1 = Color(0.9, 0.6, 0.75)
  c2 = Color(0.7, 0.1, 0.25)
  answer = Color(0.2, 0.5, 0.5)

  assert answer == (c1 - c2)

def test_color_scalar_mul():
  # Scenario: Multiplying a color by a scalar

  c = Color(0.2, 0.3, 0.4)
  answer = Color(0.4, 0.6, 0.8)

  assert answer == (c * 2)

def test_color_mul():
  # Scenario: Multiplying colors

  c1 = Color(1, 0.2, 0.4)
  c2 = Color(0.9, 1, 0.1)
  answer = Color(0.9, 0.2, 0.04)

  assert answer == c1.hadamard_product(c2)

def test_create_canvas():
  # Scenario: Creating a canvas

  c = Canvas(10, 20)
  all_black_pixels = True
  black_pixel = Color(0, 0, 0)

  for row in c.pixels:
    for p in row:
      if not p == black_pixel:
        all_black_pixels = False
        break

    if all_black_pixels == False:
      break

  assert equals(c.width, 10)
  assert equals(c.height, 20)
  assert all_black_pixels

def test_write_to_canvas():
  # Scenario: Writing pixels to a canvas

  c = Canvas(10, 20)
  red = Color(1, 0, 0)
  c.write_pixel(2, 3, red)
  answer = red

  assert answer == c.pixel_at(2, 3)

def test_ppm_header():
  # Scenario: Constructing the PPM header

  c = Canvas(5, 3)
  ppm = c.canvas_to_ppm()
  ppm_header = ppm.split("\n")[:3]
  answer = "P3\n5 3\n255"

  assert answer == "\n".join(ppm_header)

def test_ppm_body():
  # Scenario: Constructing the PPM pixel data

  c = Canvas(5, 3)
  c1 = Color(1.5, 0, 0)
  c2 = Color(0, 0.5, 0)
  c3 = Color(-0.5, 0, 1)

  c.write_pixel(0, 0, c1)
  c.write_pixel(2, 1, c2)
  c.write_pixel(4, 2, c3)

  ppm = c.canvas_to_ppm()
  ppm_body = ppm.split("\n")[3:]
  answer = "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"

  assert answer == "\n".join(ppm_body)

def test_ppm_body_length():
  # Scenario: Splitting long lines in PPM files

  c = Canvas(10, 2)
  c1 = Color(1, 0.8, 0.6)

  c.write_all_pixels(c1)

  ppm = c.canvas_to_ppm()
  ppm_body = ppm.split("\n")[3:]
  answer = "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n"

  assert answer == "\n".join(ppm_body)

def test_ppm_ends_in_newline():
  # Scenario: PPM files are terminated by a newline character

  c = Canvas(5, 3)
  ppm = c.canvas_to_ppm()
  answer = "\n"

  assert answer == ppm[-1]

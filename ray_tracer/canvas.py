from ray_tracer.base import *

class Color(Tuple):
  def __init__(self, red, green, blue):
    super().__init__(red, green, blue, 0)
    self.red = self.x
    self.green = self.y
    self.blue = self.z

  def hadamard_product(self, c2):
    return Color(
      self.red * c2.red,
      self.green * c2.green,
      self.blue * c2.blue
    )

  def is_color(self):
    return True

  def rgb_to_ppm(self):
    ppm_min = 0
    ppm_max = 255
    ppm_red = str(np.clip(ceil(self.red * 255), ppm_min, ppm_max))
    ppm_green = str(np.clip(ceil(self.green * 255), ppm_min, ppm_max))
    ppm_blue = str(np.clip(ceil(self.blue * 255), ppm_min, ppm_max))

    return [ppm_red, ppm_green, ppm_blue]

class Canvas:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pixels = []
    black_pixel = Color(0, 0, 0)

    for x in range(height):
      row = []

      for y in range(width):
        row.append(black_pixel)

      self.pixels.append(row)

  def pixel_at(self, x, y):
    return self.pixels[y][x]

  def write_pixel(self, x, y, color):
    if (y >= 0 and y < self.height) and (x >= 0 and x < self.width):
      self.pixels[y][x] = color

  def write_all_pixels(self, color):
    for y in range(self.height):
      for x in range(self.width):
        self.pixels[y][x] = color

  def canvas_to_ppm(self):
    ppm = [
      "P3",
      "%s %s" % (self.width, self.height),
      "255"
    ]

    for row in self.pixels:
      ppm_row = ""

      for pixel in row:
        ppm_pixel = pixel.rgb_to_ppm()

        for rgb in ppm_pixel:
          if len(ppm_row) + len(rgb) < 70:
            if len(ppm_row) > 0:
              ppm_row += " "

            ppm_row += rgb
          else:
            ppm.append(ppm_row)
            ppm_row = rgb

      ppm.append(ppm_row)

    return "\n".join(ppm) + "\n"

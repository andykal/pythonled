# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library

###
### settable Pulse, Cycle, and Pixels_used
###

import time
import neopixel
import board
import math

try:
    import urandom as random
except ImportError:
    import random


num_pixels = 30

head = 0
trail_pixels = 10

maxgreen = 80
sin_radians = 0.0
#pixels_used = 4 # 20
# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
#pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.4, auto_write=False)
pixpin = board.D1
pixels = neopixel.NeoPixel(pixpin, num_pixels, brightness=.1, auto_write=False)

p = []

# initialize
for i in range(0, trail_pixels):
  #currblue = (i + 1) * 4
  currblue = 100
  #p[i] = currblue
  p.append(currblue)

# main loop
while True:

  head = (head + 1) % 30
  for j in range(0, num_pixels):
    pixels[j] = (0,0,0)

  sin_radians = sin_radians + 0.05
  fracgreen = 0.6
  multiplier = (math.cos(sin_radians) + 1.0) / 2
  green = int(fracgreen * multiplier)

  for i in range(0, trail_pixels):
	
    curr_pixel = (head - i) % 30
    brightness = i / trail_pixels #fractional brightness of this pixel

    overall_brightness = 180 - int(brightness * p[i] * 2) 
    #overall_brightness = 200 - ( int(brightness * i) * int(brightness * i) * int(brightness * i))
    b = int((1 - multiplier) * overall_brightness)
    g = int((overall_brightness - b) * fracgreen)
    #print(str(i) + " : " + str(overall_brightness) + " : " + str(b) + " : " + str(g))
    #print ("blue = " + str(b) + "  green = " + str(g))
    #print(g)
    #print(str(i) + ":: " + str(b))
    #pixels[curr_pixel] = (random.randint(0,60), random.randint(0,60), p[i])
    pixels[curr_pixel] = (0, g, b)
    #time.sleep(.01)

  pixels.show()


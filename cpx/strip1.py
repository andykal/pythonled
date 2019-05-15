# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library
import time
import neopixel
import board

# Set up the 10 Circuit Playground Express NeoPixels half bright
CPX_pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.5)
#strip = light.createStrip(pins.A1, 24);

# slowly power up via blue color
for i in range(10):
    CPX_pixels.fill((0, i, 0))
    time.sleep(0.05)

# blast off!
CPX_pixels.fill((0, 0, 255))

while True:
    # pulse effect
    for i in range(255, 0, -15):
        #CPX_pixels.fill((0, int(i/4), i))
        CPX_pixels.fill((0, i, i))
    for i in range(0, 255, 5):
        CPX_pixels.fill((0, i, i))


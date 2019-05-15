# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library
import time
import neopixel
import board

# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.5, auto_write=False)

# slowly power up via blue color
for i in range(10):
    pixels.fill((0, i, 0))
    pixels.show()
    time.sleep(0.05)

# blast off!
pixels.fill((0, 0, 255))
pixels.show()

while True:
    # pulse effect
    for i in range(255, 0, -15):
        #CPX_pixels.fill((0, int(i/4), i))
        pixels.fill((0, i, i))
	pixels.show()
    for i in range(0, 255, 5):
        pixels.fill((0, i, i))
	pixels.show()


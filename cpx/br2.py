# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library
import time
import neopixel
import board

try:
    import urandom as random
except ImportError:
    import random

# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.1, auto_write=False)
low = 10
num_pixels = 30 

bubble = 0.0
bubble_speed = 1.21
bubble2 = 7.0
bubble2_speed = 0.5

speed = []
direction = []
maximum = []
blue = []
green = []

for i in range(0, num_pixels):
    #speed.append(random.randint(1,3))
    speed.append(9)
    direction.append(1)
    maxi = random.randint(50,255)
    #maxi = 245
    maximum.append(maxi)
    blue.append(random.randint(15, maxi))
    #blue.append(15)
    green.append(random.randint(0, 30))

while True:

    for p in range(0, num_pixels):
        brt = blue[p]
        #grn = int(green[p] * blue[p] / maximum[p])
        grn = green[p]
        #grn = low
        pixels[p] = (low, grn, brt)
        blue[p] = blue[p] + speed[p] * direction[p]
        if blue[p] >= maximum[p] or blue[p] < 15:
            direction[p] = -1 * direction[p]

        if blue[p] < 15:
            maxi = random.randint(50,255)
            maximum[p] = maxi
            #speed[p] = random.randint(1, 9)
            #green[p] = random.randint(0, 30)

        #pixels[p].blue = 0.6

    #pixels[int(bubble) % num_pixels] = (10, 10, 10)
    bubble = bubble + bubble_speed
    bubble2_idx = int(bubble2) % num_pixels
    #pixels[bubble2_idx] = (low, low, int(blue[bubble2_idx] / 3))
    bubble2 = bubble2 + bubble2_speed
    pixels.show()

'''
    top = random.randint(25, 200)
    step = random.randint(3, 6)
    for i in range(0, top, step):
        #pixels.fill((i, i, i))
        j = i + 15
        pixels[1] = (low, low, i)
        pixels[3] = (low, low, j)
        pixels.show()

    time.sleep(0.5)

    for i in range(top, 0, -1 * step):
        #pixels.fill((i, i, i))
        j = i + 15
        pixels[1] = (low, low, i)
        pixels[3] = (low, low, j)
        pixels.show()
'''

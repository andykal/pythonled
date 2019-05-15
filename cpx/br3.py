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

p = []
ps = []

# initialize
for i in range(0, num_pixels):
    #s = random.randint(1,3)
    s = 9
    d = 1
    maxi = random.randint(50,255)
    m = random.randint(50,250)
    b = random.randint(15, m)
    g = random.randint(0,30)

    m = 250
    b = 1
    g = 10
    p = [s, d, m, b, g]
    ps.append(p)

# main loop
while True:

    for p in range(0, num_pixels):
        #brt = blue[p]
        brt = ps[p][3]
        #grn = int(green[p] * blue[p] / maximum[p])
        grn = ps[p][4]
        #grn = low
        pixels[p] = (low, grn, brt)
        ps[p][3] = ps[p][3] + ps[p][0] * ps[p][1]

        if ps[p][3] >= ps[p][2] or ps[p][3] < 15:
            ps[p][1] = -1 * ps[p][1]

        if ps[p][3] < 15:
            maxi = random.randint(50,255)
            ps[p][2] = maxi


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

# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library

###
### settable Pulse and Cycle
###

import time
import neopixel
import board

try:
    import urandom as random
except ImportError:
    import random

pulse = 1
cycle = 1
# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.1, auto_write=False)
low = 10
num_pixels = 30 
ctr = 0
ctr2 = 0

bubble = float(num_pixels)
bubble_speed = 1.21
bubble2 = 7.0
bubble2_speed = 0.5

p = []
ps = []

# initialize
for i in range(0, num_pixels):
    #s = random.randint(1,3)
    s = 9
    #speed.append(9)
    d = 1
    maxi = random.randint(50,255)
    m = random.randint(50,250)
    #maxi = 245
    b = random.randint(15, m)
    #blue.append(15)
    g = random.randint(0,50)
    p = [s, d, m, b, g]
    ps.append(p)

# main loop
while True:

    for p in range(0, num_pixels):
        #brt = blue[p]
        brt = ps[p][3]
        #grn = int(green[p] * blue[p] / maximum[p])
        #grn = green[p]
        grn = int(ps[p][4] * brt / ps[p][2])
        #grn = ps[p][4]
        #grn = low
        pixels[p] = (low, grn, brt)

        if pulse == 1:
        	ps[p][3] = ps[p][3] + ps[p][0] * ps[p][1]

        if ps[p][3] >= ps[p][2] or ps[p][3] < 15:
            ps[p][1] = -1 * ps[p][1]

        if ps[p][3] < 15:
            maxi = random.randint(60,255)
            ps[p][2] = maxi
            # ps[p][4] = random.randint(0,50) # green reset


    #pixels[int(bubble) % num_pixels] = (10, 10, 10)
    bubble = bubble - bubble_speed
    bubble2_idx = int(bubble2) % num_pixels
    #pixels[bubble2_idx] = (low, low, int(blue[bubble2_idx] / 3))
    bubble2 = bubble2 + bubble2_speed
    pixels.show()

    #ps2 = []
    #ps2[0] = ps[len(ps)-1]
    #for i in range(1, len(ps)-2):
    #  ps2[i] = ps[i-1]

    #ps = ps2
    if cycle == 1:
	    ctr = ctr + 1
	    if ctr > 25:

		    ctr2 = ctr2 + 1
		    if ctr2 > 1:

			    ctr2 = 0
			    pst = list(ps)
			    t1 = pst[0]
			    for i in range(0, len(ps)-1):
			        ps[i] = ps[i + 1]
			    ps[len(ps)-1] = t1

# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library

###
### settable Pulse, Cycle, and Pixels_used
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
cycle_speed = 0 # 0, 1, 2
# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.4, auto_write=False)

num_pixels = 30
pixels_used = 30 # 20
ctr = 0
ctr2 = 0

maxblue = 220
maxgreen = 200
maxred = 20

bubble = float(num_pixels)
bubble_speed = 1.21
bubble2 = 7.0
bubble2_speed = 0.5

p = []
ps = []

# main loop
while True:

    pixels[0] = (100, 100, 100)
    pixels.show()
'''    
    for p in range(0, num_pixels):
        #brt = blue[p]
        brt = ps[p][3]
        #grn = int(green[p] * blue[p] / maximum[p])
        #grn = green[p]
        grn = int(ps[p][4] * brt / ps[p][2])
        #grn = ps[p][4]
	red = random.randint(10,maxred)
        pixels[p] = (red, grn, brt)

        if pulse == 1:
        	ps[p][3] = ps[p][3] + ps[p][0] * ps[p][1]

        if ps[p][3] >= ps[p][2] or ps[p][3] < 15:
            ps[p][1] = -1 * ps[p][1]

        if ps[p][3] < 15:
            maxi = random.randint(60,maxblue)
            ps[p][2] = maxi
            ps[p][4] = random.randint(0,maxgreen) # green reset


    #pixels[int(bubble) % num_pixels] = (10, 10, 10)
    bubble = bubble - bubble_speed
    bubble2_idx = int(bubble2) % num_pixels
    bubble2 = bubble2 + bubble2_speed
    pixels.show()

    # delay to cycle
    if cycle == 1:
	    ctr = ctr + 1
	    if ctr > 25:

		    ctr2 = ctr2 + 1
		    if ctr2 > cycle_speed:

			    ctr2 = 0
			    pst = list(ps)
			    t1 = pst[0]
			    for i in range(0, len(ps)-1):
			        ps[i] = ps[i + 1]
			    ps[len(ps)-1] = t1
'''

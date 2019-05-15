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
#pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.4, auto_write=False)
pixpin = board.D1
#numpix = 7
numpix = 30

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=1.0, auto_write=False)

num_pixels = 30
pixels_used = 30 # 20
ctr = 0
ctr2 = 0

#maxblue = 220
#maxgreen = 200
minblue = 10
mingreen = 10
maxblue = 50
maxgreen = 40
step = 5

bubble = float(num_pixels)
bubble_speed = 1.21
bubble2 = 7.0
bubble2_speed = 0.5

p = []
ps = []

# initialize
for i in range(0, num_pixels):
    #s = random.randint(1,3)
    s = step
    #speed.append(9)
    d = 1
    maxi = random.randint(50,255)
    m = random.randint(50,maxblue)
    ###m = 250 - int(float(i / num_pixels) * pixels_used) * 12
    #maxi = 245
    b = random.randint(15, m)
    ###b = m
    #blue.append(15)
    g = random.randint(0,maxgreen)
    ###g = 0
    p = [s, d, m, b, g]
    if i <= pixels_used:
        ps.append(p)
	#ps.append([9,1,255-i*12-13,255-i*12-13,(255-i*12-13)/10])
    else:
        ps.append([0,0,1,0,0])

# main loop
while True:

    for p in range(0, num_pixels):
        #brt = blue[p]
        brt = ps[p][3]
        #grn = int(green[p] * blue[p] / maximum[p])
        #grn = green[p]
        grn = int(ps[p][4] * brt / ps[p][2])
        #grn = ps[p][4]
	#red = random.randint(10,maxred)
        red = 10
        pixels[p] = (red, grn, brt)

        if pulse == 1:
        	ps[p][3] = ps[p][3] + ps[p][0] * ps[p][1]

        if ps[p][3] >= ps[p][2] or ps[p][3] < 15:
            ps[p][1] = -1 * ps[p][1]

        if ps[p][3] < 15:
            maxi = random.randint(minblue,maxblue)
            nextgreen = random.randint(mingreen,maxgreen)
            if random.randint(1, 50) == 5:
                ps[p][2] = 255 - int(maxi/3)
                #ps[p][4] = random.randint(0,maxgreen) # green reset
                ps[p][4] = 255 - int(nextgreen/3)
                ps[p][0] = step * 2
            else:
                ps[p][2] = maxi
                ps[p][4] = nextgreen
                ps[p][0] = step


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

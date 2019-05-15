# Use the 10 NeoPixels on Circuit Playground Express via the
#   Adafruit neopixel library

import time
import neopixel
import board
import math

try:
    import urandom as random
except ImportError:
    import random

gamma8 = [
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5,
5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10,
10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255 ]

pulse = 0
cycle = 1
cycle_speed = 0 # 0, 1, 2

pixpin = board.D1
numpix = 30

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=1.0, auto_write=False)

num_pixels = 30
pixels_used = 30 # 20

minblue = 10
mingreen = 10
maxblue = 50
maxgreen = 40
step = 5
ctr = 0
ctr2 = 0

p = []
ps = []

# initialize
for i in range(0, num_pixels):
    s = step
    d = 1

    v = 6.28 * i / num_pixels
    s = int((math.sin(v) + 1) / 2 * 255)
    gamma = gamma8[s]
    downstep = random.randint(3, 30)

    print(str(i)+ ", " + str(v) + ", " + str(s) + ", " + str(gamma))



    p = [s, d, gamma, gamma, gamma, downstep]
    if i <= pixels_used:
        ps.append(p)
	#ps.append([9,1,255-i*12-13,255-i*12-13,(255-i*12-13)/10])
    else:
        ps.append([0,0,1,0,0,0])

# main loop
c = 0.0
while True:

    #c = c + 0.1
    #cos = (math.cos(c) + 1.0) / 2
    #sin = (math.sin(c) + 1.0) / 2

    for p in range(0, num_pixels):
        #brt = blue[p]
        brt = ps[p][3]
        downstep = ps[p][5]

        r = brt
        g = max(brt - downstep, 0)
        b = brt

        pixels[p] = (r, g, b)

    pixels.show()

    # delay to cycle

    ctr2 = ctr2 + 1
    if ctr2 > cycle_speed:

	    ctr2 = 0
	    pst = list(ps)
	    t1 = pst[0]
	    for i in range(0, len(ps)-1):
	        ps[i] = ps[i + 1]
	    ps[len(ps)-1] = t1

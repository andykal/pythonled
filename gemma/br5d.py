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
cycle = 0
cycle_speed = 0 # 0, 1, 2

num_pixels = 30
pixels_used = 30 # 20
# Set up the 10 Circuit Playground Express NeoPixels half bright
#CPX_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
#pixels = neopixel.NeoPixel(board.A1, 30, brightness=0.4, auto_write=False)
pixpin = board.D1
#numpix = 7
pixels = neopixel.NeoPixel(pixpin, num_pixels, brightness=.1, auto_write=False)

ctr = 0
ctr2 = 0

minblue = 1
maxblue = 220
mingreen = 10
maxgreen = 80
#maxblue = 50
#maxgreen = 2
minstep = 3
maxstep = 5
pulse_speed = 1

bubble = float(num_pixels)
bubble_speed = 0.5 # 1.
bubble2 = 7.0
bubble2_speed = 0.5

p = []
ps = []

# initialize
for i in range(0, num_pixels):
    step = pulse_speed
    dir = 1
    #maxi = random.randint(50,255)
    peakblue = random.randint(minblue + 10 ,maxblue)
    ###m = 250 - int(float(i / num_pixels) * pixels_used) * 12
    currblue = random.randint(minblue + 11, peakblue)
    peakgreen = random.randint(mingreen,maxgreen)
    #currgreen = random.randint(mingreen - 2, peakgreen)
    currgreen = mingreen
    
    #  step, direction, peakblue, blue, green
    p = [step, dir, peakblue, currblue, peakgreen, currgreen]
    if i <= pixels_used:
        ps.append(p)
	#ps.append([9,1,255-i*12-13,255-i*12-13,(255-i*12-13)/10])
    else:
        ps.append([0,0,1,0,0,0])

# main loop
while True:

    for p in range(0, num_pixels):
        step = 		ps[p][0]
        dir = 		ps[p][1]
        peakblue = 	ps[p][2]
        blue = 		ps[p][3]
        peakgreen = 	ps[p][4]
        green = 	ps[p][5]

        ###green = int(peakgreen * blue / peakblue)
        #green = 0
	
        red = 10
	green = 0
        pixels[p] = (red, green, blue)



        if pulse == 1:
        	#ps[p][3] = ps[p][3] + ps[p][0] * ps[p][1]
		blue = blue + step * dir
		#green = green + step * dir
        	green = int(peakgreen / 2 * blue / peakblue)

#	if (blue >= peakblue and dir == 1) or (blue < 5 and dir == -1):
        #if ps[p][3] >= ps[p][2] or ps[p][3] < 15:
#            dir = -1 * dir
	if (blue >= peakblue):
	    dir = -1 * dir
	    blue = peakblue
	if (blue <= 5):
	    dir = -1 * dir
	    blue = 5
	    peakblue = random.randint(minblue,maxblue)
	    peakgreen = random.randint(mingreen,maxgreen)
	    step = random.randint(minstep,maxstep) #pulse_speed

       # if (blue < 5 and dir == -1): # blue faded out, reset peakblue
       #     peakblue = random.randint(minblue,maxblue)
       #     peakgreen = random.randint(mingreen,maxgreen)
       #     step = random.randint(minstep,maxstep) #pulse_speed
#
#            if random.randint(1, 50) == 55:
#                peakblue = 255 - int(maxi/3)
#                #ps[p][4] = random.randint(0,maxgreen) # green reset
#                peakgreen = 255 - int(nextgreen/3)
#                step = pulse_speed * 2

        ps[p][0] = step
        ps[p][1] = dir
        ps[p][2] = peakblue
        ps[p][3] = blue
        ps[p][4] = peakgreen
        ps[p][5] = green


    ###pixels[int(bubble) % num_pixels] = (30, 255, 30)
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

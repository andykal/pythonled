# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel
import math

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
spixels = neopixel.NeoPixel(board.A1, 30, brightness=0.5)

pixels.fill((0, 0, 0))
pixels.show()

rbow1 = 0
rbow2 = 64
rbow3 = 128
rbow4 = 192

# choose which demos to play
# 1 means play, 0 means don't!
simpleCircleDemo = 0
flashDemo = 0
rainbowDemo = 0
rainbowCycleDemo = 0
rainbowPixels = 1


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))

def rb(pos):
    if pos < 128:
        return(int(pos * 2), 0, 0)
    else:
        pos -= 128
        return (int(255 - pos * 2), 0, int(pos * 2))

def rbrb2(pos):
    # red to purple to blue to purple to red
    if pos < 64:			# RED TO PURPLE
        # begins on 255, 0, 0
        return(255, 0, pos * 4)
        # ends on 255, 0, 255
    elif pos < 128:			# PURPLE TO BLUE
        # begins on 255, 0, 255
        pos -= 64
        return(255 - pos * 4, 0, 255)
        # ends on 0, 0, 255
    elif pos < 192:			# BLUE TO PURPLE
        # begins on 0, 0, 255
        pos -= 128
        return(pos * 4, 0, 255)
        # ends on 255, 0, 255
    else:				# PURPLE TO RED
        # begins on 255, 0, 255
        pos -= 192
        return ( 255, 0, 255 - pos * 4)
        # ends on 255, 0, 0

def rbrb(pos):
    # red to purple to blue to purple to red
    if pos < 64:			# RED TO PURPLE
        # begins on 255, 0, 0
        return(255 - pos * 2, 0, pos * 2)
        # ends on 128, 0, 128
    elif pos < 128:			# PURPLE TO BLUE
        # begins on 128, 0, 128
        pos -= 64
        return(128 - pos * 2, 0, 128 + pos * 2)
        # ends on 0, 0, 255
    elif pos < 192:			# BLUE TO PURPLE
        # begins on 0, 0, 255
        pos -= 128
        return(pos * 2, 0, 255 - pos * 2)
        # ends on 128, 0, 128
    else:				# PURPLE TO RED
        # begins on 128, 0, 128
        pos -= 192
        return ( 128 + pos * 2, 0, 128 - pos * 2)
        # ends on 255, 0, 0

def gbgb(pos):
    # red to purple to blue to purple to red
    if pos < 64:			# RED TO PURPLE
        return(0, 255 - pos * 2, pos * 2)
    elif pos < 128:			# PURPLE TO BLUE
        pos -= 64
        return(0, 128 - pos * 2, 128 + pos * 2)
    elif pos < 192:			# BLUE TO PURPLE
        pos -= 128
        return(0, pos * 2, 255 - pos * 2)
    else:				# PURPLE TO RED
        pos -= 192
        return (0, 128 + pos * 2, 128 - pos * 2)

def rainbow_pixel(wait):
    
    for j in range(255):
        #pixels[0] = wheel(j)
        #pixels[1] = wheel((j + 30) % 255)
        #pixels[1] = wheel((j + 64) % 255)
        #pixels[8] = wheel((j + 128) % 255)
        #pixels[9] = wheel((j + 192) % 255)

        v = j / 255 * 3.14159 * 2
        s = int(math.sin(v) * 128) + 127
        if s < 9:
          print(s)
        pixels[4] = (s, 0, 0)
        pixels[5] = (0, 0, 255-s)

        rb1 = rbrb(j)
        rb2 = rbrb((j + 48) % 255)
        pixels[3] = rb1
        pixels[6] = rb2

        gb1 = gbgb(j)
        gb2 = gbgb((j - 48) % 255)
        pixels[2] = gb1
        pixels[7] = gb2

        rb3 = rbrb2(j)
        rb4 = rbrb2((j + 48) % 255)
        pixels[1] = rb1
        pixels[8] = rb2

        #for i in range(len(pixels)):
        #    idx = int((i * 256 / len(pixels)) + j * 20)
        #    pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int((i * 256 / len(pixels)) + j * 20)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        for i in range(len(spixels)):
            idx = int((i * 256 / len(spixels)) + j * 20)
            spixels[i] = wheel(idx & 255)
        spixels.show()
        #time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()

        for i in range(len(spixels)):
            idx = int((i * 256 / len(spixels)) + j * 20)
            spixels[i] = wheel(idx & 255)
        spixels.show()
        time.sleep(wait)


def simpleCircle(wait):
    RED = 0x100000  # (0x10, 0, 0) also works
    YELLOW = (0x10, 0x10, 0)
    GREEN = (0, 0x10, 0)
    AQUA = (0, 0x10, 0x10)
    BLUE = (0, 0, 0x10)
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range(len(pixels)):
        pixels[i] = RED
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = YELLOW
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = GREEN
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = AQUA
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLUE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = PURPLE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLACK
        time.sleep(wait)
    time.sleep(1)


while True:
    if simpleCircleDemo:
        print('Simple Circle Demo')
        simpleCircle(.05)

    if flashDemo:  # this will play if flashDemo = 1 up above
        print('Flash Demo')
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(.25)

        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(.25)

        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(.25)

        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(.25)

    if rainbowDemo:
        print('Rainbow Demo')
        rainbow(.001)

    if rainbowCycleDemo:
        print('Rainbow Cycle Demo')
        rainbow_cycle(.001)

    if rainbowPixels:
        print('Rainbow Pixels Demo')
        rainbow_pixel(.001)


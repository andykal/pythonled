from adafruit_circuitplayground.express import cpx
 
cpx.pixels.brightness = 0.5
b = 0
 
while True:
#    cpx.pixels[0] = (255, 0, 0)
    cpx.pixels[1] = (0, 0, 255 - b)
    cpx.pixels[5] = (0, b, 0)
#    cpx.pixels[6] = (0, 255, 255)
    cpx.pixels[4] = (b, 255 - b, 0)
    cpx.pixels[3] = (255 - b, 0, b)

    b = (b + 1) % 255

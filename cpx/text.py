from adafruit_circuitplayground.express import cpx  # imports the CPX library from its subfolder

cpx.pixels.brightness = 0.1                     # set pixel brightness
cpx.pixels.fill((0, 0, 0))                          # turns all pixels off
cpx.pixels.show()                                   # sends data to pixels

r = 0
g = 0
b = 255
s = 2
d = 1

br = 0.1
bs = 0.1
bd = 1
#bmax = 0.8
#bmin = 0.2



while True:                            # loop
    if cpx.button_b:                   # if button is pushed then everything in hanging indent is executed
        print("Button B Pressed!")     # prints text in the serial monitor
        cpx.pixels[0] = (255, 0, 0)    # sets a single neopixel to given color pixel[number] = (R,G,B)
        cpx.pixels[1] = (255, 0, 0)
        cpx.pixels[2] = (255, 0, 0)
        cpx.pixels[3] = (255, 0, 0)
        cpx.pixels[4] = (255, 0, 0)

        br = br + bs * bd

        if br > 0.8
            br = 0.8
            bd = bd * -1
        if br < 0.1
            br = 0.1
            bd = bd * -1

        cpx.pixels.brightness = br

    if cpx.button_a:                   # button is pushed
        print("Button A Pressed!")
        cpx.pixels[5] = (r, g, b)
        cpx.pixels[6] = (r, g, b)
        cpx.pixels[7] = (r, g, b)
        cpx.pixels[8] = (r, g, b)
        cpx.pixels[9] = (r, g, b)

        r = (r + s * d) % 128 
        g = (g + s * d) % 128 
        #b = (b + s * 2) % 255
        if r >= 125:
          d = d * -1
          r = 124
          
        if r <= 2:
          d = d * -1
          r = 2

        #cpx.pixels.brightness = br

    if not(cpx.button_a or cpx.button_b):
        cpx.pixels.fill((0, 0, 0))              # will turn the lights off when buttons arent pressed

    cpx.pixels.show()                       # sends accumulated data to pixels

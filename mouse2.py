from pynput.mouse import Controller
from time import sleep

# create a mouse controller
mouse = Controller()

# define the amount to move the mouse (in pixels)
delta_x = 15
delta_y = 10

# loop indefinitely
while True:
    # move the mouse a little bit
    mouse.move(delta_x, delta_y)

    # wait for X sec
    sleep(30)

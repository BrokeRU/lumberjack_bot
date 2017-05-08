from PIL import ImageGrab
import os
import time
from screen_settings import *

def screen_grab():
    box = (x_pad+1, y_pad+1, x_pad+width, y_pad+height)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\snap_' + datetime.now().strftime('%Y-%m-%d %H-%M-%S-%f') + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()

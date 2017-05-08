from PIL import ImageGrab
import os
from datetime import datetime
from screen_settings import *

def screen_grab():
    box = (x_pad+1, y_pad+1, x_pad+width, y_pad+height)
    im = ImageGrab.grab(box)
    pix = im.load()
    
    for y in range((im.height-1), 0, -11):
        # draw left side points
        pix[left_column, y] = (255, 0, 0)
        
        # draw right side points
        pix[right_column, y] = (255, 0, 0)
    
    im.save(os.getcwd() + '\\snap_' + datetime.now().strftime('%Y-%m-%d %H-%M-%S-%f') + '.png', 'PNG')

def main():
    screen_grab()
    print("Done.")

if __name__ == '__main__':
    main()

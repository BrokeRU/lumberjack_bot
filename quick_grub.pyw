from PIL import ImageGrab
import os
from datetime import datetime
from win32api import GetSystemMetrics
from screen_settings import *
import argparse

# Get screen resolution
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

def fullscreen_grab():
    box = (0, 0, screen_width, screen_height)
    im = ImageGrab.grab(box)
    pix = im.load()
    
    # vertical
    for x in range(x_pad+1, x_pad+width):
        pix[x, y_pad+1] = (255, 0, 0)
        pix[x, y_pad+height-1] = (255, 0, 0)
    
    # horizontal
    for y in range(y_pad+1, y_pad+height):
        pix[x_pad+1, y] = (255, 0, 0)
        pix[x_pad+width-1, y] = (255, 0, 0)
    
    im.save(os.getcwd() + '\\snap_' + datetime.now().strftime('%Y-%m-%d %H-%M-%S-%f') + '.png', 'PNG')

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--fullscreen", help="get full screenshot with frames", action="store_true")
    args = parser.parse_args()
    if args.fullscreen:
        fullscreen_grab()
    else:
        screen_grab()
    print("Done.")

if __name__ == '__main__':
    main()

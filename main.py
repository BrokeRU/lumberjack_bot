from PIL import ImageGrab 
import os
import time
from datetime import datetime
import win32api, win32con
import win32com.client
from PIL import ImageOps
from settings import *
from screen_settings import *
import argparse

# argparser
parser = argparse.ArgumentParser(description='Plays LumberJack game automatically. Needs browser window to be visible.')
parser.add_argument("--debug", help="change debug level (correct values are 0,1,2,3)", type=int)
args = parser.parse_args()

# Use debug argument if given
if args.debug is not None:
    debug = args.debug

# Starting points count
points = 0

# Name of dir store screenshots
cur_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# VBScript objects to push keys
shell = win32com.client.Dispatch("WScript.Shell")

def screen_grab():
    box = (x_pad+1, y_pad+1, x_pad+width, y_pad+height)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    return rgb_im


def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")


def start_game():
    # Click to browser to get focus
    mouse_pos((0, 0))
    left_click()
    
    # Press Space to start game
    shell.SendKeys(" ")
    
    time.sleep(.1)
    print("Game started.")


def check_branches():
    # import points from global scope
    global points
    
    im = screen_grab()
    
    # try to save every screenshot taked
    if debug >= 3:
        im.save(os.getcwd() + '\\' + cur_time + '\\scr_' + datetime.now().strftime('%H-%M-%S-%f') + '.png', 'PNG')
    
    # check for tree branches
    for y in range((im.height-1), 0, -11):
        if debug >= 2:
            print("%i:%i" % (left_column, y), im.getpixel((left_column, y)));
            print("%i:%i" % (right_column, y), im.getpixel((right_column, y)));
        
        # check left side for branches
        if im.getpixel((left_column, y)) == tree_color:
            print(points, "RIGHT")
            shell.SendKeys("{RIGHT 2}")
            points += 2
            if points < limit:
                time.sleep(sleep_before_limit)
            else:
                time.sleep(sleep_after_limit)
            break
        # check right side for branches
        elif im.getpixel((right_column, y)) == tree_color:
            print(points, "LEFT")
            shell.SendKeys("{LEFT 2}")
            points += 2
            if points < limit:
                time.sleep(sleep_before_limit)
            else:
                time.sleep(sleep_after_limit)
            break
    else:
        print("Can't parse image correctly!")
        if debug >= 1:
            im.save(os.getcwd() + '\\' + cur_time + '\\error_' + datetime.now().strftime('%H-%M-%S-%f') + '.png', 'PNG')
        time.sleep(sleep_error)
        
        # check for game over
        if im.getpixel((60, 60)) == score_color:
            print("Finish.")
            exit()

def main():
    if debug >= 1:
        print("Created dir:", cur_time)
        os.mkdir(cur_time)
    
    start_game()
    while True:
        check_branches()


if __name__ == '__main__':
    main()
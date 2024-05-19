

import ctypes
import ctypes.wintypes
from ctypes import WinDLL

from ctypes import windll, byref, c_ubyte
from ctypes.wintypes import RECT, HWND

import pyautogui
from collections import namedtuple
import time
from time import perf_counter
import unittest
# from initinterception import sleep
import asyncio
import win32gui
from pytweening import easeInPoly, easeOutPoly, easeInOutPoly
from humancursor import SystemCursor
from helper import Helper
from configparser import ConfigParser
import tkinter as tk
import customtkinter
import threading
from PIL import Image, ImageTk
from datetime import datetime
from datetime import time as dtime    
import os
import gc
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from game import Game
from runesolver import RuneSolver
from action import Action
from initinterception import keydown, keyup, keyupall, sleep, sleeplol
from mss import mss as mss_module
# from mss.windows import MSS as mss
import mss
import mss.tools
import numpy as np
from multiprocessing import JoinableQueue
from multiprocessing import Process
import keyboard as pythonkeyboard
from pynput.mouse import Listener, Button
from pynput import keyboard
import pygetwindow
import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"








# These ctypes structures are for Win32 INPUT, MOUSEINPUT, KEYBDINPUT, and HARDWAREINPUT structures,
# used by SendInput and documented here: http://msdn.microsoft.com/en-us/library/windows/desktop/ms646270(v=vs.85).aspx
# Thanks to BSH for this StackOverflow answer: https://stackoverflow.com/questions/18566289/how-would-you-recreate-this-windows-api-structure-with-ctypes
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ('dx', ctypes.wintypes.LONG),
        ('dy', ctypes.wintypes.LONG),
        ('mouseData', ctypes.wintypes.DWORD),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('time', ctypes.wintypes.DWORD),
        ('dwExtraInfo', ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ('wVk', ctypes.wintypes.WORD),
        ('wScan', ctypes.wintypes.WORD),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('time', ctypes.wintypes.DWORD),
        ('dwExtraInfo', ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ('uMsg', ctypes.wintypes.DWORD),
        ('wParamL', ctypes.wintypes.WORD),
        ('wParamH', ctypes.wintypes.DWORD)
    ]

class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        _fields_ = [
            ('mi', MOUSEINPUT),
            ('ki', KEYBDINPUT),
            ('hi', HARDWAREINPUT),
        ]

    _anonymous_ = ('i', )
    _fields_ = [
        ('type', ctypes.wintypes.DWORD),
        ('i', _I),
    ]
    
user32, kernel32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("kernel32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)

# End of the SendInput win32 data structures.

# def sleep(dur):
#     now = perf_counter()
#     end = now + dur
#     while perf_counter() < end:
#         pass


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

GetDC = windll.user32.GetDC
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
GetClientRect = windll.user32.GetClientRect
CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
SelectObject = windll.gdi32.SelectObject
BitBlt = windll.gdi32.BitBlt
SRCCOPY = 0x00CC0020
GetBitmapBits = windll.gdi32.GetBitmapBits
DeleteObject = windll.gdi32.DeleteObject
ReleaseDC = windll.user32.ReleaseDC















def _mouseMoveDrag(moveOrDrag, x, y, xOffset, yOffset, duration, tween, button=None):    
    def getPointOnLine(x1, y1, x2, y2, n):
        """
        Returns an (x, y) tuple of the point that has progressed a proportion ``n`` along the line defined by the two
        ``x1``, ``y1`` and ``x2``, ``y2`` coordinates.

        This function was copied from pytweening module, so that it can be called even if PyTweening is not installed.
        """
        x = ((x2 - x1) * n) + x1
        y = ((y2 - y1) * n) + y1
        return (x, y)
    MINIMUM_DURATION = 0.1
    MINIMUM_SLEEP = 0.05
    xOffset = int(xOffset) if xOffset is not None else 0
    yOffset = int(yOffset) if yOffset is not None else 0
    if x is None and y is None and xOffset == 0 and yOffset == 0:
        return  # Special case for no mouse movement at all.
    startx, starty = pyautogui.position()
    x = int(x) if x is not None else startx
    y = int(y) if y is not None else starty
    # x, y, xOffset, yOffset are now int.
    x += xOffset
    y += yOffset
    width, height = pyautogui.size()
    # Make sure x and y are within the screen bounds.
    # x = max(0, min(x, width - 1))
    # y = max(0, min(y, height - 1))
    # If the duration is small enough, just move the cursor there instantly.
    steps = [(x, y)]
    if duration > MINIMUM_DURATION:
        # Non-instant moving/dragging involves tweening:
        num_steps = max(width, height)
        sleep_amount = duration / num_steps
        if sleep_amount < MINIMUM_SLEEP:
            num_steps = int(duration / MINIMUM_SLEEP)
            sleep_amount = duration / num_steps
        steps = [getPointOnLine(startx, starty, x, y, tween(n / num_steps)) for n in range(num_steps)]
        # Making sure the last position is the actual destination.
        steps.append((x, y))
    # print(f'{len(steps)=} {steps=} {sleep_amount=} {duration=} {num_steps=} {width=} {height=}')
    print(f'{len(steps)=} {sleep_amount=} {duration=} {num_steps=} {width=} {height=}')
    for tweenX, tweenY in steps:
        if len(steps) > 1:
            # print(f'{steps=} {sleep_amount=}')
            # A single step does not require tweening.
            time.sleep(sleep_amount)
            # await sleep(sleep_amount)
            # sleep(sleep_amount)
        tweenX = int(round(tweenX))
        tweenY = int(round(tweenY))
        print(f'{tweenX=} {tweenY=}')
        ctypes.windll.user32.SetCursorPos(tweenX, tweenY)        
        # pyautogui.leftClick(tweenX,tweenY)
        x,y=pyautogui.position()
        # width, height = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        width, height = 1920, 1080
        convertedX = 65536 * x // width + 1
        convertedY = 65536 * y // height + 1
        ctypes.windll.user32.mouse_event(0x0002, ctypes.c_long(convertedX), ctypes.c_long(convertedY), 0, 0)
        ctypes.windll.user32.mouse_event(0x0004, ctypes.c_long(convertedX), ctypes.c_long(convertedY), 0, 0)
        # time.sleep(.5)
        # pyautogui.mouseDown(tweenX,tweenY)
class P(namedtuple("P", ["x", "y"])):
    """Simple, immutable, 2D point/vector class, including some basic
    arithmetic functions.
    """

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)

    def __repr__(self):
        return "P({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return P(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return P(self.x // other, self.y // other)

    def __truediv__(self, other):
        return P(self.x / other, self.y / other)

    def __neg__(self):
        return P(-self.x, -self.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return P(abs(self.x), abs(self.y))
class MyMouse(unittest.TestCase):

    TWEENS = [
        # "linear",
        # "easeInElastic",
        # "easeOutElastic",
        # "easeInOutElastic",
        # "easeInBack",
        # "easeOutBack", # this so good
        # "easeInOutBack", # this
        # "easeInBounce",
        # "easeOutBounce", # this
        # "easeInOutBounce",
        # "easeInPoly",
        # "easeOutPoly",
        # "easeInOutPoly",
        # "easeInCirc",
        # "easeOutCirc", # not bad
        "easeInOutCirc", # actually not bad, start slow end slow, mid fast
        # "easeInExpo",
        # "easeOutExpo", # good, start fast end slow
        # "easeInOutExpo", # good, start very slow, end very slow
        # "easeInSine",
        # "easeOutSine", # nothing special
        # "easeInOutSine",
        # "easeInQuint",
        # "easeOutQuint",
        # "easeInOutQuint", # not bad, start slow, end slow
        # "easeInQuart",
        # "easeOutQuart",
        # "easeInOutQuart",
        # "easeInCubic",
        # "easeOutCubic",
        # "easeInOutCubic",
        # "easeInQuad",
        # "easeOutQuad",
        # "easeInOutQuad",
    ]
    
    def setUp(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        self.center = P(*pyautogui.size()) // 2
        self.humancursor = SystemCursor()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(*self.center)  # make sure failsafe isn't triggered during this test
        pyautogui.FAILSAFE = True

    def test_moveToWithTween(self):
        # origin = self.center - P(100, 100)
        # destination = self.center + P(100, 100)
        origin = self.center - P(200, -200)
        destination = self.center + P(200, -200)
        print(f'{origin=} {destination=}')

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            # tweenFunc = easeOutPoly
            print(tweenName)
            resetMouse()
            now=perf_counter()
            # pyautogui.moveTo(destination.x, destination.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            # pyautogui.moveTo(destination.x, destination.y, duration=1 * 2, tween=tweenFunc)
            # x, y = pyautogui._normalizeXYArgs(destination.x, destination.y)
            # _mouseMoveDrag("move", x, y, 0, 0, 1., tweenFunc)
            self.humancursor.move_to((destination.x,destination.y))
            print(f'{(perf_counter()-now)=}')
            mousepos = P(*pyautogui.position())
            pyautogui.leftClick(mousepos)
            self.assertEqual(
                mousepos,
                destination,
                "%s tween move failed. mousepos set to %s instead of %s" % (tweenName, mousepos, destination),
            )
            
    def test_moveRelWithTween(self):
        origin = self.center - P(200, -200)
        delta = P(400, -400)
        destination = origin + delta

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            # tweenFunc = easeOutPoly
            print(tweenName)
            resetMouse()
            now=perf_counter()
            # pyautogui.moveRel(delta.x, delta.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            # pyautogui.moveRel(delta.x, delta.y, duration=1 * 2, tween=tweenFunc)
            x, y = pyautogui._normalizeXYArgs(delta.x, delta.y)
            _mouseMoveDrag("move", None, None, x, y, 1.*2, tweenFunc)
            print(f'{(perf_counter()-now)=}')
            mousepos = P(*pyautogui.position())
            pyautogui.leftClick(mousepos)
            self.assertEqual(
                mousepos,
                destination,
                "%s tween move failed. mousepos set to %s instead of %s" % (tweenName, mousepos, destination),
            )
class Aclass():

    def __init__(self,g=0) -> None:
        self.g=g
        pass

    def getg(self):
        return self.g

    def setg(self,g):
        self.g=g

    def printg(self):
        print(f'{self.g=}')
class Bclass():

    def __init__(self,g=0) -> None:
        self.g=g
        pass

    def getg(self):
        return self.g

    def setg(self,g):
        self.g=g

    def printg(self):
        print(f'{self.g=}')
class mytkinter(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.config2 = ConfigParser()
        self.config2.read('secret.ini')
        self.TOKEN = self.config2.get('telegram', 'TOKEN')
        self.telegram_keep_alive = True
        self.loop1 = asyncio.new_event_loop()
        self.loop2 = asyncio.new_event_loop()
        self.loop3 = asyncio.new_event_loop()
        # self.loop4 = asyncio.new_event_loop()
        # self.loop5 = asyncio.new_event_loop()
        # self.loop6 = asyncio.new_event_loop()
        self.thread1 = threading.Thread(target=self.run_thread1)
        self.thread2 = threading.Thread(target=self.run_thread2)
        self.thread3 = threading.Thread(target=self.run_thread3)
        # self.thread6 = threading.Thread(target=self.run_thread6)
        pass

    def run_threads(self):
        pass

    def join_threads(self):
        pass


    def run_thread1(self):
        asyncio.set_event_loop(self.loop1)
        self.loop1.run_until_complete(self.async_function("Thread 1", 5)) # telegram thread

    def run_thread2(self):
        asyncio.set_event_loop(self.loop2)
        self.loop2.run_until_complete(self.async_function2("Thread 2", 5)) # tkinter init thread

    def run_thread3(self):
        asyncio.set_event_loop(self.loop3)
        self.loop3.run_until_complete(self.async_function3("Thread 3", 5)) # main thread


    def start_threads(self):
        # Start both threads
        self.thread1.start()
        # self.thread2.start()
        self.thread3.start()
        pass

    def wait_for_threads(self):
        # Wait for both threads to finish
        self.thread1.join()
        print(f'thread1 joined. ')
        # self.thread2.join()
        # print(f'thread2 joined. ')
        self.thread3.join()
        print(f'thread3 joined. ')
        # self.thread6.join()
        # print(f'thread6 joined. ')
        pass


    async def async_function(self, thread_name, iterations):
        print(f'bot has started1 ..')
        try:
            # self.application = Application.builder().token(self.TOKEN).build()
            # # self.application.add_handler(CommandHandler('status', self.status_command))
            # # self.application.add_error_handler(self.error)
            # await self.application.initialize()
            # await self.application.start()
            # await self.application.updater.start_polling()
            # self.telegram_started = True
            while self.telegram_keep_alive:
                await asyncio.sleep(1)  # Simulating asynchronous work
            print(f'finished telegram_run1')
            # await self.application.updater.stop()
            # await self.application.stop()
            # await self.application.shutdown()
            print(f'finished telegram_run2')
        except Exception as e:
            print(f'{e=}')
            self.acc_not_bind = True
            self.telegram_started = True
        finally:
            print(f'exiting telegram thread ..')
        
    async def async_function2(self, thread_name, iterations):
        print(f'bot has started2 ..')
        self.root = customtkinter.CTk()
        # self.root.title("chrome")
        # self.root.iconpath = ImageTk.PhotoImage(file=os.path.join("icon.ico"))
        # self.root.wm_iconbitmap()
        # self.root.iconphoto(False, self.root.iconpath)
        # self.screen_width = self.root.winfo_screenwidth()
        # self.screen_height = self.root.winfo_screenheight()
        # window_width = 600
        # window_height = 800
        # window_x = self.screen_width - window_width
        # window_y = 0
        # self.root.geometry(f"{window_width}x{window_height}+{window_x-10}+{window_y}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.tkinter_started=True
        self.root.mainloop()
            
    def on_close(self):
        print("Closing the window")
        self.telegram_keep_alive = False
        self.destroy()
        self.thread1.join()
        print(f'thread1 joined. ')
        self.thread3.join()
        print(f'thread3 joined. ')
        # self.root=None
        # gc.collect()

    async def async_function3(self, thread_name, iterations):
        print(f'bot has started3 ..')






async def main():
    print("Main function started")

    # mtkinter=mytkinter()
    # mtkinter.start_threads()
    # # mtkinter.wait_for_threads()
    # mtkinter.protocol("WM_DELETE_WINDOW", mtkinter.on_close)
    # mtkinter.mainloop()
    
    # mymouse = MyMouse()
    # mymouse.setUp()
    # print(f'testing test_moveToWithTween')
    # time.sleep(1)
    # mymouse.test_moveToWithTween()
    # print(f'finished test_moveToWithTween. ')
    # # time.sleep(2)
    # print(f'testing test_moveRelWithTween')
    # # time.sleep(1)
    # # mymouse.test_moveRelWithTween()
    # print(f'finished test_moveRelWithTween. ')
    # print("Main function completed")

    # runesolver = RuneSolver()
    # maplehwnd=None
    # chathwnd=None
    # hwnd = 0
    # windows=[]
    # while True:
    #     print(f'{hwnd}')
    #     hwnd = win32gui.FindWindowEx(0,hwnd,None, "MapleStory")
    #     if hwnd == 0:
    #         break
    #     windows.append(hwnd)
    # for windowhwnd in windows:
    #     position = win32gui.GetWindowRect(windowhwnd)
    #     x, y, w, h = position
    #     if w-x == 410:
    #         chathwnd=windowhwnd
    #     else:
    #         maplehwnd=windowhwnd            
    #         runesolver.set_maplehwnd(maplehwnd)
    #         print(f'{maplehwnd}')
    #     print(f'{x} {y} {w} {h}')
    # he = Helper()
    # for i in range(10):
    #     # await he.move_to_and_click(x+100,y+100)
    #     await runesolver.mock()
    #     time.sleep(3)
    #     print(f'done')

    # for i in range(10):
    #     action = Action()
    #     await action.testnpc()
    #     print(f'pressed. ')
    #     time.sleep(1)

    # async def func(a,b):
    #     return a,b    
    # async def func2(a,b):
    #     return await func(a,b)
    # a,b = await func2(1,2)
    # print(a,b)

    # import os
    # # Path to the directory containing JSON files
    # folder_path = "json"
    # # Get a list of all files in the directory
    # file_list = os.listdir(folder_path)
    # # Filter out the JSON files
    # json_files = [file for file in file_list if file.endswith(".json")]
    # # Get the number of JSON files
    # num_json_files = len(json_files)
    # # Append the file names to an array of strings
    # json_file_names = [os.path.splitext(file)[0] for file in json_files]
    # print("Number of JSON files:", num_json_files)
    # print("File names:", json_file_names)
    # print("json_files:", json_files)

    # config = ConfigParser()
    # config.read('settings.ini')
    # atk = config.get('keybind', 'attack')
    # jump = config.get('keybind', 'jump')
    # teleport = config.get('keybind', 'teleport')
    # ropeconnect = config.get('keybind', 'ropeconnect')
    # npc = config.get('keybind', 'npc')
    # fountain = config.get('keybind', 'fountain')
    # print(atk, jump, teleport, ropeconnect, npc, fountain)

    # # root = tk.Tk()
    # root = customtkinter.CTk()
    # root.geometry("800x600")
    # frame = tk.Frame(root, height=100,width=200,bg="grey")
    # frame.pack()
    # # frame.grid_propagate(0)
    # # frame.grid_columnconfigure(0,weight=1)
    # # # frame.grid(row=1,column=0)
    # # frame.grid_rowconfigure(0,weight=1)
    # # def add():
    # #     tk.Entry(frame).grid()
    # # def disable():
    # #     frame.configure(height=frame["height"],width=frame["width"])
    # #     frame.grid_propagate(0)
    # # def enable():
    # #     frame.grid_propagate(1)
    # # # tk.Button(root, text="add widget", command=add).grid(row=0,column=0)
    # # # tk.Button(root, text="disable propagation", command=disable).grid(row=0,column=1)
    # # # tk.Button(root, text="enable propagation", command=enable).grid(row=0,column=2)
    # # # tk.Button(frame,bg='#123456',text='resume').grid(row=0,column=0,sticky='ne')
    # # tk.Frame(frame, height=50,width=75,bg="blue").grid(row=0,column=0,sticky='ne')
    # # tk.Frame(frame, height=50,width=75,bg="red").grid(row=1,column=0,sticky='ne')
    # # tk.Frame(frame, height=50,width=75,bg="yellow").grid(row=2,column=0,sticky='ne')
    # # tk.Frame(frame, height=50,width=75,bg="green").grid(row=3,column=0,sticky='ne')
    # # slider1 = customtkinter.CTkSlider(frame,from_=0,to=100,orientation='horizontal',number_of_steps=100,command=None)
    # # slider1.grid(row=4,column=0)    
    # def minus():
    #     pass
    # def plus():
    #     pass
    # def minus2():
    #     pass
    # def plus2():
    #     pass
    # frame2 = customtkinter.CTkFrame(root, width=400, height=300)
    # frame2.pack(padx=1, pady=1)
    # widthframe = customtkinter.CTkFrame(frame2, fg_color="transparent", bg_color='#123fec',height=5, width=20)
    # widthframe.grid(row=0, column=0, padx=(1, 1), pady=1)
    # # widthframe.grid_columnconfigure((0, 2), weight=0)   # buttons don't expand
    # # widthframe.grid_columnconfigure(1, weight=0)        # entry expands
    # # widthsub = customtkinter.CTkButton(widthframe, text="-", command=minus,width=10, height=10)
    # # widthsub.grid(row=0, column=0, padx=(1, 1), pady=1, sticky='w')
    # # widthentry = customtkinter.CTkEntry (widthframe, width=15, height=5, border_width=1,justify='right')
    # # widthentry.grid(row=0, column=1, padx=(1, 1), pady=1, sticky='we')
    # # widthadd = customtkinter.CTkButton(widthframe, text="+", command=plus,width=10, height=10)
    # # widthadd.grid(row=0, column=2, padx=(1, 1), pady=1, sticky='w')
    # heightframe = customtkinter.CTkFrame(frame2, fg_color="transparent", bg_color='#1f3f3c',height=5, width=20)
    # heightframe.grid(row=0, column=1, padx=(1, 1), pady=1)
    # # heightframe.grid_columnconfigure((0, 2), weight=0)   # buttons don't expand
    # # heightframe.grid_columnconfigure(1, weight=0)        # entry expands
    # # heightsub = customtkinter.CTkButton(heightframe, text="-", command=minus2,width=10, height=10)
    # # heightsub.grid(row=0, column=0, padx=(1, 1), pady=1, sticky='w')
    # # heightentry = customtkinter.CTkEntry (heightframe, width=15, height=5, border_width=1,justify='right')
    # # heightentry.grid(row=0, column=1, padx=(1, 1), pady=1, sticky='we')
    # # heightadd = customtkinter.CTkButton(heightframe, text="+", command=plus2,width=10, height=10)
    # # heightadd.grid(row=0, column=2, padx=(1, 1), pady=1, sticky='w')
    # buttonframe = customtkinter.CTkFrame(frame2, fg_color="transparent", bg_color='#f233ec',height=5, width=20)
    # buttonframe.grid(row=0, column=2, padx=(1, 1), pady=1)
    # # button2 = customtkinter.CTkButton(frame, text="adjust", command=self.button_adjustminimap)
    # # button2.grid(row=0, column=0, padx=(1,0), pady=(0,1))
    # root.mainloop()

    # a='b'
    # x=0
    # y=None
    # try:
    #     x=int(a)
    # except Exception as e:
    #     print(f'{e=}')
    # print(x)
    # print(a)
    # print(y)
    
    # aclass = Aclass()
    # bclass = Bclass()
    # bclass.setg(9.81)
    # aclass.setg(bclass.getg())
    # aclass.printg()
    # bclass.setg(8.81)
    # aclass.printg()

    # class MyClass2:
    #     def __init__(self) -> None:
    #         # self.class1 = MyClass()
    #         # self.class1.set_values(10, "hello")
    #         pass
    #     def set_values(self, arg1=None, arg2=None):
    #         self.arg1 = arg1
    #         self.arg2 = arg2
    #     def setclass1(self, l,r,t,b,classtype,arg1=None, arg2=None):
    #         self.l=l
    #         self.r=r
    #         self.t=t
    #         self.b=b
    #         self.class1=MyClass()
    #         self.class1.set_values(arg1,arg2)
    #     def printclass1(self):
    #         print(self.class1.arg1, self.class1.arg2)  # Output: None world
    # class MyClass:
    #     def __init__(self) -> None:
    #         self.arg1=None
    #         self.arg2=None
    #     def set_values(self, arg1, arg2):
    #         if arg1 is not None:
    #             self.arg1 = arg1
    #         if arg2 is not None:
    #             self.arg2 = arg2
    # # obj = MyClass()
    # obj2 = MyClass2()
    # # obj2.set_values(10, "hello")
    # # obj2.printclass1()
    # # obj2.setclass1(arg1=None,arg2='hhh')
    # obj2.setclass1(l=0,r=1,t=2,b=3,classtype='meow',arg2='hhh')
    # obj2.printclass1()
    # obj2.setclass1(l=0,r=1,t=2,b=3,classtype='woof',arg1=11)
    # obj2.printclass1()
    # # obj.set_values(10, "hello")
    # # print(obj.arg1, obj.arg2)  # Output: 10 hello
    # # obj.set_values(20, None)
    # # print(obj.arg1, obj.arg2)  # Output: 20 None
    # # obj.set_values(None, "world")
    # # print(obj.arg1, obj.arg2)  # Output: None world

    # for i in range(10):
    #     print(f'keydown shift')
    #     keydown('altleft')
    #     await sleep(.1)
    #     print(f'keyup shift')
    #     keyup('altleft')
    #     await sleep(.1)

    # ZONE = 5
    # WIDTH, HEIGHT = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]    
    # GRAB_ZONE = (
    #     int(WIDTH / 2 - ZONE),
    #     int(HEIGHT / 2 - ZONE),
    #     int(WIDTH / 2 + ZONE),
    #     int(HEIGHT / 2 + ZONE),
    # )
    # print(GRAB_ZONE)
    # color_tolerance = 70
    # R, G, B = (68, 221, 255)  # player
    # # R, G, B = (250, 100, 250)  # purple
    # sct = mss_module()
    # g = Game((8, 63, 200, 140)) #
    # while True:
    #     # now=perf_counter()
    #     # x = g.get_player_location()
    #     # x = g.pure_test()
    #     # print(x)
    #     # time.sleep(1)
    #     with mss() as sctt:
    #         for _ in range(100):
    #             now=perf_counter()
    #             sctt.shot()
    #             print(f'{perf_counter()-now:.10f}')
    #     # img = np.array(sct.grab(GRAB_ZONE))
    #     # pmap = np.array(img)
    #     # pixels = pmap.reshape(-1, 4)
    #     # color_mask = (
    #     #         (pixels[:, 0] > R -  color_tolerance) & (pixels[:, 0] < R +  color_tolerance) &
    #     #         (pixels[:, 1] > G -  color_tolerance) & (pixels[:, 1] < G +  color_tolerance) &
    #     #         (pixels[:, 2] > B -  color_tolerance) & (pixels[:, 2] < B +  color_tolerance)
    #     #     )
    #     # matching_pixels = pixels[color_mask]
    #     # if len(matching_pixels) > 0:
    #     #     print(f'found')
    #     # print(f'{perf_counter()-now:.10f}')
    #     time.sleep(1)
    
    # a=True
    # while True:
    #     if a==True:
    #         a=False
    #         kernel32.Beep(440, 75), kernel32.Beep(700, 100)
    #     else:
    #         a=True
    #         kernel32.Beep(440, 75), kernel32.Beep(200, 100)
    #     time.sleep(1)
    
    # while True:
    #     if pythonkeyboard.is_pressed("f10"):
    #         print(f'yes')
    #     else:
    #         print(f'no')
    #     time.sleep(1)

    # def grab(queue: JoinableQueue) -> None:
    #     rect = {"top": 0, "left": 0, "width": 600, "height": 800}
    #     with mss.mss() as sct:
    #         for _ in range(1_000):
    #             queue.put(sct.grab(rect))
    #     # Tell the other worker to stop
    #     queue.put(None)
    # def save(queue: JoinableQueue) -> None:
    #     number = 0
    #     output = "screenshots/file_{}.png"
    #     to_png = mss.tools.to_png
    #     while "there are screenshots":
    #         img = queue.get()
    #         if img is None:
    #             break
    #         to_png(img.rgb, img.size, output=output.format(number))
    #         number += 1
    # queue: JoinableQueue = JoinableQueue()
    # Process(target=grab, args=(queue,)).start()
    # Process(target=save, args=(queue,)).start()
    
    # current_time = datetime.now().time()    
    # one_am = dtime(1, 54, 0)  #
    # cur_am = dtime(1, 55, 0)  #
    # six_am = dtime(6, 30, 30)  # Creating a time object for 6 AM
    # print(current_time.hour-one_am.hour)
    # print(current_time.minute-one_am.minute)
    # print(current_time.second-one_am.second)
    # print(current_time.microsecond-one_am.microsecond)
    # print(cur_am>=one_am and cur_am<=six_am)

    # def myfunc1():
    #     return (True, False)
    # def myfunc2():
    #     return True, False
    # def myfunc3():
    #     return [True, False]
    # now=perf_counter()
    # a=myfunc1()
    # now2=perf_counter()
    # b=myfunc2()
    # now3=perf_counter()
    # c=myfunc3()
    # now4=perf_counter()
    # print(f'n2={now2-now:.10f} n3={now3-now2:.10f} n4={now4-now3:.10f}')
    # print(f'{a=} {b=} {c=}')
    # print(f'{type(a)=} {type(b)=} {type(c)=}')

    # file_path = r'C:\Windows\system32\drivers\keyboard.sys'
    # try:
    #     with open(file_path, 'rb') as file:
    #         content = file.read()
    #         print(content)
    # except FileNotFoundError:
    #     print("keyboard.sys file not found.")
    # except PermissionError:
    #     print("Permission denied. Make sure you have appropriate permissions to read the file.")
    # except Exception as e:
    #     print("An error occurred:", e)
    
    # while True:
    #     for i in range(10):
    #         keydown('a')
    #         # keyup('a')
    #         keyupall()
    #         time.sleep(.1)
    #     print(f'end. ')

    # while True:
    #     for i in range(100):
    #         now=perf_counter()
    #         # time.sleep(.001)
    #         # await sleep(.001)
    #         sleeplol(.001)
    #         print(f'{perf_counter()-now:.10f}')
    #     # break

    # maplehwnd=0
    # windows=[]
    # winlist=[]
    # winlist = pygetwindow.getWindowsWithTitle('MapleStory')
    # for w in winlist:
    #     windows.append(w._hWnd)
    # print(f'{winlist=}')
    # print(f'{windows=}')
    # for windowhwnd in windows:
    #     position = win32gui.GetWindowRect(windowhwnd)
    #     x, y, w, h = position
    #     print(f'{windows=} {w-x=}')
    #     if w-x == 1936 or w-x == 1382 or w-x == 1296 or w-x == 1040 or w-x == 816:
    #         maplehwnd=windowhwnd
    #     elif w-x == 1938 or w-x == 1384 or w-x == 1298 or w-x == 1042 or w-x == 818: # some windows 10
    #     # elif w-x == 1944 or w-x == 1390 or w-x == 1298 or w-x == 1042 or w-x == 818: # japanese maplestory JMS
    #         maplehwnd=windowhwnd
    # position = win32gui.GetWindowRect(maplehwnd)
    # x0, y0, w, h = position
    # def on_press(key):
    #     if key == keyboard.Key.esc:
    #         print(f'esc')
    #         mouse_listener.stop()
    #         return False
    # def on_click(x, y, button, pressed):
    #     if pressed and button == Button.left:
    #         print(f'{x=} {y=} {x0=} {y0=} {x-x0=} {y-y0=}')
    # mouse_listener = Listener(on_click=on_click)
    # mouse_listener.start()
    # with keyboard.Listener(on_press=on_press) as listener:
    #     try:
    #         listener.join()
    #     except Exception as e:
    #         print(f'exception. {e=}')
    
    # img_rgb = cv2.imread('../image/1.png')
    # assert img_rgb is not None, "file could not be read, check with os.path.exists()"
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # template = cv2.imread('sealed_rune.png', cv2.IMREAD_GRAYSCALE)
    # assert template is not None, "file could not be read, check with os.path.exists()"
    # w, h = template.shape[::-1]    
    # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # threshold = 0.8
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #     cv2.imwrite('../image/res.png',img_rgb)

    # # 开始截图
    # handle = user32.FindWindowW(None, "MapleStory")
    # r = RECT()
    # GetClientRect(handle, byref(r))
    # width, height = r.right, r.bottom
    # dc = GetDC(handle)
    # cdc = CreateCompatibleDC(dc)
    # bitmap = CreateCompatibleBitmap(dc, width, height)
    # SelectObject(cdc, bitmap)
    # while True:
    #     if pythonkeyboard.is_pressed("esc"):
    #         print(f'break'); break
    #     now=perf_counter()
    #     BitBlt(cdc, 0, 0, width, height, dc, 0, 0, SRCCOPY)
    #     # 截图是BGRA排列，因此总元素个数需要乘以4
    #     total_bytes = width*height*4
    #     buffer = bytearray(total_bytes)
    #     byte_array = c_ubyte*total_bytes
    #     GetBitmapBits(bitmap, total_bytes, byte_array.from_buffer(buffer))
    #     img = np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, 4)
    #     print(f'{perf_counter()-now:.10f}')
    #     cv2.imshow('img',img)
    #     cv2.waitKey(1)
    # DeleteObject(bitmap)
    # DeleteObject(cdc)
    # ReleaseDC(handle, dc)
    # # 返回截图数据为numpy.ndarray
    # # return np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, 4)
    # cv2.destroyAllWindows()

    # sequence = (1,2,3,4,5,6,7,8)
    # print(sequence)

    # ## https://www.youtube.com/watch?v=HHHkh9IOqhI
    # tessdata_dir_config = r'--tessdata-dir "C:\\Program Files\\Tesseract-OCR"'
    # g = Game((8, 63, 200, 150)) #
    # # img = g.get_screenshot()
    # # img = cv2.imread("score.png")
    # # img = cv2.imread("../image/34.png")    
    # # img = cv2.imread("../image/pytesseract.png")    
    # # img = cv2.imread("../image/2/4275__.png")    
    # img = cv2.imread("../image/3/49.png")    
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)    
    # img = cv2.bitwise_not(img)
    # print(f'{type(img)=}')
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # while True:
    #     try:
    #         now=perf_counter()
    #         # imgstring = pytesseract.image_to_string(img, lang='eng')
    #         # imgstring = pytesseract.image_to_string(img, config='--psm 6 --tessdata-dir \"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"')
    #         # imgstring = pytesseract.image_to_string(img, config='--psm 6')
    #         # imgstring = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    #         # imgstring = pytesseract.image_to_string(img, config='--psm 6 digits')
    #         imgstring = pytesseract.image_to_string(img, config='--psm 6 --oem 3 digits')
    #         print(f"PYTESSERACT!!!!!!!!! = {imgstring} {perf_counter()-now:.10f}")
    #         # g.read_score()
    #         time.sleep(.5)
    #     except Exception as e:
    #         print(f'pytesseract e: {e=}')




# Run the event loop
if __name__ == "__main__":    
    asyncio.run(main())
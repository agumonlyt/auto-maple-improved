# import ctypes
# import ctypes.wintypes
# from ctypes import WinDLL
# from ctypes import windll, byref, c_ubyte
# from ctypes.wintypes import RECT, HWND
# import pyautogui
# from collections import namedtuple
import time
from time import perf_counter
# import unittest
# # from initinterception import sleep
import asyncio
# import win32gui
# from pytweening import easeInPoly, easeOutPoly, easeInOutPoly
# from humancursor import SystemCursor
# from helper import Helper
# from configparser import ConfigParser
import customtkinter
import tkinter as tk
# import threading
# from PIL import Image, ImageTk
# from datetime import datetime
# from datetime import time as dtime    
# import os
# import gc
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# from game import Game
# from runesolver import RuneSolver
# from action import Action
from initinterception import keydown, keyup, keyupall, keydown_arrow, keyup_arrow, keyupall_arrow
import random
# from mss import mss as mss_module
# # from mss.windows import MSS as mss
# import mss
# import mss.tools
# import numpy as np
# from multiprocessing import JoinableQueue
# from multiprocessing import Process
# import keyboard as pythonkeyboard
# from pynput.mouse import Listener, Button
# from pynput import keyboard
import pygetwindow
# import cv2
# # import pytesseract
# # pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"




def sleep(dur): # async is not needed buddy. :))
    now = perf_counter()
    end = now + dur
    while perf_counter() < end:
        pass








class Decepticlone(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("800x600")
        self.title("chrome")
                
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # frame = customtkinter.CTkFrame(self)
        frame = customtkinter.CTkScrollableFrame(self)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        
        frame2 = customtkinter.CTkFrame(self)
        frame2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=1)
        frame2.grid_columnconfigure(2, weight=1)
        
        self.rows=[]
        self.comboboxes=[]
        self.entries=[]
        self.numcount=0
        def on_button_click():
            onerow=[]
            options = ["keydown", "keyup"]
            combobox = customtkinter.CTkComboBox(master=frame, values=options, width=100)
            combobox.grid(row=self.numcount, column=0, padx=1, pady=1)  # Place combobox
            self.comboboxes.append(combobox)
            onerow.append(combobox)

            for i in range(1,4):
                entry = customtkinter.CTkEntry(frame, width=100)
                entry.grid(row=self.numcount, column=i, padx=1, pady=1)
                self.entries.append(entry)
                onerow.append(entry)
            self.numcount+=1
            self.rows.append(onerow)
        button = customtkinter.CTkButton(frame2, text="Create New Function", command=on_button_click)
        button.grid(row=0,column=1,pady=(5,0))        
        def btnprint():
            for i in range(10):
                for row in self.rows:
                    button=row[0].get()
                    code=row[1].get()
                    x=float(row[2].get())/1000
                    y=float(row[3].get())/1000
                    if button == 'keydown':
                        self.bum(code,x,y)
                    else: # keyup
                        self.bum_(code,x,y)
        button2 = customtkinter.CTkButton(frame2, text="Print", command=btnprint)
        button2.grid(row=2,column=1,pady=5)

        self.mainloop()
        
    def bum(self, code, x=.031, y=.131):
        keydown(code); sleep(random.uniform(x,y))

    def bum_(self, code, x=.031, y=.131):
        keyup(code); sleep(random.uniform(x,y))

    def btnprint(self):
        for i in range(10):
            for row in self.rows:
                button=row[0].get()
                code=row[1].get()
                x=float(row[2].get())/1000
                y=float(row[3].get())/1000
                if button == 'keydown':
                    self.bum(code,x,y)
                else: # keyup
                    self.bum_(code,x,y)


async def main():
    print("Main function started")
    
    decepticlone = Decepticlone()





# Run the event loop
if __name__ == "__main__":    
    asyncio.run(main())
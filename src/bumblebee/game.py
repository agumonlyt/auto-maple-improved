import gdi_capture
import numpy as np
import cv2
import time
from time import perf_counter
# from PIL import ImageGrab
# import win32gui
# import pygetwindow
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

alpha=255
# alpha=0
# These are colors taken from the mini-map in BGRA format.
PLAYER_BGRA = (68, 221, 255, alpha)
RUNE_BGRA = (255, 102, 221, alpha)
ENEMY_BGRA = (0, 0, 255, alpha)
GUILD_BGRA = (255, 102, 102, alpha)
BUDDY_BGRA = (225, 221, 17, alpha)

EB3BGR = (0, 34, 204, alpha)
EBBGR = (238, 255, 255, alpha) # yellow timer (x+405, y+75, x+406, y+76) (397,44)
LDBGR = (136, 51, 170, alpha)
RDBGR = (0, 0, 255, alpha)
GDBGR = (221, 170, 170, alpha)
WDBGR = (255, 255, 255, alpha)
DCBGR = (187, 221, 238, alpha)
OKBGR = (17,187,170, alpha) # broid die #normalpc
# OKBGR = (17,187,153, alpha) # broid die 
# OKBGR = (0,187,170, alpha) # died_ok [0 187 170] [0 204 153]
ORBGR = (1,136,245, alpha) # orange_mushroom [1 136 245] [] #normalpc
DCBGR = (206,143,16, alpha) # first pixel of login screen (0,0) indicate that YOU HAVE DC-ED!!!
LOBGR = (17,170,136, alpha) # 
RUNECDBGR = (157,157,158, alpha) # the range is between 15x to 160 ???????
RUNECD2BGR = (73,74,76, alpha) # the range is between 15x to 160 ???????
# POBGR = (17,85,238, alpha) # 
POBGR = (102,136,255, alpha) # 
PO2BGR = (0,0,255, alpha) # 
VIBGR = (136,57,170, alpha) # violetta detector (x+701, y+472, x+702, y+473) (693,441)
SWBGR = (238,255,255, alpha) # storming will always be 0 stormwing habitat detector (timer) (221,255,255, 255) (x+405, y+75, x+406, y+76) (397,44)
ESBGR = (51,187,255, alpha) # especia please use the dot especia detector (timer) (221,255,255, 255) (x+405, y+75, x+406, y+76) (397,44)
TIBGR = (204,204,204, alpha) # timer gray dot (304,48)
GMBGR = (222,218,206, alpha) # 
DABGR = (0,0,0, alpha) # 
ARDENTBGR = (17,85,170, alpha) # # the icon of the ardent minimap, there is this orange-ish brown roofttop in the tiny icon. 
ROBGR = (187,187,204, alpha) # mapril island infinity race rock light brown bgr value
KITCHENBGR = (0,0,204,alpha) # mapril island kitchen minigame red color angry chef
UPBGR = (0,136,187,alpha) # mapril island kitchen minigame UP 
DOWNBGR = (119,51,187,alpha) # mapril island kitchen minigame DOWN
LEFTBGR = (0,187,136,alpha) # mapril island kitchen minigame LEFT
RIGHTBGR = (170,187,51,alpha) # mapril island kitchen minigame RIGHT


class Game:
    def __init__(self, region):
        self.hwnd = gdi_capture.find_window_from_executable_name("MapleStory.exe")
        # self.hwnd = gdi_capture.find_window_from_executable_name("Honeyview.exe")
        # These values should represent pixel locations on the screen of the mini-map.
        self.top, self.left, self.bottom, self.right = region[0], region[1], region[2], region[3]
        # self.left, self.top, self.bottom, self.right = region[0], region[1], region[2], region[3]
        self.pololocations = None
        self.newest_screenshot = None
        self.height, self.width = 601, 801
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            self.height, self.width = img.shape[0], img.shape[1]
            self.newest_screenshot = img.copy()

    def get_rune_image(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            return img.copy()

    def locate(self, *color):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # cv2.imshow('img', img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # Crop the image to show only the mini-map.
                img_cropped = img[self.left:self.right, self.top:self.bottom]
                # for img in img_cropped:
                #     print(f'{img=}')
                # img_cropped = img[self.top:self.bottom, self.left:self.right]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # print(f'{img_cropped=}')
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    # print(f'{c=}')
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            return locations

    def get_player_location(self):
        location = self.locate(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def get_rune_location(self):
        location = self.locate(RUNE_BGRA)
        return location[0] if len(location) > 0 else None

    def get_other_location(self):
        location = self.locate(ENEMY_BGRA, GUILD_BGRA, BUDDY_BGRA)
        return len(location) > 0

    def get_screenshot(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            return img.copy()
    
    def get_screenshot_bytes(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            print(f'{img.size=} {img.shape}')
            return img.copy().tobytes()

    def generate_newest_screenshot(self):
        self.newest_screenshot = self.get_screenshot()        

    def get_newest_screenshot(self):
        return self.newest_screenshot

    def save_newest_screenshot(self):
        cv2.imwrite(f'history/img.png',self.newest_screenshot)
        pass

    def run_once_detect_all(self):
        img = self.newest_screenshot        
        img_cropped1 = img[300:400, 300:400] # died ok button
        img_cropped2 = img[self.left:self.right, self.top:self.bottom] # minimap
        img_cropped3 = img[375:376, 430:431] # lie detector ok button
        img_cropped4 = img[329:330, 292:293] # white dialogue of polo frito especia accidentally pressed up
        # img_cropped5 = img[329:330, 292:293] # 
        
        died_locations = self.mini_checker_function(img_cropped1,OKBGR)
        red_dot_locations = self.mini_checker_function(img_cropped2,ENEMY_BGRA)
        lie_detector_ok_locations = self.mini_checker_function(img_cropped3,LOBGR)
        white_dot_locations = self.mini_checker_function(img_cropped4,WDBGR)

        return (died_locations, red_dot_locations, lie_detector_ok_locations, white_dot_locations)

    def mini_checker_function(self,img,THEBGR):
        locations = []
        sum_x, sum_y, count = 0, 0, 0
        height, width = img.shape[0], img.shape[1]
        img_reshaped = np.reshape(img, ((width * height), 4), order="C")
        matches = np.where(np.all((img_reshaped == THEBGR), axis=1))[0]
        for idx in matches:
            sum_x += idx % width
            sum_y += idx // width
            count += 1
        if count > 0:
            x_pos = sum_x / count
            y_pos = sum_y / count
            locations.append((x_pos, y_pos))
        return locations[0] if len(locations) > 0 else None
        
        
    
    def checker(self, *color, x=0,y=0,w=800,h=600):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                # print(f'{img_cropped[60:61][60:61]}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations

    def died_checker(self):        
        location = self.checker(OKBGR, x=300,y=300,w=400,h=400)
        # location = self.checker(OKBGR, x=360,y=360,w=361,h=361)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def reddot_checker(self):
        location = self.locate(ENEMY_BGRA)
        return location[0] if len(location) > 0 else None

    def liedetector_checker(self):
        location = self.checker(LOBGR, x=430,y=375,w=431,h=376)
        return location[0] if len(location) > 0 else None

    def rune_cd_checker(self):
        # print(f'{self.height=} {self.width=}')
        location = self.checkerrune2(RUNECD2BGR, x=self.right,y=6,w=self.width,h=7) # 
        # location = self.checkerrune(RUNECDBGR, x=self.right,y=15,w=self.width,h=16) # clash with other buff
        # if len(location) < 1: # temp solution.
        #     location = self.checkerrune(RUNECDBGR, x=self.right,y=69,w=self.right+1,h=70) ## during stupid announcement.         
        return location[0] if len(location) > 0 else None

    def maple_dced_checker(self):
        location = self.checker(DCBGR, x=0,y=0,w=1,h=1) # 
        return location[0] if len(location) > 0 else None

    def polo_checker(self):
        location = self.locate(POBGR)
        # location = self.checker(PLAYER_BGRA)
        if len(location) > 0:
            self.pololocations = location[0]
            return location[0]
        else:
            return None
        # return location[0] if len(location) > 0 else None

    def get_polo_locations(self):
        return self.pololocations

    def polo2_checker(self): # Polo or Frito
        location = self.checkertest(PO2BGR,x=200,y=253,w=201,h=254)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def polo3_checker(self): # Flamewolf portal
        location = self.checkertest(PO2BGR,x=172,y=233,w=173,h=234)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def polo4_checker(self): # Especia portal
        location = self.checkertest(PO2BGR,x=199,y=244,w=200,h=245)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def especia_dot_checker(self): # Especia dot detector
        location = self.checkertest(ESBGR,x=422,y=68,w=423,h=69)
        # location = self.especiatest(ESBGR,x=400,y=60,w=450,h=110)
        # location = self.checkertest(ESBGR,x=400,y=80,w=450,h=120)
        # location = self.checkertest(ESBGR,x=422,y=98,w=423,h=99) # y=68
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def hunting_map_checker(self): # Hidden Street Bounty Hunt
        # location = self.checkertest(WDBGR,x=85,y=8,w=86,h=9) # minimap white text dot
        location = self.checkertest(WDBGR,x=330,y=100,w=331,h=101) # S of Stage 1
        # location = self.checkertest(WDBGR,x=85,y=9,w=86,h=10)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def hunting_map2_checker(self): # Hidden Street Guarding The Castle Wall
        # location = self.checkertest(WDBGR,x=87,y=8,w=88,h=9) # this 1 is the minimap text white dot, if announcement cant be detected
        # location = self.checkertest2(WDBGR,x=328,y=131,w=329,h=132) # this 1 is the W of the center word Wave 1
        location = self.checkertest2(WDBGR,x=328,y=101,w=329,h=102) # this 1 is the W of the center word Wave 1
        # location = self.checkertest(WDBGR,x=87,y=9,w=88,h=10)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def hunting_map3_checker(self): # Hidden Street Golden Bird (Stormwing Habitat)
        location = self.checkertest(SWBGR,x=397,y=44,w=398,h=45)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def hunting_map_timer_checker(self): # clock
        location = self.checkertest(TIBGR,x=304,y=48,w=305,h=49)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def white_dot_checker(self):
        location = self.checkertest(WDBGR,x=292,y=329,w=293,h=330)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def dark_checker(self):
        location = self.checkertest(DABGR,x=292,y=329,w=293,h=330)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def rock_checker(self):
        location = self.checkertest3(ROBGR,x=430,y=292,w=460,h=293)
        return location
    
    def rock_checker2(self):
        location = self.checkertest3(ROBGR,x=460,y=292,w=490,h=293)
        return location

    def rock_checker3(self):
        location = self.checkertest3(ROBGR,x=500,y=292,w=530,h=293)
        return location
        
    def vdance_checker(self):
        location = self.checkertest4(DABGR,x=435,y=691,w=1034,h=693)
        # location = self.checkertest4(DABGR,x=159,y=523,w=660,h=525)
        # return location[0] if len(location) > 0 else None
        return location # count actually

    def vdance_checker2(self):
        location = self.checkertest5(DABGR,x=435,y=719,w=1034,h=720) # 1366x768 # use this for 49 combo perfect score! best of the best!
        # location = self.checkertest5(DABGR,x=392,y=671,w=991,h=672) # 1280x720 # not as good because the pink gap is narrower unfortunately
        # location = self.checkertest5(DABGR,x=264,y=719,w=863,h=720) # 1024x768 # even worse, very narrow and the V speed is too fast. 
        return location

    def kitchen_checker(self):
        location = self.checkertest7(KITCHENBGR,x=435,y=719,w=1034,h=720)
        return location

    def sequence_checker(self):
        location = self.checkertest8(KITCHENBGR,x=435,y=719,w=1034,h=720)
        return location

    def sequence_checker_extreme(self):
        location = self.checkertest9(KITCHENBGR,x=435,y=719,w=1034,h=720)
        return location

    def ardentdetector(self):
        location = self.checkertest(ARDENTBGR,x=14,y=36,w=15,h=37) # 
        return location[0] if len(location) > 0 else None

    def ardentmaploading(self):
        location = self.checkertest(DABGR,x=14,y=36,w=15,h=37)
        return location[0] if len(location) > 0 else None


    def pure_test(self): 
        location = self.checkertest(PLAYER_BGRA,x=self.top,y=self.left,w=self.bottom,h=self.right)
        return location

    def gma_detector(self):
        location = self.gma_detector_checker(GMBGR,x=0,y=300,w=400,h=550)
        # location = self.gma_detector_checker((119,170,179,255),x=0,y=250,w=15,h=265)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None




    def gma_detector_checker(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
                # print("Honeyview.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # print(f'{img_reshaped=}')
                # print(f'{img_reshaped[:,0]=}')
                # cv2.imshow('img_reshaped', img_reshaped)
                cv2.imshow('img', img)
                # cv2.imshow('img_cropped', img_cropped)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                # print(f'{color=}')
                for c in color:
                    # print(f'{c=}')
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # print(f'{np.where(np.all((img_reshaped == c), axis=1))=}')
                    # print(f'{np.where(np.all((img_reshaped == c), axis=1))[0]=}')
                    # matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 201) & (img_reshaped[:,0] <= 225) &
                        (img_reshaped[:,1] >= 201) & (img_reshaped[:,1] <= 225) &
                        (img_reshaped[:,2] >= 201) & (img_reshaped[:,2] <= 225) 
                        )[0]
                    # matches = np.where(
                    #     (img_reshaped[:,0] >= 201) & (img_reshaped[:,0] <= 225) &
                    #     (img_reshaped[:,1] >= 201) & (img_reshaped[:,1] <= 225) &
                    #     (img_reshaped[:,2] >= 201) & (img_reshaped[:,2] <= 225) 
                    #     )
                    print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {img_reshaped[idx]} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations


        
    def especiatest(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                cv2.imshow('img_cropped', img_cropped)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations

    # def init_maple_windows(self):
    #     windows=[]
    #     winlist=[]
    #     winlist = pygetwindow.getWindowsWithTitle('MapleStory')
    #     for w in winlist:
    #         windows.append(w._hWnd)
    #     for windowhwnd in windows:
    #         position = win32gui.GetWindowRect(windowhwnd)
    #         x, y, w, h = position
    #         if w-x == 410:
    #             self.chathwnd=windowhwnd
    #         else:
    #             self.maplehwnd=windowhwnd
    #     self.position = win32gui.GetWindowRect(self.maplehwnd)
                
    def checkertest(self, *color, x,y,w,h):
        # now=perf_counter()
        # screenshot = ImageGrab.grab(self.position)
        # screenshot = np.array(screenshot)
        # img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        # now1=perf_counter()-now
        # print(f'{now1=}')
        # now2=perf_counter()
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            # now3=perf_counter()-now2
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img=} {img.ndim=}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # now2=perf_counter()-now
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # now3=perf_counter()-now
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # print(f'{img_cropped=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # now4=perf_counter()
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # now5=perf_counter()-now4
                    # print(f'n3={now3:.10f}')
                    # print(f'n1={now1:.10f} n3={now3:.10f} n5={now5:.10f}')
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:                        
                        # print(f'{img_cropped=}')
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations
            
    def checkertest2(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            return locations

            
    def checkertest3(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x-15:w-15]
                img_cropped2 = img[y+50:h+50,x:w]
                # print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    count2=0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        # sum_x += idx % width
                        # sum_y += idx // width
                        count += 1
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        # x_pos = sum_x / count
                        # y_pos = sum_y / count
                        # locations.append((x_pos, y_pos))
                        return (True,False)
                    matches2 = np.where(np.all((img_reshaped2 == c), axis=1))[0]
                    for idx in matches2:
                        count2 += 1
                    if count2 > 0:
                        return (False,True)
            # return locations
            return None



    def checkertest4(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                # print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 227) & (img_reshaped[:,0] <= 239) &
                        (img_reshaped[:,1] >= 166) & (img_reshaped[:,1] <= 180) &
                        (img_reshaped[:,2] >= 247) & (img_reshaped[:,2] <= 248) 
                        )[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
            # return locations
            return count
            
    def checkertest5(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                img_cropped2 = img[y-2:h-2, x:w]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # matches = np.where(
                    #     (img_reshaped[:,0] >= 237) & (img_reshaped[:,0] <= 239) &
                    #     (img_reshaped[:,1] >= 135) & (img_reshaped[:,1] <= 137) &
                    #     (img_reshaped[:,2] >= 253) & (img_reshaped[:,2] <= 255) 
                    #     )[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 180) & (img_reshaped[:,0] <= 239) &
                        (img_reshaped[:,1] >= 135) & (img_reshaped[:,1] <= 195) &
                        (img_reshaped[:,2] >= 253) & (img_reshaped[:,2] <= 255) 
                        )[0]
                    # print(f'{matches=}')
                    # for idx in matches:
                    #     pass
                    for idx in matches:
                        # print(f'{img_reshaped2[idx]=}')
                        #
                        # if img_reshaped2[idx,0]+66 < 255:
                        #     return idx                        
                        # if img_reshaped2[idx,1]+66 < 255:
                        #     return idx
                        # if img_reshaped2[idx,2]+66 < 255:
                        #     # print(f'press npc key now. {img_reshaped2[idx]}')
                        #     return idx
                        #
                        if img_reshaped2[idx,0]+66 < 255:
                            if img_reshaped2[idx,1]+66 < 255:
                                if img_reshaped2[idx,2]+66 < 255:
                                    # print(f'press npc key now. {img_reshaped2[idx]}')
                                    return idx
                        #
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # sum_x += idx % width
                        # sum_y += idx // width
                        count += 1
                    # print(f'{sum_x=} {sum_y=} {count=}')
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    # print(f'{locations=}')
            return 0

    def checkertest6(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[100:101, 489:490]
                img_cropped2 = img[444:445, 679:680]
                # img_cropped3 = img[444:445, 679:680] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # print(f'{img_reshaped=} {img_reshaped2=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    matches = np.where(np.all((img_reshaped == KITCHENBGR), axis=1))[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    if img_reshaped2[:,0] == 0:
                        if img_reshaped2[:,1] == 136:
                            return (count, 1) # UP
                        elif img_reshaped2[:,1] == 187:
                            return (count, 3) # LEFT
                    elif img_reshaped2[:,0] == 119:
                        return (count,2) # DOWN
                    elif img_reshaped2[:,0] == 170:
                        return (count,4) # RIGHT
                # UPBGR = (0,136,187,alpha) # mapril island kitchen minigame UP 
                # DOWNBGR = (119,51,187,alpha) # mapril island kitchen minigame DOWN
                # LEFTBGR = (0,187,136,alpha) # mapril island kitchen minigame LEFT
                # RIGHTBGR = (170,187,51,alpha) # mapril island kitchen minigame RIGHT
            return (0,0)

    def checkertest7(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[100:101, 489:490]
                # img_cropped2 = img[444:445, 679:680]
                # img_cropped3 = img[444:445, 679:680] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # print(f'{img_reshaped=} {img_reshaped2=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    matches = np.where(np.all((img_reshaped == KITCHENBGR), axis=1))[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    # if img_reshaped2[:,0] == 0:
                    #     if img_reshaped2[:,1] == 136:
                    #         return (count, 1) # UP
                    #     elif img_reshaped2[:,1] == 187:
                    #         return (count, 3) # LEFT
                    # elif img_reshaped2[:,0] == 119:
                    #     return (count,2) # DOWN
                    # elif img_reshaped2[:,0] == 170:
                    #     return (count,4) # RIGHT
                # UPBGR = (0,136,187,alpha) # mapril island kitchen minigame UP 
                # DOWNBGR = (119,51,187,alpha) # mapril island kitchen minigame DOWN
                # LEFTBGR = (0,187,136,alpha) # mapril island kitchen minigame LEFT
                # RIGHTBGR = (170,187,51,alpha) # mapril island kitchen minigame RIGHT
            return count
            
    # def read_score(self):        
    #     img_cropped = self.get_screenshot()
    #     img_cropped = img_cropped[139:151, 1309:1338]
    #     # img_cropped = self.newest_screenshot[139:151, 1309:1338]
    #     # img_cropped = self.newest_screenshot
    #     img_cropped = cv2.resize(img_cropped, (290,120), interpolation=cv2.INTER_LINEAR)
    #     img_cropped = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    #     _, img_cropped = cv2.threshold(img_cropped, 128, 255, cv2.THRESH_BINARY)
    #     try:
    #         # imgstring = pytesseract.image_to_string(img_cropped, config='digits')
    #         # imgstring = pytesseract.image_to_string(img_cropped, config='--psm 10 --oem 3 digits')
    #         imgstring = pytesseract.image_to_string(img_cropped, config='--psm 6 --oem 3 digits')
    #         # imgstring = pytesseract.image_to_string(img_cropped, config='--psm 10 --oem 3')
    #         # imgstring = pytesseract.image_to_string(img_cropped, lang='eng', boxes=False, config='--psm 10 --oem 3')
    #         # imgstring = pytesseract.image_to_string(img_cropped, config='--psm 6')
    #         # imgstring = pytesseract.image_to_string(img_cropped)
    #         imgstring = imgstring.replace('\n', '')
    #         filename = imgstring+''
    #         print(f"PYTESSERACT!!!!!!!!! = {imgstring=} {type(imgstring)=} {type('string')=} {filename=}")
    #         # print(f"PYTESSERACT!!!!!!!!! = ")
    #         cv2.imwrite(f'../image/{filename}.png', img_cropped)
    #         # cv2.imwrite(f'../image/{imgstring}_.png', img_cropped)
    #     except Exception as e:
    #         print(f'pytesseract e: {e=}')
    #     # finally:
    #         # print(f'finally')

    ## UPBGR = (0,118,205,alpha) # mapril island kitchen minigame UP (0,122,205) (0,125,210) (0,119,210)
    ## DOWNBGR = (17,92,214,alpha) # mapril island kitchen minigame DOWN (87,74,205) (17,85,214)
    ## LEFTBGR = (0,155,168,alpha) # mapril island kitchen minigame LEFT (0,163,160,alpha)
    ## RIGHTBGR = (136,156,92,alpha) # mapril island kitchen minigame RIGHT
    def check_arrows_extreme8(self, img):
        matches = np.where((img[:,0] == 0))[0]
        for idx in matches:
            matches1 = np.where((img[:,1] == 118) or (img[:,1] == 119) or (img[:,1] == 122) or (img[:,1] == 125))[0]
            for idx1 in matches1:
                return 1
            matches2 = np.where((img[:,1] == 155) or (img[:,1] == 163))[0]
            for idx2 in matches2:
                return 3
        matches3 = np.where((img[:,0] == 17))[0]
        for idx3 in matches3:
            return 2
        matches4 = np.where((img[:,0] == 136))[0]
        for idx4 in matches4:
            return 4
        return 0

    ## UPBGR = (0,125,196,alpha) # mapril island kitchen minigame UP 
    ## DOWNBGR = (111,51,192,alpha) # mapril island kitchen minigame DOWN (103,53,196)
    ## LEFTBGR = (0,169,152,alpha) # mapril island kitchen minigame LEFT (0,178,144）
    ## RIGHTBGR = (159,178,65,alpha) # mapril island kitchen minigame RIGHT (159,1799,65)
    def check_arrows_extreme7(self, img):
        matches = np.where((img[:,0] == 0))[0]
        for idx in matches:
            matches1 = np.where((img[:,1] == 125))[0]
            for idx1 in matches1:
                return 1
            matches2 = np.where((img[:,1] == 169) or (img[:,1] == 178))[0]
            for idx2 in matches2:
                return 3
        matches3 = np.where((img[:,0] == 111) or (img[:,0] == 103))[0]
        for idx3 in matches3:
            return 2
        matches4 = np.where((img[:,0] == 159))[0]
        for idx4 in matches4:
            return 4
        return 0

    # UPBGR = (0,136,187,alpha) # mapril island kitchen minigame UP 
    # DOWNBGR = (119,51,187,alpha) # mapril island kitchen minigame DOWN
    # LEFTBGR = (0,187,136,alpha) # mapril island kitchen minigame LEFT
    # RIGHTBGR = (170,187,51,alpha) # mapril island kitchen minigame RIGHT
    def check_arrows_extreme6(self, img):
        matches = np.where((img[:,0] == 0))[0]
        for idx in matches:
            matches1 = np.where((img[:,1] == 136))[0]
            for idx1 in matches1:
                return 1
            matches2 = np.where((img[:,1] == 187))[0]
            for idx2 in matches2:
                return 3
        matches3 = np.where((img[:,0] == 119))[0]
        for idx3 in matches3:
            return 2
        matches4 = np.where((img[:,0] == 170))[0]
        for idx4 in matches4:
            return 4
        return 0

    def check_arrows(self, img):        
        if img[:,0] == 0:
            if img[:,1] == 136:
                return 1 # UP
            elif img[:,1] == 187:
                return 3 # LEFT
        elif img[:,0] == 119:
            return 2 # DOWN
        elif img[:,0] == 170:
            return 4 # RIGHT
        return 0

    def checkertest8(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                self.newest_screenshot=img
                # img_cropped = img[100:101, 489:490]
                img_cropped = img[444:445, 679:680]
                img_cropped1 = img[446:447, 793:794] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped2 = img[446:447, 873:874] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped3 = img[446:447, 953:954] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped4 = img[446:447, 1033:1034] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped5 = img[446:447, 1113:1114] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped6 = img[446:447, 1193:1194] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped7 = img[446:447, 1273:1274] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped8 = img[446:447, 1353:1354] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped1 = np.reshape(img_cropped1, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                img_reshaped3 = np.reshape(img_cropped3, ((width * height), 4), order="C")
                img_reshaped4 = np.reshape(img_cropped4, ((width * height), 4), order="C")
                img_reshaped5 = np.reshape(img_cropped5, ((width * height), 4), order="C")
                img_reshaped6 = np.reshape(img_cropped6, ((width * height), 4), order="C")
                img_reshaped7 = np.reshape(img_cropped7, ((width * height), 4), order="C")
                img_reshaped8 = np.reshape(img_cropped8, ((width * height), 4), order="C")
                # img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # print(f'{img_reshaped=} {img_reshaped2=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # matches = np.where(np.all((img_reshaped == KITCHENBGR), axis=1))[0]
                    # for idx in matches:
                    #     sum_x += idx % width
                    #     sum_y += idx // width
                    #     count += 1
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    current_arrow = self.check_arrows(img_reshaped)
                    next_arrow1 = self.check_arrows(img_reshaped1)
                    next_arrow2 = self.check_arrows(img_reshaped2)
                    next_arrow3 = self.check_arrows(img_reshaped3)
                    next_arrow4 = self.check_arrows(img_reshaped4)
                    next_arrow5 = self.check_arrows(img_reshaped5)
                    next_arrow6 = self.check_arrows(img_reshaped6)
                    next_arrow7 = self.check_arrows(img_reshaped7)
                    next_arrow8 = self.check_arrows(img_reshaped8)
                    # if img_reshaped2[:,0] == 0:
                    #     if img_reshaped2[:,1] == 136:
                    #         return (count, 1) # UP
                    #     elif img_reshaped2[:,1] == 187:
                    #         return (count, 3) # LEFT
                    # elif img_reshaped2[:,0] == 119:
                    #     return (count,2) # DOWN
                    # elif img_reshaped2[:,0] == 170:
                    #     return (count,4) # RIGHT
            return (current_arrow, next_arrow1, next_arrow2, next_arrow3, next_arrow4, next_arrow5, next_arrow6, next_arrow7, next_arrow8)

    #### EXTREME VERSION #####
    def checkertest9(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # img_cropped = img[100:101, 489:490]
                img_cropped = img[444:445, 679:680]
                img_cropped1 = img[446:447, 793:794] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped2 = img[446:447, 873:874] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped3 = img[446:447, 953:954] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped4 = img[446:447, 1033:1034] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped5 = img[446:447, 1113:1114] # 793, 873, 953, 1033, 1113, 1193, 1273, 1353 / 446
                img_cropped6 = img[445:448, 1184:1202] # 1184~1202 3 pixels height
                img_cropped7 = img[445:448, 1264:1282] # 1264~1282
                # img_cropped7 = img[446:447, 1264:1282] # 1264~1282
                img_cropped8 = img[445:448, 1344:1362] # 1344~1362 # 491 514 
                # img_cropped8 = img[446:447, 1344:1362] # 1344~1362 # 491 514 
                img_cropped77 = img[460:483, 1247:1251] # 1264~1282 # 491 514 1248 1252
                img_cropped88 = img[460:483, 1327:1331] # 1344~1362 # 491 514 #1328 1332
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                height6, width6 = img_cropped6.shape[0], img_cropped6.shape[1]
                height77, width77 = img_cropped77.shape[0], img_cropped77.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped1 = np.reshape(img_cropped1, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                img_reshaped3 = np.reshape(img_cropped3, ((width * height), 4), order="C")
                img_reshaped4 = np.reshape(img_cropped4, ((width * height), 4), order="C")
                img_reshaped5 = np.reshape(img_cropped5, ((width * height), 4), order="C")
                img_reshaped6 = np.reshape(img_cropped6, ((width6 * height6), 4), order="C")
                img_reshaped7 = np.reshape(img_cropped7, ((width6 * height6), 4), order="C")
                img_reshaped8 = np.reshape(img_cropped8, ((width6 * height6), 4), order="C")
                img_reshaped77 = np.reshape(img_cropped77, ((width77 * height77), 4), order="C")
                img_reshaped88 = np.reshape(img_cropped88, ((width77 * height77), 4), order="C")
                # img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # print(f'{img_reshaped=} {img_reshaped2=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # matches = np.where(np.all((img_reshaped == KITCHENBGR), axis=1))[0]
                    # for idx in matches:
                    #     sum_x += idx % width
                    #     sum_y += idx // width
                    #     count += 1
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    current_arrow = self.check_arrows(img_reshaped)
                    next_arrow1 = self.check_arrows(img_reshaped1)
                    next_arrow2 = self.check_arrows(img_reshaped2)
                    next_arrow3 = self.check_arrows(img_reshaped3)
                    next_arrow4 = self.check_arrows(img_reshaped4)
                    next_arrow5 = self.check_arrows(img_reshaped5)
                    next_arrow6 = self.check_arrows_extreme6(img_reshaped6)
                    next_arrow7 = self.check_arrows_extreme7(img_reshaped7)
                    next_arrow8 = self.check_arrows_extreme8(img_reshaped8)
                    if next_arrow7 == 0:
                        next_arrow7 = self.check_arrows_extreme7(img_reshaped77)
                        print(f'color not found, searching vertical pixels. {next_arrow7=}')
                    else:
                        print(f'arrow_7th = {next_arrow7} and {self.check_arrows_extreme7(img_reshaped77)}, same?? diff??')
                    if next_arrow8 == 0:
                        next_arrow8 = self.check_arrows_extreme8(img_reshaped88)
                        print(f'color not found, searching vertical pixels. {next_arrow8=}')
                    else:
                        print(f'arrow_8th = {next_arrow8} and {self.check_arrows_extreme8(img_reshaped88)}, same?? diff??')
                    # if img_reshaped2[:,0] == 0:
                    #     if img_reshaped2[:,1] == 136:
                    #         return (count, 1) # UP
                    #     elif img_reshaped2[:,1] == 187:
                    #         return (count, 3) # LEFT
                    # elif img_reshaped2[:,0] == 119:
                    #     return (count,2) # DOWN
                    # elif img_reshaped2[:,0] == 170:
                    #     return (count,4) # RIGHT
                # UPBGR = (0,136,187,alpha) # mapril island kitchen minigame UP 
                # DOWNBGR = (119,51,187,alpha) # mapril island kitchen minigame DOWN
                # LEFTBGR = (0,187,136,alpha) # mapril island kitchen minigame LEFT
                # RIGHTBGR = (170,187,51,alpha) # mapril island kitchen minigame RIGHT
            return (current_arrow, next_arrow1, next_arrow2, next_arrow3, next_arrow4, next_arrow5, next_arrow6, next_arrow7, next_arrow8)

    def checkerrune(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                img_cropped2 = img[y+54:h+54, x:w]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    matches = np.where(
                        (img_reshaped[:,0] >= 149) & (img_reshaped[:,0] <= 161) &
                        (img_reshaped[:,1] >= 149) & (img_reshaped[:,1] <= 161) &
                        (img_reshaped[:,2] >= 149) & (img_reshaped[:,2] <= 161) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # tmp = idx % width
                        # img = img_cropped[:,tmp-50:tmp+50]
                        # cv2.imshow('img',img)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 1. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped[:,0] >= 134) & (img_reshaped[:,0] <= 144) &
                        (img_reshaped[:,1] >= 112) & (img_reshaped[:,1] <= 122) &
                        (img_reshaped[:,2] >= 93) & (img_reshaped[:,2] <= 113) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 2. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped2[:,0] >= 149) & (img_reshaped2[:,0] <= 161) &
                        (img_reshaped2[:,1] >= 149) & (img_reshaped2[:,1] <= 161) &
                        (img_reshaped2[:,2] >= 149) & (img_reshaped2[:,2] <= 161) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 3. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped2[:,0] >= 134) & (img_reshaped2[:,0] <= 144) &
                        (img_reshaped2[:,1] >= 112) & (img_reshaped2[:,1] <= 122) &
                        (img_reshaped2[:,2] >= 93) & (img_reshaped2[:,2] <= 113) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 4. {locations=}')
                        return locations
            print(f'rune cd icon not found anywhere. (means rune cd finished. )  {locations=}')
            return locations

            
    def checkerrune2(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                img_cropped2 = img[y+54:h+54, x:w]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    matches = np.where(
                        (img_reshaped[:,0] >= 74) & (img_reshaped[:,0] <= 83) &
                        (img_reshaped[:,1] >= 74) & (img_reshaped[:,1] <= 82) &
                        (img_reshaped[:,2] >= 71) & (img_reshaped[:,2] <= 77) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # tmp = idx % width
                        # img = img_cropped[:,tmp-50:tmp+50]
                        # cv2.imshow('img',img)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 1. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped[:,0] >= 134) & (img_reshaped[:,0] <= 144) &
                        (img_reshaped[:,1] >= 112) & (img_reshaped[:,1] <= 122) &
                        (img_reshaped[:,2] >= 93) & (img_reshaped[:,2] <= 113) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 2. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped2[:,0] >= 149) & (img_reshaped2[:,0] <= 161) &
                        (img_reshaped2[:,1] >= 149) & (img_reshaped2[:,1] <= 161) &
                        (img_reshaped2[:,2] >= 149) & (img_reshaped2[:,2] <= 161) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 3. {locations=}')
                        return locations
                    matches = np.where(
                        (img_reshaped2[:,0] >= 134) & (img_reshaped2[:,0] <= 144) &
                        (img_reshaped2[:,1] >= 112) & (img_reshaped2[:,1] <= 122) &
                        (img_reshaped2[:,2] >= 93) & (img_reshaped2[:,2] <= 113) 
                        )[0]
                    for idx in matches:
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
                        print(f'rune cd icon found at 4. {locations=}')
                        return locations
            print(f'rune cd icon not found anywhere. (means rune cd finished. )  {locations=}')
            return locations
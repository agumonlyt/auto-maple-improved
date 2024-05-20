import random
import time
from time import perf_counter
from configparser import ConfigParser
# from initinterception import interception, move_to, move_relative, left_click, keydown, keyup, sleep
from src.bumblebee.initinterception import keydown, keyup, keyupall, keydown_arrow, keyup_arrow, keyupall_arrow, sleep, sleeplol
import win32gui
from PIL import ImageGrab
import json
import numpy as np
import requests














class Action:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read('src\\bumblebee\\settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')
        self.fountainkey = self.config.get('keybind', 'fountainkey')
        self.ccbutton = self.config.get('keybind', 'ccbutton')
        self.bossui = self.config.get('keybind', 'bossui')
        self.ardent = self.config.get('keybind', 'ardent')
        self.ipaddress = self.config.get('main', 'ipaddress')
        self.offsety=10
        self.offsetx=10
        ## for main rotation
        self.top=10.0
        self.left=10.0
        self.right=10.0
        self.btm=10.0 
        ## for stormwing map
        self.stop=29.0
        self.sleft=35.0 # 18.0 # 27.0
        self.sright=130 # 125.0 # 135.0 140.0 132.5
        self.sbtm=58.0 # 54.5
        self.runesolver=None
        self.g=None
        ## timer variables goes here        
        self.randomlist = ['z', 'x', 'c', 'space', '2', '3', '0', 'f9', 'w', 'e', 'r', 't', 's', 'd', 'f', 'v']
        # self.randomlist = []
        self.cosmicshowerplanttimer0=0
        self.cosmicshowerplanttimer=0
        self.cosmicshowerplant=True
        self.fountaintimer0=0
        self.fountaintimer=0
        self.fountain=True
        self.randommtimer0=0
        self.randommtimer=0
        self.runetimer0=0
        self.runetimer=0
        self.checkrune=True
        self.solverune=True
        self.now=0
        ## misc. others. 
        self.replaceropeconnect=False
        self.stoprune=False
        self.maplehwnd=None # somehow only using in runesolver3()
        ## enter portal algorithm variable goes here
        self.goingtoportal=False
        self.gotoportal1=False
        self.gotoportal2=False
        self.gotoportal3=False
        self.gotoportal4=False
        self.tries=0
        self.plb=73.5 # portal left boundary
        self.prb=74.5 # portal right boundary
        self.plbm2=self.plb-2 # portal left boundary minus two, 71.5
        self.prbp2=self.prb+2 # portal right boundary plus two, 76.5
        self.successthreshold=180.5 # what will be the coordinate of your character if successfully entered portal. 
        self.preventgotonextmap=56.5 # if there is a goto next map portal, put here
        self.firstx = 0 # use to compare pass portal
        ## all the entry goes here
        self.rotation_list = ['default']
        self.rotation='default'
        self.rotation_mapping = {
            'default': self.default,
        }  
        self.rotation='default'

    def setup(self,g,maplehwnd):
        if g is not None:
            self.g=g
        if maplehwnd is not None:
            self.maplehwnd=maplehwnd
        
    def perform_next_attack(self, x, y):
        self.rotation_mapping[self.rotation](x,y)
        
    def get_rotation_list(self):
        return self.rotation_list
        
    def set_rotation(self, rotation):
        self.rotation = rotation
        print(f'{self.rotation=}')
    
    def refreshkeybind(self):
        self.config.read('settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')
        
    def disablerune(self):
        self.stoprune=True

    def enablerune(self):
        self.stoprune=False

    def sleeprandom(self,x=31,y=101):
        r = random.randint(x, y)
        r /= 1000
        sleep()

    #################### BASIC PREDEFINED KEYPRESSES WITH SLEEP #########################3#

    def escp(self,x=31,y=101):
        keydown('esc')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def escr(self,x=31,y=101):
        keyup('esc')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def escpr(self,x=31,y=101):
        self.escp()
        self.escr()

    def enterp(self,x=31,y=101):
        keydown('enter')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def enterr(self,x=31,y=101):
        keyup('enter')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def enterpr(self,x=31,y=101):
        self.enterp()
        self.enterr()

    def enterp_special(self,x=31,y=101):
        keydown('enter')
        r = random.randint(x, y)
        r /= 1000
        time.sleep(r)

    def enterr_special(self,x=31,y=101):
        keyup('enter')
        r = random.randint(x, y)
        r /= 1000
        time.sleep(r)

    def enterpr_special(self,x=31,y=101):
        self.enterp_special(x,y)
        self.enterr_special(x,y)

    def ccbuttonp(self,x=31,y=101):
        keydown(self.ccbutton)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ccbuttonr(self,x=31,y=101):
        keyup(self.ccbutton)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def ccbuttonpr(self,x=31,y=101):
        self.ccbuttonp()
        self.ccbuttonr()

    def bossuip(self,x=31,y=101):
        keydown(self.bossui)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def bossuir(self,x=31,y=101):
        keyup(self.bossui)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def bossuipr(self,x=31,y=101):
        self.bossuip()
        self.bossuir()

    def ardentp(self,x=31,y=101):
        keydown(self.ardent)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ardentr(self,x=31,y=101):
        keyup(self.ardent)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def ardentpr(self,x=31,y=101):
        self.ardentp()
        self.ardentr()

    def leftp(self,x=31,y=101):
        keydown_arrow('left')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def leftr(self,x=31,y=101):
        keyup_arrow('left')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def leftpr(self,x=31,y=101):
        self.leftp()
        self.leftr()

    def rightp(self,x=31,y=101):
        keydown_arrow('right')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def rightr(self,x=31,y=101):
        keyup_arrow('right')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    def rightpr(self,x=31,y=101):
        self.rightp()
        self.rightr()

    def upp(self,x=31,y=101):
        # print(f'up press ..')
        keydown_arrow('up')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        # print(f'up press done ..')

    def upr(self,x=31,y=101):
        # print(f'up release ..')
        keyup_arrow('up')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        # print(f'up done ..')
    
    def uppr(self,x=31,y=101):
        self.upp()
        self.upr()

    def downp(self,x=31,y=101):
        keydown_arrow('down')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def downr(self,x=31,y=101):
        keyup_arrow('down')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def downpr(self,x=31,y=101):
        self.downp()
        self.downr()

    def jumpp(self,x=31,y=101):
        # print(f'jumpp')
        keydown(self.jump)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def jumpr(self,x=31,y=101):
        keyup(self.jump)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def jumppr(self,x=31,y=101):
        self.jumpp()
        self.jumpr()

    ## additional patch for extra key buttons. 

    def ctrlp(self,x=31,y=101):
        keydown('ctrl')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ctrlr(self,x=31,y=101):
        keyup('ctrl')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ctrlpr(self,x=31,y=101):
        self.ctrlp()
        self.ctrlr()

    def bp(self,x=31,y=101):
        keydown('b')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def br(self,x=31,y=101):
        keyup('b')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def zp(self,x=31,y=101):
        keydown('z')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def zr(self,x=31,y=101):
        keyup('z')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def xp(self,x=31,y=101):
        keydown('x')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def xr(self,x=31,y=101):
        keyup('x')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def cp(self,x=31,y=101):
        keydown('c')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def cr(self,x=31,y=101):
        keyup('c')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def vp(self,x=31,y=101):
        keydown('v')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def vr(self,x=31,y=101):
        keyup('v')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def ap(self,x=31,y=101):
        keydown('a')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ar(self,x=31,y=101):
        keyup('a')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def sp(self,x=31,y=101):
        keydown('s')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def sr(self,x=31,y=101):
        keyup('s')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def dp(self,x=31,y=101):
        keydown('d')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def dr(self,x=31,y=101):
        keyup('d')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
        
    def fp(self,x=31,y=101):
        keydown('f')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def fr(self,x=31,y=101):
        keyup('f')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def gp(self,x=31,y=101):
        keydown('g')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def gr(self,x=31,y=101):
        keyup('g')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def gpr(self,x=31,y=101):
        self.gp()
        self.gr()

    def hp(self,x=31,y=101):
        keydown('h')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def hr(self,x=31,y=101):
        keyup('h')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def hpr(self,x=31,y=101):
        self.hp()
        self.hr()

    def sp(self,x=31,y=101):
        keydown('s')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def sr(self,x=31,y=101):
        keyup('s')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def spr(self,x=31,y=101):
        self.sp()
        self.sr()

    def yp(self,x=31,y=101):
        keydown('y')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def yr(self,x=31,y=101):
        keyup('y')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ypr(self,x=31,y=101):
        self.yp()
        self.yr()

    def jp(self,x=31,y=101):
        keydown('j')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def jr(self,x=31,y=101):
        keyup('j')
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def jpr(self,x=31,y=101):
        self.jp()
        self.jr()

    def teleportp(self,x=31,y=101):
        keydown(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def teleportr(self,x=31,y=101):
        keyup(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def teleportpr(self,x=31,y=101):
        self.teleportp()
        self.teleportr()

    def attackp(self,x=31,y=101):
        keydown(self.atk)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def attackr(self,x=31,y=101):
        keyup(self.atk)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ropeconnectp(self,x=31,y=101):
        keydown(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ropeconnectr(self,x=31,y=101):
        keyup(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def ropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        self.ropeconnectp()
        self.ropeconnectr()

    def npcp(self,x=31,y=101):
        keydown(self.npc)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def npcr(self,x=31,y=101):
        keyup(self.npc)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def fountainp(self,x=31,y=101):
        # print(f'{self.fountainkey=}')
        keydown(self.fountainkey)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)

    def fountainr(self,x=31,y=101):
        keyup(self.fountainkey)
        r = random.randint(x, y)
        r /= 1000
        sleep(r)
    
    ##################### CUSTOM ATTACK SEQUENCE ##############################

    def leftattack(self):
        print(f'leftattack')
        self.leftp()
        self.attackp()
        self.attackr()
        self.leftr()

    def rightattack(self):
        print(f'rightattack')
        self.rightp()
        self.attackp()
        self.attackr()
        self.rightr()

    def leftattackk(self):
        print(f'leftattackk')
        self.leftp()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.leftr()

    def rightattackk(self):
        print(f'rightattackk')
        self.rightp()
        self.attackp()
        self.attackr()
        self.rightr()

    def goleftattack(self):
        print(f'self.goleftattack')
        self.leftp()
        self.teleportp()
        self.teleportr()
        self.attackp()
        self.attackr()
        self.leftr()

    def goleftattackk(self):
        print(f'self.goleftattackk')
        self.leftp()
        self.teleportp()
        self.teleportr()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.leftr()

    def goattackleft(self):
        print(f'self.goattackleft')
        self.leftp()
        self.attackp()
        self.attackr()
        self.teleportp()
        self.teleportr()
        self.leftr()

    def goattackkleft(self):
        print(f'self.goattackkleft')
        self.leftp()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.teleportp()
        self.teleportr()
        self.leftr()

    def gorightattack(self):
        print(f'self.gorightattack')
        self.rightp()
        self.teleportp()
        self.teleportr()
        self.attackp()
        self.attackr()
        self.rightr()

    def gorightattackk(self):
        print(f'self.gorightattackk')
        self.rightp()
        self.teleportp()
        self.teleportr()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.rightr()

    def goattackright(self):
        print(f'self.goattackright')
        self.rightp()
        self.attackp()
        self.attackr()
        self.teleportp()
        self.teleportr()
        self.rightr()

    def goattackkright(self):
        print(f'self.goattackkright')
        self.rightp()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.teleportp()
        self.teleportr()
        self.rightr()

    def goupattack(self):
        print(f'goupattack')
        sleep(.1)
        self.upp()
        self.teleportp()
        self.teleportr()
        self.upr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def goupattack_v2(self):
        print(f'goupattack_v2')
        self.rightp()
        self.ropeconnectp()
        self.ropeconnectr()
        self.attackp()
        self.attackr()
        self.rightr()

    def goupattack_v3(self):
        print(f'goupattack_v3')
        sleep(.1)
        self.jumpp()
        self.jumpr()
        self.ropeconnectp(31,101)
        self.ropeconnectr(31,101)
        sleep(.333)
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def upjumpattack(self):
        print(f'upjumpattack')
        sleep(.1)
        self.upp()
        self.teleportp()
        self.teleportr()
        self.upr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def godownattack(self):
        print(f'godownattack')
        self.downp()
        self.teleportp()
        self.teleportr()
        self.downr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def goleftattack_fjump(self):
        print(f'self.goleftattack_fjump')
        self.leftp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.leftr()

    def gorightattack_fjump(self):
        print(f'self.gorightattack_fjump')
        self.rightp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.rightr()

    def goupattack_fjump(self): # adele upjump
        print(f'goupattack_fjump')
        sleep(.1)
        self.jumpp()
        self.jumpr()
        self.upp()
        self.jumpp()
        self.jumpr()
        self.upr()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def godownattack_fjump(self):
        print(f'godownattack_fjump')
        self.downp()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.downr()
        
    def leftwalk(self,x=222,y=333):
        print(f'leftwalk')
        self.leftp(x,y)
        self.leftr()

    def rightwalk(self,x=222,y=333):
        print(f'rightwalk')
        self.rightp(x,y)
        self.rightr()
        
    def downjump(self):
        self.downp()
        self.jumpp()
        self.jumpr()
        self.downr()

    def upjumpup(self):
        print(f'upjumpup')
        self.jumpp()
        self.jumpr()
        self.upp()
        self.jumpp()
        self.jumpr()
        self.upr()

    ############### ENTER PORTAL ALGORITHM ###################

    def portalenterorskip(self,x,y):
        if self.gotoportal1:
            if not self.goingtoportal and not (x >= self.plbm2 and x <= self.prbp2):
                self.firstx = x
                if x>175.5: # dangerous portal
                    keyupall()
                    keyupall_arrow()
                    print(f'pressing left only (portal) {x=} {y=} ..')  
                    self.leftp()
                elif x < self.plb:
                    self.rightp()
                    self.upp()
                    self.upr()
                    print(f'pressing right up ..')  
                elif x > self.prb:
                    self.leftp()
                    self.upp()
                    self.upr()
                    print(f'pressing left up ..')  
                self.goingtoportal=True
                return
            elif x >= self.plbm2 and x <= self.prbp2:
                # print(f'goingtoportal equals true ..')
                self.goingtoportal = True
                self.tries=55
            if self.goingtoportal:
                print(f'{x=} {y=} {self.tries=}')
                if x > self.preventgotonextmap: # got a portal to other map, prevent that
                    keyupall()
                    keyupall_arrow()
                    print(f'dangerous portal soon. stopping. ')
                    self.gotoportal1=False
                    self.goingtoportal=False
                    self.tries=0
                    return
                self.upp(31,71) # tongx
                self.upr(3,11)
                if y <= self.successthresholdy:
                    print(f'successfully use portal (out). {y=}')
                    keyupall()
                    keyupall_arrow()
                    self.gotoportal1=False
                    self.goingtoportal=False
                    self.tries=0
                    return
                else:
                    if self.firstx < self.plb:
                        if x > self.prb:
                            self.tries=55
                    if self.firstx > self.prb:
                        if x < self.plb:
                            self.tries=55
                    self.tries+=1
                    if self.tries > 55:
                        print(f'tries finished. ')
                        keyupall()
                        keyupall_arrow()
                        self.gotoportal1=False
                        self.goingtoportal=False
                        self.tries=0
                        
                        if x >= self.plbm2 and x <= self.prbp2:
                            print(f'send300 gotoportal1 [test=1s]')
                            keyupall()
                            keyupall_arrow()
                            self.gotoportal1=False
                            self.goingtoportal=False
                            self.tries=0
                            # while True:
                            for i in range(15): # hopefully don't stucked forever
                                g_variable = self.g.get_player_location() # double checking
                                x, y = (None, None) if g_variable is None else g_variable
                                if x == None:
                                    pass
                                else:
                                    if y <= self.successthresholdy:
                                        keyupall()
                                        keyupall_arrow()
                                        print(f'successfully use portal. {y=} [test=2s]')
                                        break
                                    else:
                                        print(f'uppr saves, x, {x} {y=}')
                                        if x < self.plb:
                                            print(f'self.plb')
                                            self.rightp(111,171)
                                            self.rightr(11,71)
                                        elif x > self.prb:
                                            print(f'self.prb')
                                            self.leftp(111,171)
                                            self.leftr(11,71)
                                        if x >= self.preventgotonextmap:
                                            self.leftp(171,211)
                                            self.leftr(11,71)
                                        else:
                                            self.upp(31,101)
                                            self.upr(31,101)
                                            sleep(.010)

    ################## REFACTORED RUNE SOLVING PATCH ######################

    def runegoupmovement(self,x=31,y=101):
        print(f'runegoupmovement')
        self.ropeconnectpr()
        # time.sleep(1.7) already sleep in gotorune function

    def runegodownmovement(self,x=31,y=101):
        print(f'runegodownmovement')
        self.downjump()
        # time.sleep(1.7) # already sleep in gotorune function

    def runegoleftmovement(self,x=31,y=101):
        print(f'runegoleftmovement')
        self.goleftattack_fjump()
        time.sleep(.7)

    def runegorightmovement(self,x=31,y=101):
        print(f'runegorightmovement')
        self.gorightattack_fjump()
        time.sleep(.7)

    def solving_rune(self):
        self.stoprune=False
        g_variable = self.g.get_rune_location()
        x, y = (None, None) if g_variable is None else g_variable
        if x == None:
            print(f'x==None..continue..means..no..rune..')
            return     
        else:
            print(f'rune location: {x=} {y=}')
            purpdist = x
            lowdist = x - 2
            highdist = x + 2
            height = y + 1  # LOL
        prevhigh = 0
        prevhighcount = 0
        counter = 0
        lastdistance = 0
        lastheight = 0
        theI = 0
        keyupall()
        while (True):
            if self.stoprune:
                return
            while (True):
                print(f'theI {theI}')
                theI += 1
                if theI > 24:
                    print(f'{theI} tries already! are you stucked!? returning .. ')
                    return
                r = random.randint(1, 4)
                r /= 1000
                sleep(r)
                g_variable = self.g.get_player_location()
                x, y = (None, None) if g_variable is None else g_variable
                if x == None:
                    print(f'x==None..continue..means..no..player..something blocking bruh ..f')
                    r = random.randint(900, 1100)
                    r /= 1000
                    sleep(r)
                else:
                    break
            print(f'solving rune? 1 ..')
            if (x >= lowdist and x <= highdist):
                print(f'playerx: {x}, playery: {y}, height: {height}, {purpdist =}')
                h1 = 3
                if y >= height-h1 and y <= height+h1:
                    print('already at rune position')
                    r = random.randint(770, 920)
                    r /= 1000
                    sleep(r)
                    print(f'pressing npc ..')
                    self.npcp(3,11)
                    self.npcr()
                    print(f'done pressing npc ..')
                    r = random.randint(1000, 1700)
                    r /= 1000
                    sleep(r)
                    self._solve_rune()
                    return
                else:
                    if y == prevhigh:
                        prevhighcount += 1
                        if prevhighcount > 6:
                            self.leftp()
                            self.jumpp()
                            self.jumpr()
                            self.leftr()
                    if abs(y - prevhigh) < 15:
                        yinyang=False
                    prevhigh = y
                    if y > height:
                        print(y)
                        print(height)
                        if abs(y-height) < 15:
                            self.runegoupmovement() # self.jumpupjumpattack()
                        else:
                            self.runegoupmovement() # self.ropeconnectpr()
                        r = random.randint(1000, 1700)
                        r /= 1000
                        sleep(r)
                    else:
                        print(y)
                        print(height)
                        if abs(y-height<15):
                            self.runegodownmovement() # self.downjump()
                        else:
                            self.runegodownmovement() # self.downjumpv2()
                        r = random.randint(1000, 1500)
                        r /= 1000
                        sleep(r)
                    r = random.randint(500, 900)
                    r /= 1000
                    sleep(r)
            else:
                distance = x - purpdist
                theight = y - height
                print(f'distance: {distance}, {lastdistance}, {purpdist=}, {x=}, ')
                if lastdistance - distance == 0:
                    if lastheight - theight == 0:
                        counter += 1
                        if counter > 55:
                            self.leftp()
                            self.jumpp()
                            self.jumpr()
                            self.leftr()
                else:
                    counter = 0
                lastdistance = distance
                lastheight = theight
                if distance > 30 or distance < -30:
                    if distance > 30:
                        print('hey distance > 30', distance)
                        self.runegoleftmovement() 
                    if distance < -30:
                        self.runegorightmovement() 
                elif distance > 0:
                    distances = int(distance * 100 / 2.0)
                    print(f'> 0 {distances}')
                    self.leftp(distances-50, distances+50)
                    self.leftr(100, 300)
                    print(f'height: {height}')
                    if height == 32:
                        time.sleep(.6)
                    pass
                elif distance < 0:
                    distances = int(abs(distance) * 100 / 2.0)
                    print(f'< 0 {distances}')
                    self.rightp(distances-50, distances+50)
                    self.rightr(100, 300)
                    if height == 32:
                        time.sleep(.6)
                    pass
                elif distance == 0:
                    pass

    def _solve_rune(self):
        now=perf_counter()
        print('_solve_rune: solving rune ..')
        position = win32gui.GetWindowRect(self.maplehwnd)
        x, y, w, h = position
        runepos = (x+121, y+143, x+697, y+371) # 800x600
        # runepos = (x+221, y+143, x+797, y+371) # 1074x768
        # runepos = (x+341, y+143, x+917, y+371) # 1280x720
        # runepos = (x+381, y+143, x+957, y+371) # 1366x768
        # runepos = (x+631, y+143, x+1207, y+371) # 1920x1080 # if this coordinate not work, lemme know!
        print(x,y,w,h)
        screenshot = ImageGrab.grab(runepos,all_screens=True)
        # screenshot.show()
        # time.sleep(5)
        img = np.array(screenshot)
        sendjson = {
            'image': img.tolist()
        }
        link = 'http://'+self.ipaddress+':8001/'
        link = link + 'predict'
        r = requests.post(url=link, json=sendjson)
        json_data = json.loads(r.text)
        print(json_data['prediction'])
        sms = json_data['prediction']
        for i in range(len(sms)):
            print(sms[i:i+1])
            if sms[i:i+1] == 'u':
                print('up')
                self.upp(3,11)
                self.upr(101,171)
            if sms[i:i+1] == 'd':
                print('down')
                self.downp(3,11)
                self.downr(101,171)
            if sms[i:i+1] == 'l':
                print('left')
                self.leftp(3,11)
                self.leftr(101,171)
            if sms[i:i+1] == 'r':
                print('right')
                self.rightp(3,11)
                self.rightr(101,171)
            time.sleep(0.001)
        print(f'{perf_counter()-now=}')

    #################### DEFAULT ROTATION. WRITE YOUR CUSTOM ROTATION HERE. ####################################

    def default(self,x,y):
        if x < 30.5:
            random.choice([self.gorightattack_fjump])()
        elif x >= 30.5:
            random.choice([self.goleftattack_fjump])()
        self.post_perform_action(x,y)

    ################## POST_PERFORM_ACTION ALWAYS PUT AT LAST FOR EASY TO READ ########################

    def post_perform_action(self,x,y):
        self.now = perf_counter()
        self.randomtimer = self.now - self.randomtimer0
        if self.randomtimer > 15:
            self.randomtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                self.send2(code)
                self.send3(code)
        # self.fountaintimer = self.now - self.fountaintimer0
        # if self.fountaintimer > 59:
        #     self.fountain = True
        
    ############ RANDOMISER PATCH ###############

    def send2(self, code):
        keydown(code)
        r = random.randint(31, 131)
        r /= 1000
        sleep(r)

    def send3(self, code):
        keyup(code)
        r = random.randint(31, 131)
        r /= 1000
        sleep(r)

    ## better naming. yes. 
    def bum_(self, code, x=31, y=131):
        keydown(code); sleep(random.uniform(x,y))

    def _bum(self, code, x=31, y=131):
        keyup(code); sleep(random.uniform(x,y))

    def bee_(self, code, x=31, y=131):
        keydown_arrow(code); sleep(random.uniform(x,y))

    def _bee(self, code, x=31, y=131):
        keyup_arrow(code); sleep(random.uniform(x,y))

    def _bumblebee(self, code, x=31, y=131):
        keyupall(code); sleep(random.uniform(x,y))

    def _beeblebum(self, code, x=31, y=131):
        keyupall_arrow(code); sleep(random.uniform(x,y))

    # test purpose

    def testnpc(self):
        self.npcp()
        self.npcr()

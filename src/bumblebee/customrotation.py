import random
import time
from time import perf_counter
# from configparser import ConfigParser
from action import Action
from initinterception import sleep








class Customrotation(Action):

    def __init__(self):
        super().__init__()
        self.offsety=5
        self.offsetx=15
        self.goleft=True
        self.goright=False
        # self.randomlist = ['z', 'x', 'c', 'space', '2', '3', '0', 'f9', 'w', 'e', 'r', 't', 's', 'd', 'f', 'v']
        self.randomlist = ['b', '0', 'u', '9', 'a', 'c', 'r', 'z', 'ctrl', 'home', 'f', 'f', 'f']
        self.cosmicshowerplanttimer0=0
        self.cosmicshowerplanttimer=0
        self.cosmicshowerplant=True
        self.SStimer0=0
        self.SStimer=0
        self.SS=True
        self.HHtimer0=0
        self.HHtimer=0
        self.HH=True
        self.GGtimer0=0
        self.GGtimer=0
        self.GG=True
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
        ## enter portal algorithm variable goes here
        self.goingtoportal=False
        self.gotoportal1=False
        self.gotoportal2=False
        self.gotoportal3=False
        self.gotoportal4=False
        self.tries=0
        self.plb=164.5 # portal left boundary
        self.prb=165.5 # portal right boundary
        self.plbm2=self.plb-2 # portal left boundary minus two, 71.5
        self.prbp2=self.prb+2 # portal right boundary plus two, 76.5
        self.successthreshold=180.5 # what will be the coordinate of your character if successfully entered portal. 
        self.successthresholdy=39.5 # what will be the coordinate of your character if successfully entered portal. 
        self.preventgotonextmap=175.5 # if there is a goto next map portal, put here
        ## enter portal algorithm variable ends here
        self.rotation_list = ['default', 'leftright', 'leftrightlong', 'leftrightdownlong', 'leftrightuplong',
            'moonbridge','arcana_lp', 'arigatou', 'coridor7']
        self.rotation='default'
        self.rotation_mapping = {
            'default': self.clockwise,
            'leftright': self.leftright,
            'leftrightlong': self.leftrightlong,
            'leftrightdownlong': self.leftrightdownlong,
            'leftrightuplong': self.leftrightuplong,
            'moonbridge': self.moonbridge,
            'arcana_lp': self.arcana_lp,
            'arigatou': self.arigatou,
            'coridor7': self.coridor7,

        }

    def define(self):
        pass

    # def setup(self,runesolver,g,rotation):
    #     if runesolver is not None:
    #         self.runesolver=runesolver
    #     if rotation is not None:
    #         self.rotation=rotation
    #     if g is not None:
    #         self.g=g
        
    async def perform_next_attack(self, x, y):
        # await self.limen1_7(x,y)
        # await self.clockwise(x,y)
        # print(f'{self.rotation=}')
        await self.rotation_mapping[self.rotation](x,y)
        
    def get_rotation_list(self):
        return self.rotation_list
        
    def set_rotation(self, rotation):
        self.rotation = rotation
        print(f'{self.rotation=}')

    # basic 4x direction movement (goleft, goright, gooup, godown)
    async def goleftattack(self):
        print(f'goleftattack')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goleftattack2(self):
        print(f'goleftattack2')
        await self.leftp()
        await self.jumpp(222,388)
        await self.jumpr(3,11)    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def gorightattack(self):
        print(f'gorightattack')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def gorightattack2(self):
        print(f'gorightattack2')
        await self.rightp()
        await self.jumpp(222,388)
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goupattack(self): # adele upjump
        print(f'goupattack')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        print(f'press ropeconnect once. ')
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await sleep(.555)
        print(f'press ropeconnect twice. ')
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        print(f'attack.  ')
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def goupattack2(self): # adele upjump
        print(f'goupattack2')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        print(f'press ropeconnect once. ')
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await sleep(.888)
        print(f'press ropeconnect twice. ')
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        print(f'attack.  ')
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack(self):
        print(f'godownattack')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.downr()

    # variation of 4 basic movement to make sequence more randomise.
    async def goleftattackk(self):
        print(f'goleftattackk')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        
    async def goattackleft(self):
        print(f'goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.leftr()

    async def goattackkleft(self):
        print(f'goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.leftr()
    
    async def gorightattackk(self):
        print(f'gorightattackk')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.rightr()
    
    async def goattackright(self):
        print(f'goattackright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()  
        await self.jumpp()
        await self.jumpr()
        await self.rightr()

    async def goattackkright(self):
        print(f'goattackkright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()  
        await self.jumpp()
        await self.jumpr()
        await self.rightr()

    async def upjumpattack(self):
        print(f'upjumpattack')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)
    
    # adele customization

    async def goleftattadele(self):
        print(f'goleftattadele')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.leftr()

    async def goleftattadele2(self):
        print(f'goleftattadele2')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.leftr()

    async def gorightattadele(self):
        print(f'gorightattadele')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.rightr()

    async def gorightattadele2(self):
        print(f'gorightattadele2')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.attackp()
        await self.attackr()
        await self.fp()
        await self.fr()
        await self.rightr()

    async def stormwing(self,x,y,goleft,goright):
        if goright:
            if y < self.top:
                await self.godownattack()
                time.sleep(.3)
            elif y > self.top:
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
            if x > self.right:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.1)
                goright=False
                goleft=True
        elif goleft:
            if y < self.top:
                await self.godownattack()
                time.sleep(.3)
            elif y > self.top:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.1)
            if x < self.left: # only if x < left
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                time.sleep(.1)
                goright=True
                goleft=False
        return goleft,goright

    # zero patch for additional custom attacks
    
    async def zeroZatt(self):
        # print(f'aaaa')
        await self.zp()
        await self.zr()
        
    async def zeroXatt(self):
        # print(f'aaaa')
        await self.xp()
        await self.xr()
        
    async def zeroCatt(self):
        # print(f'aaaa')
        await self.cp()
        await self.cr()
        
    async def zeroVatt(self):
        # print(f'aaaa')
        await self.vp()
        await self.vr()
        
    async def zeroAatt(self):
        # print(f'aaaa')
        await self.ap()
        await self.ar()
        
    async def zeroSatt(self):
        # print(f'aaaa')
        await self.sp()
        await self.sr()
        
    async def zeroDatt(self):
        # print(f'aaaa')
        await self.dp()
        await self.dr()
        
    async def zeroFatt(self):
        # print(f'aaaa')
        await self.fp()
        await self.fr()

    # soul master actions patch for limen 1-7
    
    async def rightupjump(self):
        print(f'rightupjump')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.rightr(3,11)
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        time.sleep(.1)

    async def leftupjump(self):
        print(f'leftupjump')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.leftr(3,11)
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        time.sleep(.1)

    async def rightjumpattack(self):
        print(f'rightjumpattack')
        await self.rightp()
        await self.jumpp(131,211)
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def jumpropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        await self.ropeconnectp(x,y)
        await self.ropeconnectr(x2,y2)

    async def ropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        await self.ropeconnectp(x,y)
        await self.ropeconnectr(x2,y2)

    async def cosmicshower(self):
        r = random.randint(2,4)
        for i in range(r):
            await self.bp(101,177)
            await self.br()

    async def faceleftfountain(self):
        await self.leftp()
        await self.leftr()
        await self.fountainp()
        await self.fountainr()
        time.sleep(.1)

    async def facerightfountain(self):
        await self.rightp()
        await self.rightr()
        await self.fountainp()
        await self.fountainr()
        time.sleep(.1)

    async def walkleft(self,distance=1):
        print(f'walkleft for {distance=}')
        if distance > 9:
            x=int(distance*33)
            y=int(distance*66)
        else:
            # x=int(distance*88)
            # y=int(distance*144)
            x=int(distance*77)
            y=int(distance*99)
        await self.leftp(x,y)
        await self.leftr()
        # if distance <= 2:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 4:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 6:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 8:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # else:
        #     await self.leftp(distance*388,distance*444) # calculate sleep time according to distance. 
        #     await self.leftr()
            
    async def walkright(self,distance=1):
        print(f'walkright for {distance=}')
        if distance > 9:
            x=int(distance*33)
            y=int(distance*66)
        else:
            # x=int(distance*88)
            # y=int(distance*144)
            x=int(distance*77)
            y=int(distance*99)
        await self.rightp(x,y)
        await self.rightr()
        # if distance <= 2:
        #     await self.rightp(x,y)
        #     await self.rightr()
        # elif distance <= 4:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # elif distance <= 6:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # elif distance <= 8:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # else:
        #     await self.rightp(distance*388,distance*444) # calculate sleep time according to distance. 
        #     await self.rightr()


    async def limen1_7(self,x,y):    
        if y > 34.5 and y <= 47.5:
            if x > 84.5 and x <= 120.5:
                if self.cosmicshowerplant:
                    if x >= 102.5 and x <= 104.5:
                        await random.choice([self.jumpropeconnectpr])(x2=999,y2=1222)
                        time.sleep(.1)
                        await random.choice([self.cosmicshower])()
                    elif x < 102.5:
                        # await random.choice([self.walkright])(102.5-x)
                        # time.sleep(.1)
                        # await random.choice([self.jumpropeconnectpr])(x2=999,y2=1222)
                        # time.sleep(.1)
                        # await random.choice([self.cosmicshower])()
                        await random.choice([self.rightupjump])()
                        return
                    elif x > 104.5:
                        # await random.choice([self.walkleft])(x-104.5)
                        # time.sleep(.1)
                        # await random.choice([self.jumpropeconnectpr])(x2=999,y2=1222)
                        # time.sleep(.1)
                        # await random.choice([self.cosmicshower])()
                        await random.choice([self.leftupjump])()
                        return
                    else: # should be no else case here
                        print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                    self.cosmicshowerplant=False
                    self.cosmicshowerplanttimer0=perf_counter()
                    return # done, go next loop. 
                else:
                    pass # do nothing, proceed to check goleft goright
            if self.goleft:
                if x > 57.5:
                    await random.choice([self.goleftattack, self.goleftattack2])()
                else:
                    if self.fountain:
                        await random.choice([self.goupattack])()
                    self.goright=True
                    self.goleft=False
            elif self.goright:
                if x < 140.5:
                    await random.choice([self.gorightattack, self.gorightattack2])()
                else:
                    # await random.choice([self.rightjumpattack])()
                    # time.sleep(.05)
                    await random.choice([self.goleftattack, self.goleftattack2])()
                    self.goright=False
                    self.goleft=True
        else: # means platform other than ground floor
            if x >= 28.5 and x <= 57.5:
                if y > 18.5 and y <= 29.5:
                    if self.fountain:
                        if x >= 37.5 and x <= 38.5:
                            await random.choice([self.facerightfountain])()
                        elif x >= 53.5 and x <= 57.5:
                            await random.choice([self.faceleftfountain])()
                        elif x > 38.5 and x <= 45.5:
                            await random.choice([self.walkleft])(x-38.5)
                            time.sleep(.1)
                            await random.choice([self.facerightfountain])()
                        elif x > 45.5 and x < 53.5:
                            await random.choice([self.walkright])(53.5-x)
                            time.sleep(.1)
                            await random.choice([self.faceleftfountain])()
                        elif x < 37.5:
                            await random.choice([self.walkright])(37.5-x)
                            time.sleep(.1)
                            await random.choice([self.facerightfountain])()
                        else:
                            print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                        self.fountain=False
                        self.fountaintimer0=perf_counter()
                    else:
                        await random.choice([self.gorightattack, self.gorightattack2])()
                elif y <= 18.5:
                    await random.choice([self.gorightattack, self.gorightattack2])()
                else:
                    print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
            elif x > 57.5 and x <= 84.5:
                await random.choice([self.gorightattack, self.gorightattack2])()
            elif x > 84.5 and x <= 120.5:
                if y <= 23.5:
                    if self.cosmicshowerplant:
                        if x >= 102.5 and x <= 104.5:
                            await random.choice([self.cosmicshower])()
                        elif x < 102.5:
                            await random.choice([self.walkright])(102.5-x)
                            time.sleep(.1)
                            await random.choice([self.cosmicshower])()
                        elif x > 104.5:
                            await random.choice([self.walkleft])(x-104.5)
                            time.sleep(.1)
                            await random.choice([self.cosmicshower])()
                        else: # should be no else case here
                            print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                        self.cosmicshowerplant=False
                        self.cosmicshowerplanttimer0=perf_counter()
                    else:
                        await random.choice([self.godownattack])()
                else: # any y platform other than top platform
                    # if self.goleft:
                    #     await random.choice([self.goleftattack])() 
                    # elif self.goright:
                    #     await random.choice([self.gorightattack])()
                    # else:
                    #     await random.choice([self.gorightattack])()
                    await random.choice([self.gorightattack, self.gorightattack2])()
            elif x > 120.5 and x <= 165.5:
                if y <= 28.5:
                    if x >= 138.5 and x <= 142.5: # ladder
                        await random.choice([self.goleftattack, self.goleftattack2])()
                    else:
                        await random.choice([self.godownattack])()
                else: # should be no else case here
                    print(f'if ever character stucked at this point, assign an action. {x=} {y=}')

        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                await self.send2(code)
                await self.send3(code)                
        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # polocheckertimer = self.now - self.polocheckertimer0
        # if polocheckertimer > 90:
        #     self.pausepolochecker=False
        self.runetimer = self.now - self.runetimer0
        # if runetimer > 600: # change to 600 when haste
        if self.runetimer > 900: # change to 600 when haste
            self.checkrune = True
            # self.checkrune = False
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} {statuetimer=} {fountaintimer=}, {runetimer=}, {cctimer=}')
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft=} gr={self.goright=}')
        # print(f'{x=} {y=} {self.runetimer} {self.solverune} | {self.left}, {self.top}, {self.right}, {self.btm} | {self.left1}, {self.top1}, {self.right1}, {self.btm1}')
        # print(f'{x=}, {y=} | {left=}, {top=}, {right=}, {btm=} | {left1=}, {top1=}, {right1=}, {btm1=}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        # elif self.polochecker:
        #     if self.whitedotoccur:
        #         if not await self.polocheckerfunc(self.gotoportal):
        #             self.replaceropeconnect=True
        #         self.whitedotoccur=False
        #     else:
        #         await self.polocheckerfunc(self.gotoportal)
        else:
            pass






    async def clockwise(self,x,y):
        if y > self.top and (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x > self.left+self.offsetx:
                if x < self.left+self.offsetx+5:
                    await random.choice([self.leftwalk])()
                else:
                    await random.choice([self.goleftattack, self.goleftattackk])()
            elif x < self.left-self.offsetx:
                if x > self.left-self.offsetx-5:
                    await random.choice([self.rightwalk])()
                else:
                    await random.choice([self.gorightattack, self.gorightattackk])()
            elif x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.goupattack_v3])()
                else:
                    await random.choice([self.goupattack])()
        elif y <= self.top+self.offsety and y > self.top-self.offsety:
            if x < self.right-self.offsetx:
                await random.choice([self.gorightattack, self.gorightattackk])()
            elif x > self.right+self.offsetx:
                await random.choice([self.goleftattack, self.goleftattackk])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
        elif y > self.top and not (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.goupattack_v3])()
                else:
                    await random.choice([self.goupattack])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
            else:
                if x < ((self.right-self.left)/2):
                    if self.replaceropeconnect:
                        await random.choice([self.goupattack_v3])()
                    else:
                        await random.choice([self.goupattack])()
                elif x >= ((self.right-self.left)/2):
                    await random.choice([self.godownattack])()
        else:
            await random.choice([self.godownattack])()

        await self.post_perform_action(x,y)




            
    async def moonbridge(self,x,y):
        print(f'moonbridge adele: {x=} {y=} l={self.left} r={self.right} t={self.top} b={self.btm} ox={self.offsetx} oy={self.offsety}')
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                    await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
                elif y <= self.top-self.offsety:
                    await random.choice([self.godownattack])()
                else:
                    await random.choice([self.goupattack2])()
                    time.sleep(.2)
                print(f'testing: heightdiff={y-self.top}')
            elif x < self.left:
                await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
            else:
                await random.choice([self.goleftattack, self.goleftattackk, self.goleftattadele, self.goleftattadele2])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
                else:
                    if x>=160.5 and x<=162.5:
                        await random.choice([self.leftwalk])()
                    await random.choice([self.godownattack])()
                    time.sleep(.2)
            elif x > self.right:
                await random.choice([self.goleftattack, self.goleftattackk, self.goleftattadele, self.goleftattadele2])()
            else:
                await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        await self.post_perform_action(x,y)

    async def leftrightuplong(self,x,y):
        print(f'{x=} {y=} l={self.left} r={self.right} t={self.top} b={self.btm} ox={self.offsetx} oy={self.offsety}')
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                    await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
                elif y <= self.top-self.offsety:
                    await random.choice([self.godownattack])()
                else:
                    await random.choice([self.goupattack2])()
                    time.sleep(.2)
                print(f'testing: heightdiff={y-self.top}')
            else:
                await random.choice([self.goleftattack, self.goleftattackk, self.goleftattadele, self.goleftattadele2])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
                else:
                    if x>=160.5 and x<=162.5:
                        await random.choice([self.leftwalk])()
                    await random.choice([self.godownattack])()
                    time.sleep(.2)
            else:
                await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        await self.post_perform_action(x,y)
        
    async def arcana_lp(self,x,y):
        print(f'{self.right=} {self.offsetx=}')
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                    await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
                else:
                    await random.choice([self.upjumpattack])()
                    time.sleep(.2)
                print(f'testing: heightdiff={y-self.top}')
            else:
                await random.choice([self.goleftattack, self.goleftattackk, self.goleftattadele, self.goleftattadele2])()
        elif self.goright:
            if x >=93.5 and x<= 95.5:
                await random.choice([self.rightwalk])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
                else:
                    await random.choice([self.godownattack])()
                    time.sleep(.6)            
            else:
                await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        await self.post_perform_action(x,y)

    async def leftrightdownlong(self,x,y):
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                    await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
                else:
                    await random.choice([self.upjumpattack])()
                    time.sleep(.2)
                print(f'testing: heightdiff={y-self.top}')
            else:
                await random.choice([self.goleftattack, self.goleftattackk, self.goleftattadele, self.goleftattadele2])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
                else:
                    await random.choice([self.godownattack])()
                    time.sleep(.6)
            else:
                await random.choice([self.gorightattack, self.gorightattackk, self.gorightattadele, self.gorightattadele2])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        await self.post_perform_action(x,y)
            
    async def leftrightlong(self,x,y):
        # print(f'{x=} {y=} l={self.left} t={self.top} r={self.right} b={self.btm}')
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                    await random.choice([self.gorightattack, self.gorightattackk])()
                else:
                    await random.choice([self.upjumpattack])()
                    time.sleep(.2)
                print(f'testing: heightdiff={y-self.top}')
            else:
                await random.choice([self.goleftattack, self.goleftattackk])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
            else:
                await random.choice([self.gorightattack, self.gorightattackk])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        # time.sleep(2)
        await self.post_perform_action(x,y)



    async def leftright(self,x,y):
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                await random.choice([self.upjumpattack])()
                time.sleep(.2)
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                print(f'testing: heightdiff={y-self.top}')
            elif x < self.left:
                await random.choice([self.gorightattack, self.gorightattackk])()
            else:
                await random.choice([self.goleftattack, self.goleftattackk])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:                
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    await random.choice([self.goupattack])()
                else:
                    await random.choice([self.godownattack])()
                self.goleft=True
                self.goright=False
            elif x > self.right:
                await random.choice([self.goleftattack, self.goleftattackk])()
            else:
                await random.choice([self.gorightattack, self.gorightattackk])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')
        await self.post_perform_action(x,y)
        


    async def arigatou(self, x,y):
        await self.leftp(1000,1200)
        await self.leftr()
        await sleep(2.0)



    ############################# WINDBREAKER CORIDOR 7 ROTATION #####################################

    async def wbgoup(self):
        print(f'wbgoup')
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        time.sleep(.1)
        time.sleep(.3) # temp # for testing only

    async def wbgodown(self):
        print(f'wbgodown')
        await self.downp()
        await self.jumpp()
        await self.jumpr()
        await self.downr()
        await self.attackp()
        await self.attackr()
        time.sleep(.1)
        time.sleep(.3) # temp # for testing only

    async def wbgoright(self):
        print(f'wbgoright')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()
        time.sleep(.1)
        # time.sleep(.3) # temp # for testing only

    async def wbgoright2(self):
        print(f'wbgoright2')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()
        time.sleep(.1)
        # time.sleep(.3) # temp # for testing only
        
    async def wbgoright3(self):
        print(f'wbgoright3')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.rightr()
        await self.attackp()
        await self.attackr()
        time.sleep(.3)
        await self.teleportp()
        await self.teleportr()
        time.sleep(.1)
        # time.sleep(.3) # temp # for testing only

    async def wbgoleft(self):
        print(f'wbgoleft')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        time.sleep(.1)
        time.sleep(.2) # temp # for testing only

    async def wbgoleft2(self):
        print(f'wbgoleft2')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        time.sleep(.1)
        time.sleep(.2) # temp # for testing only

    async def wbgoleft3(self):
        print(f'wbgoleft3')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.jumpp()
        await self.jumpr()
        await self.leftr()
        await self.attackp()
        await self.attackr()
        time.sleep(.3)
        await self.teleportp()
        await self.teleportr()
        time.sleep(.1)
        time.sleep(.2) # temp # for testing only

    async def afterportal(self):
        print(f'afterportal')
        await self.leftp(171,241)
        await self.leftr()
        time.sleep(.1)
        # time.sleep(.2)

    async def leftteleport(self):
        print(f'leftteleport')
        await self.leftp()
        await self.teleportp()
        await self.teleportr()
        await self.leftr()
        time.sleep(.3)

    async def leftcyclone(self):
        print(f'leftcyclone')      
        await self.vp(350,450)
        await self.vr(3,11)
        await self.leftp()
        await self.yp(71,101)
        await self.yr(340,360)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.attackp()
        await self.attackr()
        await self.leftr(3,11)
        time.sleep(.1)

        # await self.leftp()
        # await self.leftr()
        # await self.cyclone()
        await sleep(.385)

    async def rightcyclone(self):
        print(f'rightcyclone')        
        await self.vp(350,450)
        await self.vr(3,11)
        await self.rightp()
        await self.yp(71,101)
        await self.yr(340,360)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.rightr(3,11)

        # await self.rightp()
        # await self.rightr()
        # await self.cyclone()
        await sleep(.385)

    async def rightcycloneattack(self):
        print(f'rightcycloneattack')        
        time.sleep(.1)
        await self.vp(350,450)
        await self.vr(3,11)
        await self.rightp(31,71)
        await self.rightr(3,11)
        await self.rightp()
        await self.yp(71,101)
        await self.yr(340,360)
        time.sleep(.1)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr(3,11)
        await self.attackp()
        await self.attackr()
        await self.rightr(3,11)
        time.sleep(.1)

        # await self.rightp()
        # await self.rightr()
        # await self.cyclone()
        await sleep(.385)

    async def cyclone(self):
        print(f'cyclone')
        await self.vp(800,1100)
        await self.vr(3,11)
        await self.vr(3,11)
        await self.yp()
        await self.yp(342,372)
        await self.jumpp()
        await self.jumpr(3,11)
        time.sleep(.1)
        
    async def plantfountain(self):
        print(f'plantfountain')
        time.sleep(.1)
        await self.jp()
        await self.jr()
        await self.jp()
        await self.jr()
        await self.jp()
        await self.jr()
        time.sleep(.1)
        await self.wbgodown()


    async def coridor7(self,x,y):
        # right map portal = (177.5,69.5)
        # teleport portal = (164.5~165.5, 69.5)
        # 38.5
        if self.goingtoportal or self.gotoportal1 or self.gotoportal2 or self.gotoportal3 or self.gotoportal4:
            pass
        else:
            # if x >= self.plb-10 and x <= self.prb+10:
            #     if y > 39.5:
            #         # await random.choice([self.wbgoup])()
            #         self.gotoportal1=True
            #     elif y <= 39.5:
            #         await random.choice([self.wbgoleft, self.wbgoleft2, self.wbgoleft3])()
            #     elif y <= 53.5:
            #         await random.choice([self.wbgodown])()
            # elif x > 175.5:
            #     await random.choice([self.leftteleport])()
            # else:
            #     if y <= 53.5:
            #         await random.choice([self.wbgodown])()
            #     elif y > 39.5:
            #         if x < self.plb:
            #             await random.choice([self.wbgoright, self.wbgoright2, self.wbgoright3])()
            #         elif x > self.prb:
            #             await random.choice([self.wbgoleft, self.wbgoleft2, self.wbgoleft3])()
            #         else:
            #             print(f'error {x=} {y=}')

            print(f'{x=} {y=} {self.goingtoportal=} {self.gotoportal1=} {self.goleft=} {self.goright=}')

            if self.fountain:
                if y <= 40.5:
                    if x >= 45.5 and x <= 70.5:
                        print(f'fountain11111111111111111111 {x=} {y=}')
                        print(f'fountain11111111111111111111 {x=} {y=}')
                        print(f'fountain11111111111111111111 {x=} {y=}')
                        print(f'fountain11111111111111111111 {x=} {y=}')
                        await random.choice([self.walkleft])(x-48.5)
                        await random.choice([self.plantfountain])()
                        self.fountaintimer0=perf_counter()
                        self.fountain=False
                    elif x >= 16.5 and x <= 36.5:
                        print(f'fountain2222222222222222222 {x=} {y=}')
                        print(f'fountain2222222222222222222 {x=} {y=}')
                        print(f'fountain2222222222222222222 {x=} {y=}')
                        print(f'fountain2222222222222222222 {x=} {y=}')
                        await random.choice([self.walkright])(33.5-x)
                        await random.choice([self.plantfountain])()
                        self.fountaintimer0=perf_counter()
                        self.fountain=False

            if x >= self.plb-8 and x <= self.prb+8:
                if y > 39.5:
                    if self.gotoportal1:
                        pass    
                    else:
                        # await random.choice([self.wbgoup])()
                        self.gotoportal1=True
                elif y <= 39.5:
                    self.goright=False
                    self.goleft=True
                    await random.choice([self.afterportal])()
                    if self.GG: await self.gpr(); self.GGtimer0=perf_counter(); self.GG=False; time.sleep(.3)
                    elif self.HH: await self.hpr(); self.HHtimer0=perf_counter(); self.HH=False; time.sleep(.3)
                    await random.choice([self.leftcyclone])()
            else:
                if y > 54.5:
                    if x > self.right+10:
                        await random.choice([self.leftteleport])()
                        # await random.choice([self.wbgoleft, self.wbgoleft2, self.wbgoleft3, self.leftcyclone])()
                        self.gotoportal1=True
                    elif x >= self.right:
                        await random.choice([self.walkleft])(x-165.5)
                        self.gotoportal1=True
                    elif x < self.right-15:
                        if x <= 94.5:
                            if self.SS: 
                                await self.spr(); self.SStimer0=perf_counter(); self.SS=False; time.sleep(.444)
                                await random.choice([self.rightcycloneattack])()
                                # await random.choice([self.wbgoright, self.wbgoright2, self.wbgoright3])()
                            else:
                                await random.choice([self.rightcyclone])()
                        else:
                            await random.choice([self.rightcyclone])()
                    elif x <= self.right-10:
                        await random.choice([self.wbgoright, self.wbgoright2, self.wbgoright3])()
                    elif x <= self.right:
                        await random.choice([self.wbgoright, self.wbgoright2, self.wbgoright3])()
                        # await random.choice([self.rightwalk])()
                elif y <= 54.5:
                    if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                        await random.choice([self.wbgodown])()
                    elif x > self.left:
                        await random.choice([self.leftcyclone])()
                    elif x < self.left:
                        await random.choice([self.wbgodown])()
                    else:
                        print(f'error1 {x=} {y=}')
                else:
                    print(f'error2 {x=} {y=}')
            
            


            # if x  <= self.left:
            #     self.goleft=False
            #     self.goright=True
            #     await random.choice([self.rightcyclone])()
            # elif x  >= self.right:
            #     self.goleft=True
            #     self.goright=False
            #     await random.choice([self.leftcyclone])()
            # else:
            #     if self.goleft:
            #         await random.choice([self.leftcyclone])()
            #     elif self.goright:
            #         await random.choice([self.rightcyclone])()

            
            await self.post_perform_action(x,y)

        await self.portalenterorskip(x,y)






    async def post_perform_action(self,x,y):
        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                await self.send2(code)
                await self.send3(code)
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        # if self.cosmicshowerplanttimer > 59:
        #     self.cosmicshowerplant = True
        self.HHtimer = self.now - self.HHtimer0
        if self.HHtimer > 30:
            self.HH = True
        self.SStimer = self.now - self.SStimer0
        if self.SStimer > 15:
            self.SS = True
        self.GGtimer = self.now - self.GGtimer0
        if self.GGtimer > 30:
            self.GG = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 56:
            self.fountain = True
        # self.runetimer = self.now - self.runetimer0
        # # if runetimer > 600: # change to 600 when haste
        # if self.runetimer > 900: # change to 600 when haste
        #     self.checkrune = True
        #     # self.checkrune = False
        # if self.checkrune:
        #     self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')

        # if self.solverune:
        #     await self.runesolver.gotorune(self.g)



























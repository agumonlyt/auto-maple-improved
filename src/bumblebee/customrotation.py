import random
import time
from time import perf_counter
from src.bumblebee.action import Action
from src.bumblebee.initinterception import sleep


class Customrotation(Action):

    def __init__(self):
        super().__init__()

        ########## CUSTOM VARIABLES ########################################
        self.flag=False

        ########## ALL TIMER GOES HERE #####################################
        self.fountaintimer0=0
        self.fountaintimer=0
        self.fountain=True
        self.randommtimer0=0
        self.randommtimer=0
        self.now=0

        ############# PORTAL USAGE ALGORITHM VARIABLES GOES HERE #############
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
        
        ####### CUSTOM ROTATIONS ##############################################################################################
        self.randomlist = ['z', 'z', 'z', 'z', 'z', 'z']
        self.rotation_list = ['default']
        self.rotation='default'
        self.rotation_mapping = {
            'default': self.default,
        }

    def perform_next_attack(self, x, y):
        self.rotation_mapping[self.rotation](x,y)
        


    ############ CUSTOM ROTATION #################################################################################

    def default_left_attack(self):
        print(f'default_left_attack')
        self.leftp(222,333)
        self.attackp()
        self.attackr()
        self.leftr()
        time.sleep(.1)
        time.sleep(.8)

    def default_right_attack(self):
        print(f'default_right_attack')
        self.rightp(222,333)
        self.attackp()
        self.attackr()
        self.rightr()
        time.sleep(.1)
        time.sleep(.8)

    def default(self,x,y):
        if x < 69.5:
            if self.flag:
                self.flag=False
                random.choice([self.default_right_attack])()                
            else:
                random.choice([self.default_left_attack])()
                self.flag=True
        elif x >= 69.5:
            if self.flag:
                self.flag=False
                random.choice([self.default_right_attack])()
            else:
                random.choice([self.default_left_attack])()
                self.flag=True
        self.portal_usage_check(x,y)        
        self.post_perform_action(x,y)

    ############ POST_PERFORM_ACTION #############################################################################

    def post_perform_action(self,x,y):
        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f"pressing random button: '{code}'")
                self.bum_(code)
                self._bum(code)
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 56:
            self.fountain = True












































    ################ LIST OF PREDIFINED ATTACK SEQUENCE ##############################################################
    ################ VERY UGLY CODES #################################################################################
    ################ ADD MORE CUSTOM ATTACK SEQUENCE BELOW ###########################################################

    def goleftattack(self):
        print(f'goleftattack')
        self.leftp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.leftr()

    def goleftattack2(self):
        print(f'goleftattack2')
        self.leftp()
        self.jumpp(222,388)
        self.jumpr(3,11)    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.leftr()

    def gorightattack(self):
        print(f'gorightattack')
        self.rightp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.rightr()

    def gorightattack2(self):
        print(f'gorightattack2')
        self.rightp()
        self.jumpp(222,388)
        self.jumpr(3,11)
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.rightr()

    def goupattack(self): 
        print(f'goupattack')
        sleep(.1)
        self.jumpp()
        self.jumpr()
        print(f'press ropeconnect once. ')
        self.ropeconnectp(31,101)
        self.ropeconnectr(31,101)
        sleep(.555)
        print(f'press ropeconnect twice. ')
        self.ropeconnectp(31,101)
        self.ropeconnectr(31,101)
        print(f'attack.  ')
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def goupattack2(self): 
        print(f'goupattack2')
        sleep(.1)
        self.jumpp()
        self.jumpr()
        print(f'press ropeconnect once. ')
        self.ropeconnectp(31,101)
        self.ropeconnectr(31,101)
        sleep(.888)
        print(f'press ropeconnect twice. ')
        self.ropeconnectp(31,101)
        self.ropeconnectr(31,101)
        print(f'attack.  ')
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.1)

    def godownattack(self):
        print(f'godownattack')
        self.downp()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.downr()

    def goleftattackk(self):
        print(f'goleftattackk')
        self.leftp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.leftr()
        
    def goattackleft(self):
        print(f'goattackleft')
        self.leftp()
        self.attackp()
        self.attackr()
        sleep(.5)
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.leftr()

    def goattackkleft(self):
        print(f'goattackleft')
        self.leftp()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.5)
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.leftr()
    
    def gorightattackk(self):
        print(f'gorightattackk')
        self.rightp()
        self.jumpp()
        self.jumpr()    
        self.jumpp()
        self.jumpr()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        self.rightr()
    
    def goattackright(self):
        print(f'goattackright')
        self.rightp()
        self.attackp()
        self.attackr()
        sleep(.5)
        self.jumpp()
        self.jumpr()  
        self.jumpp()
        self.jumpr()
        self.rightr()

    def goattackkright(self):
        print(f'goattackkright')
        self.rightp()
        self.attackp()
        self.attackr()
        self.attackp()
        self.attackr()
        sleep(.5)
        self.jumpp()
        self.jumpr()  
        self.jumpp()
        self.jumpr()
        self.rightr()

    def upjumpattack(self):
        print(f'upjumpattack')
        sleep(.1)
        self.jumpp()
        self.jumpr()
        self.upp()
        self.jumpp()
        self.jumpr()
        self.upr()
        self.attackp()
        self.attackr()
        sleep(.1)
    
    def rightupjump(self):
        print(f'rightupjump')
        self.rightp()
        self.jumpp()
        self.jumpr()
        self.rightr(3,11)
        self.upp()
        self.jumpp()
        self.jumpr()
        self.upr()
        time.sleep(.1)

    def leftupjump(self):
        print(f'leftupjump')
        self.leftp()
        self.jumpp()
        self.jumpr()
        self.leftr(3,11)
        self.upp()
        self.jumpp()
        self.jumpr()
        self.upr()
        time.sleep(.1)

    def rightjumpattack(self):
        print(f'rightjumpattack')
        self.rightp()
        self.jumpp(131,211)
        self.jumpr()
        self.attackp()
        self.attackr()
        self.rightr()

    def jumpropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        self.ropeconnectp(x,y)
        self.ropeconnectr(x2,y2)

    def ropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        self.ropeconnectp(x,y)
        self.ropeconnectr(x2,y2)

    def faceleftfountain(self):
        self.leftp()
        self.leftr()
        self.fountainp()
        self.fountainr()
        time.sleep(.1)

    def facerightfountain(self):
        self.rightp()
        self.rightr()
        self.fountainp()
        self.fountainr()
        time.sleep(.1)

    def walkleft(self,distance=1):
        print(f'walkleft for {distance=}')
        if distance > 9:
            x=int(distance*33)
            y=int(distance*66)
        else:
            # x=int(distance*88)
            # y=int(distance*144)
            x=int(distance*77)
            y=int(distance*99)
        self.leftp(x,y)
        self.leftr()
            
    def walkright(self,distance=1):
        print(f'walkright for {distance=}')
        if distance > 9:
            x=int(distance*33)
            y=int(distance*66)
        else:
            # x=int(distance*88)
            # y=int(distance*144)
            x=int(distance*77)
            y=int(distance*99)
        self.rightp(x,y)
        self.rightr()
    



















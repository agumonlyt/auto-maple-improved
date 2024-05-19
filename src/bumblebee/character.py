












import random
from action import Action
# from classtype.mycharacterign import Mycharacterign
# from classtype.adele import Adele
# from classtype.angelicbuster import Angelicbuster
# from classtype.aran import Aran
# from classtype.ark import Ark
# from classtype.battlemage import Battlemage
# from classtype.bishop import Bishop
# from classtype.blaster import Blaster
# from classtype.bowmaster import Bowmaster
# from classtype.cadena import Cadena
# from classtype.cannonmaster import Cannonmaster
# from classtype.captain import Captain
# from classtype.crossbowman import Crossbowman
# from classtype.darkknight import Darkknight
# from classtype.demonavenger import Demonavenger
# from classtype.demonslayer import Demonslayer
# from classtype.dualblade import Dualblade
# from classtype.eunwol import Eunwol
# from classtype.evan import Evan
# from classtype.firepoison import Firepoison
# from classtype.flamewizard import Flamewizard
# from classtype.hayato import Hayato
# from classtype.hero import Hero
# from classtype.hoyoung import Hoyoung
# from classtype.icelightning import Icelightning
# from classtype.illium import Illium
# from classtype.kaine import Kaine
# from classtype.kanna import Kanna 
# from classtype.kaiser import Kaiser 
# from classtype.khali import Khali
# from classtype.kinesis import Kinesis
# from classtype.lara import Lara
# from classtype.luminous import Luminous
# from classtype.lynn import Lynn
# from classtype.mechanic import Mechanic
# from classtype.mercedes import Mercedes
# from classtype.mihile import Mihile
# from classtype.moxuan import Moxuan
# from classtype.nightlord import Nightlord
# from classtype.nightwalker import Nightwalker
# from classtype.paladin import Paladin
# from classtype.pathfinder import Pathfinder
# from classtype.phantom import Phantom
# from classtype.shadower import Shadower
# from classtype.soulmaster import Soulmaster
# from classtype.striker import Striker
# from classtype.viper import Viper
# from classtype.wildhunter import Wildhunter
# from classtype.windbreaker import Windbreaker
# from classtype.xenon import Xenon
# from classtype.zero import Zero
from customrotation import Customrotation




class Character:

    def __init__(self) -> None:
        self.top=0
        self.btm=0
        self.left=0
        self.right=0
        self.runesolver=None
        self.g=None
        self.offsety=10
        self.offsetx=10
        self.replaceropeconnect=False
        # self.teleport=True
        # self.ac = Action()
        self.ac = None
        self.classtype = {
            'customrotation': Customrotation,
            # 'mycharacterign': Mycharacterign,
            # 'adele': Adele,
            # 'angelicbuster': Angelicbuster,
            # 'aran': Aran,
            # 'ark': Ark,
            # 'battlemage': Battlemage,
            # 'bishop': Bishop,
            # 'blaster': Blaster,
            # 'bowmaster': Bowmaster,
            # 'cadena': Cadena,
            # 'cannonmaster': Cannonmaster,
            # 'captain': Captain,
            # 'crossbowman': Crossbowman,
            # 'darkknight': Darkknight,
            # 'demonavenger': Demonavenger,
            # 'demonslayer': Demonslayer,
            # 'dualblade': Dualblade,
            # 'eunwol': Eunwol,
            # 'evan': Evan,
            # 'firepoison': Firepoison,
            # 'flamewizard': Flamewizard,
            # 'hayato': Hayato,
            # 'hero': Hero,
            # 'hoyoung': Hoyoung,
            # 'icelightning': Icelightning,
            # 'illium': Illium,            
            # 'kaine': Kaine,
            # 'kaiser': Kaiser,
            # 'kanna': Kanna,
            # 'khali': Khali,
            # 'kinesis': Kinesis,
            # 'lara': Lara,
            # 'luminous': Luminous,
            # 'lynn': Lynn,
            # 'mechanic': Mechanic,
            # 'mercedes': Mercedes,
            # 'mihile': Mihile,
            # 'moxuan': Moxuan,            
            # 'nightlord': Nightlord,
            # 'nightwalker': Nightwalker,
            # 'paladin': Paladin,
            # 'pathfinder': Pathfinder,
            # 'phantom': Phantom,
            # 'shadower': Shadower,
            # 'soulmaster': Soulmaster,
            # 'striker': Striker,
            # 'viper': Viper,
            # 'wildhunter': Wildhunter,
            # 'windbreaker': Windbreaker,
            # 'xenon': Xenon,
            # 'zero': Zero,

            ## previous version. 
            # 'nightlord': Nightlord,
            # 'soulmaster': Soulmaster,
            # 'zero': Zero,
            # 'adele': Adele,
            # 'bowmaster': Bowmaster,
            # 'nightwalker': Nightwalker,
            # 'shadower': Shadower,
            # 'bishop': Bishop,
        }

    def setup(self,left,right,top,btm,classtype=None,runesolver=None,g=None,rotation=None,maplehwnd=None):
        self.left=left
        self.right=right
        self.top=top
        self.btm=btm
        self.ac=self.classtype[classtype]() if classtype is not None else self.ac
        # print(f'{self.ac=} {classtype=}')
        self.ac.left=left
        self.ac.right=right
        self.ac.top=top
        self.ac.btm=btm
        self.ac.setup(runesolver,g,rotation,maplehwnd)
        # print(f'setup complete. {left=} {right=} {top=} {btm=}')
        # print(f'{self.ac.left=} {self.ac.right=} {self.ac.top=} {self.ac.btm=}')

    def change_ac_type(self, classtype):
        if classtype in self.classtype:
            self.ac = self.classtype[classtype]()
            self.offsetx=self.ac.offsetx
            self.offsety=self.ac.offsety
            # print(f'{self.offsetx=} {self.offsety=} {self.classtype=}')
            self.ac.refreshkeybind()

    def refreshkeybind(self):
        self.ac.refreshkeybind()

    # def change_ac_type(self,ac):
        # self.ac=ac
        # if isinstance(self.ac, Flashjump):
        #     print(f'fj: {self.ac=}')
        #     self.offsety=15
        #     self.offsetx=15
        # if isinstance(self.ac, Teleport):
        #     print(f'tp: {type(self.ac)=}')

    async def perform_next_attack(self,x,y):
        await self.ac.perform_next_attack(x,y)

    def get_rotation_list(self):
        return self.ac.get_rotation_list()

    def set_rotation(self,rotation):
        self.ac.set_rotation(rotation)

    async def gotorune(self):
        await self.ac.gotorune()

    async def perform_next_attack2(self,x,y):
        if y > self.top and (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x > self.left+self.offsetx:
                if x < self.left+self.offsetx+5:
                    await random.choice([self.ac.leftwalk])()
                else:
                    await random.choice([self.ac.goleftattack, self.ac.goleftattackk])()
            elif x < self.left-self.offsetx:
                if x > self.left-self.offsetx-5:
                    await random.choice([self.ac.rightwalk])()
                else:
                    await random.choice([self.ac.gorightattack, self.ac.gorightattackk])()
            elif x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.ac.goupattack_v3])()
                else:
                    await random.choice([self.ac.goupattack])()
        elif y <= self.top+self.offsety and y > self.top-self.offsety:
            if x < self.right-self.offsetx:
                await random.choice([self.ac.gorightattack, self.ac.gorightattackk])()
            elif x > self.right+self.offsetx:
                await random.choice([self.ac.goleftattack, self.ac.goleftattackk])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.ac.godownattack])()
        elif y > self.top and not (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.ac.goupattack_v3])()
                else:
                    await random.choice([self.ac.goupattack])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.ac.godownattack])()
            else:
                if x < ((self.right-self.left)/2):
                    if self.replaceropeconnect:
                        await random.choice([self.ac.goupattack_v3])()
                    else:
                        await random.choice([self.ac.goupattack])()
                elif x >= ((self.right-self.left)/2):
                    await random.choice([self.ac.godownattack])()
        else:
            await random.choice([self.ac.godownattack])()


    async def stormwing(self,x,y,goleft,goright):
        return await self.ac.stormwing(x,y,goleft,goright)
    
    async def bountyhuntrotation(self):
        await self.ac.bountyhuntrotation()
    
    async def castlewallrotation(self):
        await self.ac.castlewallrotation()













import random
from src.bumblebee.action import Action
from src.bumblebee.customrotation import Customrotation




class Character:

    def __init__(self) -> None:
        self.action = None
        self.classtype = {
            'customrotation': Customrotation,
        }

    def setup(self,classtype=None,g=None,maplehwnd=None):        
        self.action=self.classtype[classtype]() if classtype is not None else self.action
        self.action.setup(g,maplehwnd)

    def perform_next_attack(self,x,y):
        self.action.perform_next_attack(x,y)

    def gotorune(self):
        self.ac.gotorune()

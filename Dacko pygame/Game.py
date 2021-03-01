from MainMenu import *
from Town import *
from Entity import *
from Monster import*
from PlayerTurn import*
from PlayerAbilities import *
from Abilities import *
from Combat import*


MainMenu(0)

os.system('cls')
Name=input("What is your Character's Name: ")
Name=Name.title()
# Reminder.. Player: ( Name , Hp , En , Stats , Buffs , Potions , Coins , Lvl , Exp , Lvl Points )
Player = Player (Name,[100,100],[5,5],[2,0,2],[],[0,0],0,2,[0,0],0)
Monster = Entity ("Wolf",[15,15],[3,3],[2,2,0],[])


Town(Player,0)

Combat(Player,Monster,1,0,0)


d=input()

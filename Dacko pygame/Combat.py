import random

from PlayerAbilities import *
from Abilities import *
from Entity import*
from PlayerTurn import *

def Speed_Roll(Entity):
    speed_bonus=0
    buffsize=Entity.check_Buff_Size()
    # For i in the size of the buff array
    for i in range(buffsize):
        # Check if there is a buff named Speed
        o=Entity.check_Buff(i,"Speed")
        #If Buff returns TRUE | 1 |
        if o[0]==1:
            #Get value from that buff
            speed_bonus=speed_bonus+o[2]


    speed=random.randrange(1,10)+speed_bonus+Entity.show_Stats()[1]
    if speed<0:
        speed=0
    return speed


def find_Buff(Entity,buff):
    bonus_buff=0
    for i in range(Entity.check_Buff_Size()):
        # Check if there is a buff with the name same as string | buff |
        o=Entity.check_Buff(i,buff)
        #If Buff returns TRUE | 1 |
        if o[0]==1:
            #Get value from that buff
            bonus_buff=bonus_buff+o[1]

    return bonus_buff





    # class PLAYER class MONSTER ROUND (1) TURN (0) DEAD (0) --START-- first time

def Combat(Player,Monster,r,t,d):

    ##ROUND START
    round=r

    turn=t

    #set a dead counter
    dead=d

    while dead==0:
        Player_speed=Speed_Roll(Player)
        Monster_speed=Speed_Roll(Monster)

        #If the monster rolled a higher speed value he goes first aka send class Monster with turn 1st
        if Monster_speed>=Player_speed:
            Current_Turn(Monster,Player,r,turn+1,1)
        else:
            Current_Turn(Player,Monster,r,turn+1,0)


    # Entity current player , Enemy is enemy , t is for turn and Monster_Check is for is it ai (0 NO ||| 1 YES)

def check_Dead(Entity,d):
    if Entity.show_Hp()[0]<=0:
        d=1
        return d
    return d

def Current_Turn(Entity,Enemy,r,t,Monster_Check):

    if int(t / 2)== r:
        if Monster_Check==0:
         Combat(Entity,Enemy,r+1,t,0)
        elif Monster_Check==1:
         Combat(Enemy,Entity,r+1,t,0)
#   print("{0} is Even".format(num))

    #Damage Per Turn
    Dpt=0

    #is Stunned
    Stun=0

    Dpt=find_Buff(Entity,"DPT")
    if Monster_Check==0:
        if check_Dead(Entity,0)==1:
            Lose_Screen(Enemy)

    elif Monster_Check==1:
        if check_Dead(Entity,0)==1:
            Win_Screen(Entity)

    if Dpt>0:
        print( Entity.Name+ " takes "+str(Dpt)+" Damage")
        Entity.Take_Damage(Dpt)

    if Stun>0:
        print (Entity.Name+ " is Stunned this turn ")
        Entity.check_TBuff()
        if Monster_Check==0:
            Current_Turn(Enemy,Entity,t+1,Monster_Check+1)
        elif Monster_Check==1:
            Current_Turn(Enemy,Entity,t+1,Monster_Check-1)

    if Monster_Check==0:
        Player_Turn(Entity,Enemy,r,t)

    elif Monster_Check==1:
        Monster_Turn(Entity,Enemy,r,t,Monster_Check)

def Monster_Turn(Entity,Enemy,r,t,Monster_Check):
     print("Monster turn :\n\n")
     Attack(Entity,Enemy)
     Current_Turn(Enemy,Entity,r,t+1,Monster_Check-1)

def Win_Screen(Player):

    import Town
    print("CONGRATULATIONS YOU KILLED THE MONSTERS")
    print("Go back to town press a")
    a=input()
    if a=="a":
        Town.Town(Player,0)

def Lose_Screen(Player):

    import Town
    print("YOU LOST THE GAME")
    print("Go back to town press a")
    a=input()
    if a=="a":
        Town.Town(Player,0)













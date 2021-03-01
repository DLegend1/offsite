import os
from Entity import *

def Shop_Text(Player):
    print('''
    ############################################
    ############## Greeen Shop #################
    ############################################
    ''')
    print ( "Hello " + Player.Name + " What would you like to buy from my humble shop" )
    print('''


	1.Buy Healing Potion  (2 Coins)
	2.Buy Energy Potion   (2 Coins)
	t.Go back to Town    

    
     ''')

def House_Text(Player):
    print('''
    ############################################
    ########### Home Sweet Home ################
    ############################################

	1.Sleep  (Regain Hp and En)
	t.Go back to Town    

    
     ''')

def Training_Area_Text(Player):
    print('''
    ############################################
    ###########  Training Area  ################
    ############################################
    ''')

    print ( " "+ Player.Name + " \'s stats currently are STR: " + str(Player.show_Stats()[0]) + ", DEX: " + str(Player.show_Stats()[1]) + ", INT: " + str(Player.show_Stats()[2]) + " and currently you are LVL "+ str(Player.show_Lvl()[0]) + "(You have "+ str( Player.show_Lvl()[1]) +" Skill Points to use) ")

    print('''
	1. Knight training grounds (Str)
	2. Assassin training grounds (Dex)
	3. Wizard training grounds (Int)
	t.Go back to Town
    
    '''

     )

def Training_Ground_Text(Player,c):
        print('''  
    ############################################''')
        print("    ########",end='')
        if c==1:
            print (" Knight Training Ground ",end='')
        elif c==2:
            print (" Ninjas Training Ground ",end='')
        elif c==3:
            print (" Wizard Training Ground ",end='')
        print("############")
        print('''    ############################################
    ''')

        print( Player.Name +"'s stats currently are STR: " + str(Player.show_Stats()[0]) + ", DEX: " + str(Player.show_Stats()[1]) + ", INT: " + str(Player.show_Stats()[2]) + " and currently you are LVL "+ str(Player.show_Lvl()[0]) + "(You have "+ str(Player.show_Lvl()[1]) +" Skill Points to use)")

        print('''
    
	1. ''',end='')
        if c==1:
            print("Increase your Str by 1 (Consumes 1 Skill Point)")
        elif c==2:
            print("Increase your Dex by 1 (Consumes 1 Skill Point)")
        elif c==3:
            print("Increase your Int by 1 (Consumes 1 Skill Point)")

        print ("    t.Go back to Training Area")

def Town_Text(Player):



    print('''
    ############################################
    ############ Town of Elzebab ###############
    ############################################
    Hello Adventurer ''' + str(Player.Name) + ''' and welcome to the Town of Elzebab 


	a.Adventure
	1.Shop
	2.House
	3.Training Area
	q.Quit game
    
     ''')



def Shop(Player,b):

    Shop_Text(Player)

    if b==1:
        print("         Invalid Input please try again!!")
    elif b==2:
        print("         Not Enough money to purchase that!!")

    a=input(">...:")

    if a=="1":
        if Player.Check_Coins() >= 2 :
            Player.Get_Potion(1)
        else:
            Shop(Player,2)
    elif a=="2":
        if Player.Check_Coins()>= 2 :
            Player.Get_Potion(2)
        else:
            Shop(Player,2)
    elif a=="t" or a=="T":
        Town(Player,0)
    else:
        os.system('cls')
        Shop(Player,1)

def House(Player,b):

    House_Text(Player)

    if b==1:
        print("         Invalid Input please try again!!")
    if b==2:
        print("         You feel fully refreshed!!!")

    a=input(">...:")

    if a=="1":
        Player.Sleep()
        House(Player,2)
    elif a=="t" or a=="T":
        Town(Player,0)
    else:
        os.system('cls')
        House(Player,1)

def Training_Ground(Player,b,c):

    Training_Ground_Text(Player,c)

    if b==1:
        print("         Invalid Input please try again!!")
    elif b==2:
        print("         Not Enough Skill Points to Raise your Desired Skill")

    a=input(">...:")

    if a=="1" and c==1:

        if Player.show_Lvl()[1]==0:
            os.system('cls')
            Training_Ground(Player,2,c)
        else:
            s=self.show_Stats
            Player.Stat_Increase(s[0]+1,10,0)


    elif a=="1" and c==2:

        if Player.show_Lvl()[1]==0:
            os.system('cls')
            Training_Ground(Player,2,c)
        else:
            s=self.show_Stats
            Player.Stat_Increase(s[1]+1,0,0)

    elif a=="1" and c==3:

        if Player.show_Lvl()[1]==0:
            os.system('cls')
            Training_Ground(Player,2,c)
        else:
            s=self.show_Stats
            Player.Stat_Increase(s[2]+1,0,2)


    elif a=="t" or a=="T":
        Training_Area(Player,0)

    else:
        os.system('cls')
        Training_Ground(Player,1,c)


def Training_Area(Player,b):

    Training_Area_Text(Player)

    if b==1:
        print("         Invalid Input please try again!!")

    a=input(">...:")

    if a=="1":
        Training_Ground(Player,0,1)
    elif a=="2":
        Training_Ground(Player,0,2)
    elif a=="3":
        Training_Ground(Player,0,3)
    elif a=="t" or a=="T":
        Town(Player,0)
    else:
        os.system('cls')
        Training_Area(Player,1)


def Town(Player,b):

    Town_Text(Player)

    if b==1:
        print("         Invalid Input please try again!!")

    a=input(">...:")

    if a=="a":
        a=a
    elif a=="1":
        Shop(Player,0)
    elif a=="2":
        House(Player,0)
    elif a=="3":
        Training_Area(Player,0)
    elif a=="q" or a=="Q":
        quit()
    else:
        os.system('cls')
        Town(Player,1)

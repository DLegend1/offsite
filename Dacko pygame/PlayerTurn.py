from Abilities import *
#from Entity import*



def Player_Text(Player,Monster):

    print('''
    ############################################
    ############     Battle     ################
    ############################################
    
    
    ''')

    print ( " "+ Player.Name + "'s stats currently are \n Hp= "+ str(Player.show_Hp()[0]) + "/" + str(Player.show_Hp()[1]) +" \n En= " + str(Player.show_En()[0]) + "/ " + str(Player.show_En()[1]) +"\n\n " )


    print ( "  "+ Monster.Name + "'s stats currently are \n Hp= "+ str(Monster.show_Hp()[0]) + "/" + str(Monster.show_Hp()[1]) +" \n En= " + str(Monster.show_En()[0]) + "/ " + str(Monster.show_En()[1]) +" \n\n " )







    for i in range(Player.check_Buff_Size()):
        print("You have the following buffs: ",end="")
        print(Player.show_Buff()[i][1] + ": " + str(Player.show_Buff()[i][3]) + "  (" + str(Player.show_Buff()[i][2]) + " Turns ) ,",end="")


    print ( '''
    
	a. Attack 1d6+ Str ( '''+ str (Player.show_Stats()[0]) +''' )
	
	s. Skills / Abilities
	
	d. Use Potion
	>
	>
    ''' )

def Skill_Text(Player):
    options=[]
    reseter
    print("STR abilities: ")
    #ability [0] = 0 STR : 1 DEX : 2 INT
    # Print the Strength abilities with name and energy and descritpion 0 Name - 1 Cost - 2 Description
    for i in range(len (ability)):
        if ability[i][0]==0:
            options.append("s")
            options[i]=options[i]+str(i+1)

            print(options[i]+". "+Strength_Abilities(Player,Monster,2,0)[i][0]+" - "+Strength_Abilities(Player,Monster,2,0)[i][1]+" Energy  ( "+ Strength_Abilities(Player,Monster,2,0)[i][2] +" )")

            if ability[i+1][0]!=0:
                reseter=i+1

    # Print the Dexterity abilities with name and energy and descritpion 0 Name - 1 Cost - 2 Description
    print("DEX abilities: ")
    for i in range(len (ability)):
        if ability[i][0]==1:
            options.append("d")
            options[i]=options[i]+str(i+1)-reseter
            print(options[i]+". "+Dexterity_Abilities(Player,Monster,2,0)[i-reseter][0]+" - "+Dexterity_Abilities(Player,Monster,2,0)[i-reseter][1]+" Energy  ( "+ Dexterity_Abilities(Player,Monster,2,0)[i-reseter][2] +" )")
            if ability[i+1][0]!=0:
                reseter=i+1

    # Print the Intelligence abilities with name and energy and descritpion 0 Name - 1 Cost - 2 Description
    print("INT abilities: ")
    for i in range(len (ability)):
        if ability[i][0]==2:
            options.append("i")
            options[i]=options[i]+str(i+1)-reseter
            print(options[i]+". "+Intelligence_Abilities(Player,Monster,2,0)[i-reseter][0]+" - "+Intelligence_Abilities(Player,Monster,2,0)[i-reseter][1]+" Energy  ( "+ Intelligence_Abilities(Player,Monster,2,0)[i-reseter][2] +" )")

    print("\nback : To go back!")

    return options

def Player_Menu(Player,Monster,ability,r,t):

    Player_Text(Player,Monster)


    a=0
    from Combat import Current_Turn
    while a not in ('a','A','s','S','d','D'):

        a=input(">...:")

        if a=="a" or "A":
            Attack(Player,Monster)
            Current_Turn(Monster,Player,r,t+1,1)

        elif a=="s" or a=="S":
            Skill(Player,Monster,ability)
            Current_Turn(Monster,Player,r,t+1,1)

        elif a=="d" or a=="D":
            Potion(Player)
            Current_Turn(Monster,Player,r,t+1,1)

def Skill(Player,Monster,ability):

    options=Skill_Text(Player)
    a=0

        # Array with the name options has the following 's' for strength followed by number
    while a not in (options,"back"):

        a=input(">...:")

        if a==options:
            if a[0]=="s":
                for i in range(len (options)):
                    if a==ability[i]:
                        Strength_Abilities(Player,Monster,2,1)[int(a[1])]



            if a[0]=="d":
                for i in range(len (options)):
                    if a==ability[i]:
                        Dexterity_Abilities(Player,Monster,2,1)[int(a[1])]


            if a[0]=="i":
                for i in range(len (options)):
                    if a==ability[i]:
                        Intelligence_Abilities(Player,Monster,2,1)[int(a[1])]


        if a=="back":
            Player_Menu(Player,Monster,ability)

def Player_Turn(Player,Monster,r,t):
    # 0 STR 1 DEX 2 INT --- NAME of ABILITY
    ability=can_cast_Player_Abilities(Player,Monster)
    Player_Menu(Player,Monster,ability,r,t)



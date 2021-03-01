from PlayerAbilities import *


def can_cast_Player_Abilities(Player,Monster):

    #Empty Array
    can_cast=[]

    #If Player has Energy to cast spell add name in can cast with index ( 0 Strength, 1 Dexterity, 2 Intelligence  )

    for i in range(len(Strength_Abilities(Player,Monster,1,0))):
        if Strength_Abilities(Player,Monster,1,0)[i][2] <=Player.show_En()[0] and Strength_Abilities(Player,Monster,1,0)[i][1]<=Player.show_Stats()[0] :
            can_cast.append([0,Strength_Abilities(Player,Monster,1,0)[i][0]])

    for i in range(len(Dexterity_Abilities(Player,Monster,1,0))):
        if Dexterity_Abilities(Player,Monster,1,0) [i][2] <=Player.show_En()[0] and Dexterity_Abilities(Player,Monster,1,0)[i][1]<=Player.show_Stats()[1]:
            can_cast.append([1,Strength_Abilities(Player,Monster,1,0)[i][0]])

    for i in range(len(Intelligence_Abilities(Player,Monster,1,0))):
        if Intelligence_Abilities(Player,Monster,1,0) [i][2] <=Player.show_En()[0] and Intelligence_Abilities(Player,Monster,1,0)[i][1]<=Player.show_Stats()[2]:
            can_cast.append([2,Strength_Abilities(Player,Monster,1,0)[i][0]])

    return can_cast




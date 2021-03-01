
import random





def Critical(Player):
    isCrit=0
    for i in range(Player.check_Buff_Size()):
        if Player.check_Buff(i,"CRIT")[0]== 1:
            Player.remove_Buff(i)
            isCrit=1
    if isCrit==0:
        Crit=random.randrange(1,10)+ Player.show_Stats()[1]
        if Crit >= 10:
            isCrit=1
    return isCrit


def Attack(Player,Monster):

    isCrit=Critical(Player)

    attack=random.randrange(1,6)+Player.show_Stats()[0]

    print(Player.Name +" Rolled with modifiers " +str(attack))

    if isCrit==1:
        print(Player.Name+" Rolled a CRITICAL")
        print(Player.Name +" Deals " +str(attack*2) + " Damage to "+ Monster.Name)
        Monster.Take_Damage(attack*2)

    elif isCrit==0:
        print(Player.Name +" Deals " +str(attack*2) + " Damage to "+ Monster.Name)
        Monster.Take_Damage(attack)



#Abilities Follow the rules [ (Name) , Ability Modifier(has learned) , Energy Req ]

#Get back to this
#def Skills(Player,Monster):


'''____________________________________________________________________________________________________'''

        # Abilities 0= NAME , 1 Level to Unlock , 2 Cost    N == 0 see available abilities - 1 go to ability   L ==  0 Ability Description 1 Cast Ability
def Strength_Abilities(Player,Monster,n,l):
        if n==1:
            Str_Abilities=[["Fast Heavy",1,1],["Heavy Hit",2,1],["100% Strength",4,Player.show_En()[0]]]
            return Str_Abilities
        if n==2:
            list=[Str_Fast_Heavy(Player,Monster,l),Str_Heavy_Hit(Player,Monster,l),Str_100_Strength(Player,Monster,l)]
            if l==0:
                return list

def Dexterity_Abilities(Player,Monster,n,l):
        if n==1:
            Dex_Abilities=[["Shinobi Run",1,1],["Find Weakspot",2,1],["Shadow Clone Strike",4,4]]
            return Dex_Abilities
        if n==2:
            list=[Dex_Shinobi_Run(Player,Monster,l),Dex_Find_Weakspot(Player,Monster,l),Dex_Shadow_Clone_Strike(Player,Monster,l)]
            if l==1:
                return list


def Intelligence_Abilities(Player,Monster,n,l):
        if n==1:
            Int_Abilities=[["Still Mind",0,0],["Enchanted Attack",1,1],["Energy Bomb",2,3],["Meteor Explosion",4,Player.show_En()[0]]]
        return Int_Abilities
        if n==2:
            list=[Int_Still_Mind(Player,Monster,l),Int_Enchanted_Attack(Player,Monster,l),Int_Energy_Bomb(Player,Monster,l),Int_Meteor_Explosion(Player,Monster,l)]
            if l==1:
                return list

'''
                                    STR Skills
______________________________________________________________________________________________________-'''

def Str_Fast_Heavy(Player,Monster,n):
    Name="Fast Heavy"
    Cost=1
    Description="Swing hard and fast and deal 1d6 + STR*2 damage"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= random.randrange(1,6)+ (Player.show_Stats()[0]*2)

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)

def Str_Heavy_Hit(Player,Mosnter,n):
    Name="Heavy Hit"
    Cost=2
    Description="Deal Str*4 damage to opponent"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= Player.show_Stats()[0]*4

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)

def Str_100_Strength(Player,Monster,n):
    Name="100% Strength"
    Cost=show_En()[0]
    Description="Use all of your Energy and Deal En*8 damage"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= Cost*8

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)


'''
                                    DEX Skills
________________________________________________________________________________________________________'''

def Dex_Shinobi_Run(Player,Monster,n):
    Name="Shinobi Run"
    Cost=1
    Description="Increase Speed for +1 for 3 Turns"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:
        check=0
        # 0 Timed : "Speed" Name : 3+1 Turns (because cleanup) : 1 Value
        Buff= [0,"Speed",4,1]

        Player.Cast_Spell(Cost)

        for i in range(Entity.check_Buff_Size()):

            # Check if there is a buff named Speed
            o=Entity.check_Buff(i,"Speed")
            #If Buff returns TRUE | 1 |
            if o[0]==1:
                #Get value from that buff
                if o[1]==1:
                    # IF the buff has value 1 add extra time to it
                    Player.add_Timer(i,4)
                    check=1

        if check==0:
            Player.add_Buff(Buff)

def Dex_Find_Weakspot(Player,Monster,n):
    Name="Weak Spot"
    Cost=2
    Description="Next attack is a guranteed critical (Double DMG)"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:
        check=0
        # 1 Static : "CRIT" Name : Infinite Turns (until action ) : 1 Value becuz wy not
        Buff= [1,"CRIT","",1]

        Player.Cast_Spell(Cost)

        for i in range(Entity.check_Buff_Size()):

            # Check if there is a buff named Speed
            o=Entity.check_Buff(i,"CRIT")
            #If Buff returns TRUE | 1 |
            if o[0]==1:
                Player.remove_Buff(i)
                Player.add_Buff(Buff)

        if check==0:
            Player.add_Buff(Buff)

def Dex_Shadow_Clone_Strike(Player,Monster,n):
    Name="Shadow Clone Strike"
    Cost=show_En()[0]
    Description="Use all energy Deal Energy*6 Damage"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= Player.show_Stats()[1]*6

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)

'''
                                    INT Skills
__________________________________________________________________________________________________________'''

def Int_Still_Mind(Player,Monster,n):
    Name="Meditate"
    Cost="None"
    Description="Regain 2 + [Int/2] Energy :: Next enemy attack is guranteed CRIT against you"

    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:
        Buff= [1,"CRIT","",1]
        Energy= 2+ int(Player.show_En()[0]/2)
        Monster.add_Buff(self,Buff)
        Regain_En(Energy)

def Int_Enchanted_Attack(Player,Monster,n):
    Name="Enchanted Attack"
    Cost=1
    Description="Imbue a weapon with magical energy and deal 1d6 + STR + Int damage"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= random.randrange(1,6)+ Player.show_Stats()[0] + Player.show_Stats()[2]

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)

def Int_Energy_Bomb(Player,Monster,n):
    Name="Energy Bomb"
    Cost=3
    Description="Charge part of your energy and unleash a spark of your power : Deal Int*8 Damage"


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= Player.show_Stats()[2] * 8

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)

def Int_Meteor_Explosion(Player,Monster,n):
    Name="Meteor Explosion"
    Cost=Player.show_En()[0]
    Description="Draw forth all your Energy and unleash MASSIVE DESTRUCTION : Deal En*10 "


    if n==0:
        skill_text=[]
        skill_text.append(Name,Cost,Description)
        return skill_text

    elif n==1:

        Damage= Player.show_En()[0] * 10

        Player.Cast_Spell(Cost)

        isCrit=Critical(Player)

        if isCrit==1:
            Monster.Take_Damage(Damage*2)

        elif isCrit==0:
            Monster.Take_Damage(Damage)





'''

s1.
s2.

d1.
d2.

e1. Meditate ( 0 Energy ) : Regain X Energy
e2.



b. Go back Player_Menu

'''

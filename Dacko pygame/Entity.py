class Entity():

    # Hp= [Current,Max] , En= [Current,Max] , Stats= [Str , Dex , Int ] ,
    # Buffs [Type [Type (0 Timed) (1 Static) , Name of Buff , Time , Value )]
    def __init__(self,Name,Hp,En,Stats,Buffs):
        self.Name=Name
        self.Hp=Hp
        self.En=En
        self.Stats=Stats
        self.Buffs=Buffs

    #Gets name
    def Name(self):
        return self.Name
    #Function that shows Stats

    def show_Stats(self):
        return self.Stats

    #Function that reduces Hp

    def Take_Damage(self,dmg):
        self.Hp[0]=self.Hp[0]-dmg

    #Function that reduces En

    def Cast_Spell(self,mana):
        self.En[0]=self.En[0]-mana

    #Function that shows Current and Max Hp

    def show_Hp(self):
        return self.Hp

    #Function that shows Current and Max En

    def show_En(self):
        return self.En

    def Regain_En(self,Energy):
        self.En[0]+Energy

    # \/ This is the BUFF list it shows everything about Buffs


    def show_Buff(self,i):
        return  self.Buffs[i]

    def check_Buff_Size(self):
        return len(self.Buffs)


    #Function that Checks a buff in the location | i |
    def check_Buff(self,i,buff):
            # IF a string exist
            if buff in self.Buffs[i][1]:
                # Return (0 False) or (1 True) and the value of the BUFF
                return [1,self.Buffs[3]]
        # If there is no buff then return [ Nothing, (0 False)
            return 0



    #Function that Adds a Buff
    def add_Buff(self,buff):
        self.Buffs.append(buff)

    #Extends timer of Buff
    def add_Timer(self,i,t):
        self.Buffs[i][2]=t

    #Function that removes a buff
    def remove_Buff(self,rbuff):
        self.Buffs.pop(rbuff)

    #Function that Checks and removes Timed Buffs ---- Buffs [Type(0 Timed) (1 Static) , Name , Time ]
    def check_TBuff(self):
        for i in range(len(self.Buffs)):
            if self.Buffs[i][0]==0:
                self.Buffs[i][2]=self.Buffs[i][2]-1
                if self.Buffs[i][2]==0:
                    self.Buffs[i].pop




'''
==============================================================================================
'''

#Entity ( Name, Hp [Current , Max] , En [Current , Max] , Stats [Str , Dex , Int])

#Player ( Potions [ Health Potion, Energy Potion ] , Exp [ Current , Max ]


class Player(Entity):
    def __init__(self,Name,Hp,En,Stats,Buffs,Potions,Coins,Lvl,Exp,Lvl_point):
        self.Name=Name
        self.Hp=Hp
        self.En=En
        self.Stats=Stats
        self.Buffs=Buffs
        self.Potions=Potions
        self.Coins=Coins
        self.Lvl=Lvl
        self.Exp=Exp
        self.Lvl_point=Lvl_point

    #Change Current Hp and En to Max after Sleep in Town

    def Sleep(self):
        self.Hp[0]=self.Hp[1]
        self.En[0]=self.En[1]

    #Change Stats in the Training Arena
    def Stat_Increase(self,new_stats,Hp_increase,En_increase):
        self.stats=new_stats
        self.Hp[1]=self.Hp[1]+Hp_increase
        self.En[1]=self.En[1]+En_increase
        self.Lvl_point=self.Lvl_point-1

    #Add a Potion after Purchase  1 = Healing Potion , 2= Energy Potion
    def Get_Potion(self,t):
        self.Coins=self.Coins-2
        if t==1:
            self.Potions[0]=self.Potions[0]+1
        elif t==2:
            self.Potions[1]=self.Potions[1]+1

    #For Future implentations I put this here
    def Check_Coins(self):
        return self.Coins


    #Add Money after Combat
    def Get_Coins(self,n):
        self.Coins=self.Coins+n

    #for the Town show menu
    def show_Lvl(self):
        Level=[self.Lvl,self.Lvl_point]
        return Level


    #Check for Level and add Exp after Combat
    def Get_Exp (self,n):
        #Add XP
        self.Exp[0]=self.Exp[0]+n
        #Check if Lvl Up
        if self.Exp[0] >= self.Exp[1]:
            #Lvl Up and add Lvl Point
            self.Lvl=self.Lvl+1
            self.Lvl_point=self.Lvl_point+1
            self.Exp[1]=self.Exp[1]+150
            # MBY make levels harder (great again) self.Exp[1]=self.Exp[1]+self.Lvl*75

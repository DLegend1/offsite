import os


def TextScreen():
    print('''
        ############################################
        ####Welcome to the Generic Title Screen#####
        ############################################
        #                                          #
        #            1. Play Game...               #
        #            2. Exit Game                  #
        #                                          #
        ############################################
        >  
        > 
        >'''
          )


def MainMenu(b):

    TextScreen()

    if b==1:
        print("        >Invalid Input please try again!!")

    print('''        >
        >
        >
        >''')

    a=input("        >...: ")

    if a=="1":
        a=1
    elif a=="2":
        quit()
    else:
        os.system('cls')
        MainMenu(1)

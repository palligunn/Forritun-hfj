import random
from random import randrange
#hópverkefni 2
#jóhann Chanse Sigurðsson og Páll Gunnar Svansson
svar = 0
while svar != 9:
    print ("1.Bílar")
    print ("2.Samlagning")
    print ("3.Skæri, blað, steinn")
    print ("4.Strengur")
    print ("5.Heiltölur")
    print ("6.Teningarspilið Craps")
    print ("7.Teningakast")
    print ("8.Byggingaupplýsingar úr hópverkefni 1")
    print ("9.Hætta")
    print (" ")
    svar = int(input("sláðu inn tölu"))
        #liður 1 - Bílar
    if svar == 1:
        print("=-1-=")
        bilamenn = int(input("Sláðu inn fjölda farþega : "))
        print(bilamenn,"eru skráð.")
        if bilamenn < 5:
            print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.") 
        else:
            biltalning = bilamenn
            
            bilkall = 0
            bilar = 0
            bilsidast = 0
            for set in range(1,biltalning+1):
                bilkall = bilkall + 1
                if bilkall == 5:
                    bilkall = 0
                    bilar = bilar + 1
                    bilamenn = bilamenn - 5
                if bilamenn < 5 and bilsidast == 0: #sidasti billin
                    if bilamenn == 4:
                        bilar = bilar + 1
                        bilsidast = 4
                    if bilamenn == 3:
                        bilar = bilar + 1
                        bilsidast = 3
                    if bilamenn == 2:
                        bilar = bilar + 1
                        bilsidast = 2
                    if bilamenn == 1:
                        bilsidast = 1
                        bilar = bilar + 1
        print("Fjöldi bíla sem þarf:",bilar)
        print("Fjöldi í síðasta bílnum:",bilsidast)
        print("=-1-=")

        #liður 2 - Samlagning
    if svar == 2:
        print("=-2-=")
        samem = 0
        samlagntala = int(input("Sláðu inn tölu : "))
        #if samlagntala < :
         #   for msam in range(samlagntala,0,-1): #minus lagning
          #      print(msam)
           #     print("yay") #(╯°□°）╯︵ ┻━┻
                

        if samlagntala > 0:
            for psam in range(1,samlagntala+1): #plus lagning
                print(psam)
                samem = samem + psam
       
        elif samlagntala == 0:
            print("Takk fyrir að nota forritið okkar") #núll
        else:
            for msam in range(samlagntala,0): #minus lagning
                print(msam)
                samem = samem + msam
            
        print("===")
        print(samem)
        print("===")
        print("=-2-=")

        #liður 3 - Skæri, blað, steinn
    if svar == 3:                #laga þetta seinna #og ég lega það núna
        print("=-3-=")
        gameturns = 0
        pmove = 0
        pwin = 0
        cpuwin = 0
        gamedraw = 0
        while pmove != 4:
            print("/1. Skæri 2. Blað 3. Steinn 4. Hætta/")
            pmove = int(input("Veldu 1, 2, 3 eða 4: "))
            if pmove != 4:
                cpumove = randrange(1,4) #forritið velur sitt eigið numer
                gameturns = gameturns +1
                if pmove == cpumove:
                    print("Jafntefli.")
                    gamedraw = gamedraw + 1
                elif pmove == 3 and cpumove == 1 or pmove == 2 and cpumove == 3 or pmove == 1 and cpumove == 2:
                    print("Notandi vann!")
                    pwin = pwin + 1
                else:
                    print("Notandi tapar.")
                    cpuwin = cpuwin + 1
                print("Notandi valdi",pmove,"á móti",cpumove)
                print("-----")
        print("Sigur =",pwin,"Töp =",cpuwin,"Jafntefli =",gamedraw,"Lengd leiks :",gameturns)
        print("=-3-=")
        #liður 4 - Strengur
    if svar == 4:
        texti = input("Sláðu inn Texta: ")
        texti = texti.replace('á','*')
        texti = texti.replace('Á','*')
        texti = texti.replace('b','*')
        texti = texti.replace('B','*')
        texti = texti.replace('c','*')
        texti = texti.replace('C','*')
        texti = texti.replace('d','*')
        texti = texti.replace('D','*')
        texti = texti.replace('ð','*')
        texti = texti.replace('Ð','*')
        texti = texti.replace('e','*')
        texti = texti.replace('E','*')
        texti = texti.replace('é','*')
        texti = texti.replace('É','*')
        texti = texti.replace('f','*')
        texti = texti.replace('F','*')
        texti = texti.replace('g','*')
        texti = texti.replace('G','*')
        texti = texti.replace('h','*')
        texti = texti.replace('H','*')
        texti = texti.replace('i','*')
        texti = texti.replace('I','*')
        texti = texti.replace('í','*')
        texti = texti.replace('Í','*')
        texti = texti.replace('j','*')
        texti = texti.replace('J','*')
        texti = texti.replace('k','*')
        texti = texti.replace('K','*')
        texti = texti.replace('l','*')
        texti = texti.replace('L','*')
        texti = texti.replace('m','*')
        texti = texti.replace('M','*')
        texti = texti.replace('o','*')
        texti = texti.replace('O','*')
        texti = texti.replace('ó','*')
        texti = texti.replace('Ó','*')
        texti = texti.replace('p','*')
        texti = texti.replace('P','*')
        texti = texti.replace('q','*')
        texti = texti.replace('Q','*')
        texti = texti.replace('r','*')
        texti = texti.replace('R','*')
        texti = texti.replace('t','*')
        texti = texti.replace('T','*')
        texti = texti.replace('u','*')
        texti = texti.replace('U','*')
        texti = texti.replace('ú','*')
        texti = texti.replace('Ú','*')
        texti = texti.replace('v','*')
        texti = texti.replace('V','*')
        texti = texti.replace('x','*')
        texti = texti.replace('X','*')
        texti = texti.replace('y','*')
        texti = texti.replace('Y','*')
        texti = texti.replace('ý','*')
        texti = texti.replace('Ý','*')
        texti = texti.replace('z','*')
        texti = texti.replace('Z','*')
        texti = texti.replace('þ','*')
        texti = texti.replace('Þ','*')
        texti = texti.replace('æ','*')
        texti = texti.replace('Æ','*')
        texti = texti.replace('ö','*')
        texti = texti.replace('Ö','*')
        print(texti)

        #liður 5 - Heiltölur
    if svar == 5:
        tala_1 = []
        tala_2 = []
        tala_3 = []
        tala_4 = []
        tala_5 = []
        tala_6 = []
        tala_7 = []
        for i in range(1):
            tala_1 = (randrange(1,101))
        for i in range(1):
            tala_2 = (randrange(1,101))
        for i in range(1):
            tala_3 = (randrange(1,101))
        for i in range(1):
            tala_4 = (randrange(1,101))
        for i in range(1):
            tala_5 = (randrange(1,101))
        for i in range(1):
            tala_6 = (randrange(1,101))
        for i in range(1):
            tala_7 = (randrange(1,101))    
        print (("tölurnar sem þú fékkst eru: "), tala_1, tala_2, tala_3, tala_4, tala_5, tala_6, tala_7)
        print ("stærðsta talan er : ",(max(tala_1, tala_2, tala_3, tala_4, tala_5, tala_6, tala_7)))
        print ("minnsta talan er: ", (min(tala_1, tala_2, tala_3, tala_4, tala_5, tala_6, tala_7)))
        meðaltal =(int(tala_1 + tala_2 + tala_3 + tala_4 + tala_5 + tala_6 + tala_7/7))
        print ("meðaltalið á tölunum er: ", meðaltal)
        print (" ")

    if svar == 9:
        quit()



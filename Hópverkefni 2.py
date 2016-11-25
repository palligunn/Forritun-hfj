#hópverkefni 2
#jóhann Chanse Sigurðsson og Páll Gunnar Svansson
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

        #liður 1 - Bílar
    if svar = 1:
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
    if svar = 2:
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
    if svar = 3:                #laga þetta seinna
        listi = ["blað", "skæri", "steinn"]
        tölva = listi[randint(0,2)]
        notandi = False
        while notandi == False:
            notandi = input("skæri, blað, steinn? [skrifaðu orðinn eins og stendur hér] ")
        if notandi == tölva:
            print ("jafntefli")
        elif notandi == "steinn":
            if tölva == "blað":
                print ("Þú tapaðir")
            else:
                print ("Þú vannst")
        elif notandi == "blað":
            if tölva == "skæri":
                print ("þú tapaðir")
                else:
                    print ("Þú vannst")
        elif notandi == "skæri":
            if tölva == "steinn":
                print ("þú tapaðir")
            else:
                print ("þú vannst")
        else:
            print ("þú skrifaðir ekki rétt")
        notandi = False
        tölva = listi[randint(0,2)]
        #liður 4 - Strengur
    if svar = 4:
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
    if svar = 5:

        #liður 6 - Teningaspilið Craps
    if svar = 6:

        #liður 7 - Teningakast
    if svar = 7:

        #liður 8 - Byggingaupplýsingar úr hópverkefni 1
    if svar = 8:

    if svar = 9:
        quit()

    

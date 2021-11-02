from ChemClass import Reaction
import time
element = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn"]
molarmass = [1.01,4.00,6.49,9.01,10.81,12.01,14.01,16.00,19.00,20.18,22.99,24.31,26.98,28.09,30.98,32.07,35.45,39.95,39.10,40.08,44.96,47.87,50.94,52.00,54.94,55.85,58.93,58.69,63.55,65.38,69.72,72.64,74.92,78.96,79.90,83.80,85.47,87.62,88.91,91.22,92.91,95.96,98.00,101.07,102.91,106.42,107.87,112.44,114.82,118.71]
def convertMolG():                      #Starting the Function
    global element;
    global molarmass;
    print ("")
    convProp = "";                      #Setting convProp to ask which conversion property it is using.
    while convProp.lower() != "grams" and convProp.lower() != "gram" and convProp.lower() != "mole" and convProp.lower() != "moles" and convProp.lower() != "mol" and convProp.lower() != "mols":
        whatConv = raw_input("What are you starting with, grams and moles? ")
        #convProp = whatConv;
        if whatConv.lower() == "grams" or whatConv.lower() == "gram" or whatConv.lower() == "mole" or whatConv.lower() == "moles" or whatConv.lower() == "mol" or whatConv.lower() == "mols":
            #print("Good answer")
            convProp = whatConv.lower();
        else:
            print("That was an invalid option")
    AElement = "";
    while AElement not in element:              #Making sure user put in a correct element
        IElement = raw_input("What element are you using(Symbol)? ")
        AElement= IElement[:1].upper() + IElement[1:2].lower()
        if AElement not in element:
            print("That is not one of the first 50 elements or it is not an element.")
    #GramsOrMols = input("How much "+str(AElement)+" do you have? ");        #Asking to the grams or moles
    if convProp[0:1].lower() == "g":
        GramsOrMols = input("How many grams of "+str(AElement)+" do you have? ");
        print(str(GramsOrMols)+"grams of "+str(AElement)+" is "+str(GramsOrMols/float(molarmass[element.index(AElement)]))+" moles.")
    elif convProp[0:1].lower() == "m":
        GramsOrMols = input("How many moles of "+str(AElement)+" do you have? ");
        print(str(GramsOrMols)+"moles of "+str(AElement)+" is "+str(float(molarmass[element.index(AElement)])*GramsOrMols)+" grams.")
    print("")
    runChem();
    
def Stoichiometry():
    global element;
    global molarmass;
    print("Starting Stoic")
    checkTR = False;
    while checkTR == False:
        TReaction = raw_input("What type of reaction is this? "
        "Sythesis/Double Replacement/Single Replacement? ")
        if TReaction.lower() == "synthesis" or TReaction.lower() == "double replacement" or TReaction.lower() == "single replacement" or TReaction.lower() == "syn" or TReaction.lower() == "dr" or TReaction.lower() == "sr": 
            checkTR = True;
        else:
            print("That was an invalid option");
    if TReaction.lower() == "synthesis" or TReaction.lower() == "syn":
        STsynGood = False;
        while STsynGood == False:
            synEle1 = raw_input("What is element 1? ");
            SynAEle1 = synEle1[:1].upper() + synEle1[1:2].lower()
            synEle2 = raw_input("What is element 2? ");
            SynAEle2 = synEle2[:1].upper() + synEle2[1:2].lower()
            if SynAEle1 in element and SynAEle2 in element:
                STsynGood = True;
            else:
                print("One of the elements was incorrect")
        #Asking for grams and making it into moles.
        synEle1G = raw_input("What is the mass of element 1? ")
        synEle2G = raw_input("What is the mass of element 2? ")
        synEle1M = float(synEle1G)/float(molarmass[element.index(SynAEle1)]);
        synEle2M = float(synEle2G)/float(molarmass[element.index(SynAEle2)]);
        #Possible area for special ratio in balanced formula
        
        #Start of BCA tables!!!!
        if synEle1M > synEle2M:
            print("    "+str(SynAEle1)+" + "+str(SynAEle2)+" --> "+str(SynAEle1+SynAEle2))
            print("B:  "+str(synEle1M)+"   "+str(synEle2M)+" --> 0")
            print("C: "+str(chr(45))+str(synEle2M)+"  "+str(chr(45))+str(synEle2M)+" --> +"+str(synEle2M))
            print("A:  "+str(synEle1M-synEle2M)+"   "+str(int(0))+"   --> "+str(synEle2M))
            print(str(SynAEle2)+" is the limiting reactant")
            lr=SynAEle2
        if synEle2M > synEle1M:
            print("    "+str(SynAEle1)+"   "+str(SynAEle2)+" --> "+str(SynAEle1+SynAEle2))
            print("B:  "+str(synEle1M)+"   "+str(synEle2M)+" --> 0")
            print("C: "+str(chr(45))+str(synEle1M)+"  "+str(chr(45))+str(synEle1M)+" --> +"+str(synEle2M))
            print("A:  "+str(int(0))+"     "+str(float(synEle2M)-float(synEle1M))+" --> "+str(synEle2M))
            print(str(SynAEle1)+" is the limiting reactant")
            lr=SynAEle1
        elif synEle2M == synEle1M:
            print("    "+str(SynAEle1)+"   "+str(SynAEle2)+" --> "+str(SynAEle1+SynAEle2))
            print("B:  "+str(synEle1M)+"   "+str(synEle2M)+" --> 0")
            print("C: "+str(chr(45))+str(synEle2M)+"  "+str(chr(45))+str(synEle2M)+" --> +"+str(synEle2M))
            print("A:  "+str(int(0))+"     "+str(int(0))+"   --> "+str(synEle2M))
            print("There is no limiting reactant")
            lr=" neither reactant"
        SynClass=Reaction()
        SynClass.new_Syninput("Where "+str(synEle1M)+"moles of "+str(SynAEle1)+" and "+str(synEle2M)+"moles of "+str(SynAEle2)+", the limiting reactant is "+str(lr))
        time.sleep(5)
        runChem();
    elif TReaction.lower() == "double replacement" or TReaction.lower() == "dr":
        DRGood=0;
        while DRGood!=2:
            DRGood=0;
            #Start of the Double Reaction Compound 1
            DRCompound1=raw_input("What is the first compound? ")
            #Checking a 2 length compound
            if len(DRCompound1) == 2:
                DRE1=DRCompound1[0:1].upper()
                DRE2=DRCompound1[1:2].upper()
                if DRE1 in element and DRE2 in element:
                    DRGood+=1;
            #Checking if the elements are real if there is a length of 3
            if len(DRCompound1) == 3:
                DRE1=DRCompound1[0:1].upper()+DRCompound1[1:2].lower()
                DRE2=DRCompound1[2:3].upper()
                if DRE1 in element and DRE2 in element:
                    DRGood+=1;
                else:    
                    DRE1=DRCompound1[0:1].upper();
                    DRE2=DRCompound1[1:2].upper()+DRCompound1[2:3].lower()
                    if DRE1 in element and DRE2 in element:
                        DRGood+=1;
                    else:
                        print("Those elements are not real.")
            #Finding if the elements are real in a 4 length string
            if len(DRCompound1) == 4:
                DRE1=DRCompound1[0:1].upper()+DRCompound1[1:2].lower()
                DRE2=DRCompound1[2:3].upper()+DRCompound1[3:4].lower()
                if DRE1 in element and DRE2 in element:
                    DRGood+=1;
            #Start of Double Reaction Compound 2
            DRCompound2=raw_input("What is the second compound? ")
            #Checking a 2 length compound
            if len(DRCompound2) == 2:
                DRE3=DRCompound2[0:1].upper()
                DRE4=DRCompound2[1:2].upper()
                if DRE3 in element and DRE4 in element:
                    DRGood+=1;
            #Checking if the elements are real if there is a length of 3
            if len(DRCompound2) == 3:
                DRE3=DRCompound2[0:1].upper()+DRCompound2[1:2].lower()
                DRE4=DRCompound2[2:3].upper()
                if DRE3 in element and DRE4 in element:
                    DRGood+=1;
                else:    
                    DRE3=DRCompound2[0:1].upper();
                    DRE4=DRCompound2[1:2].upper()+DRCompound2[2:3].lower()
                    if DRE3 in element and DRE4 in element:
                        DRGood+=1;
                    else:
                        print("Those elements are not real.")
            #Finding if the elements are real in a 4 length string
            if len(DRCompound2) == 4:
                DRE3=DRCompound2[0:1].upper()+DRCompound2[1:2].lower()
                DRE4=DRCompound2[2:3].upper()+DRCompound2[3:4].lower()
                if DRE3 in element and DRE4 in element:
                    DRGood+=1;
                    
        #Asking the user for the masses
        DRC1G=input("What is the mass of the first compound? ")
        DRC2G=input("What is the mass of the second compound? ")
        DRC1M=DRC1G/(float(molarmass[element.index(DRE1)])+(float(molarmass[element.index(DRE2)])))
        DRC2M=DRC2G/(float(molarmass[element.index(DRE2)])+(float(molarmass[element.index(DRE3)])))
        #BCA Tables print
        if DRC1M > DRC2M:
            print("    "+str(DRE1+DRE2)+" + "+str(DRE3+DRE4)+" --> "+str(DRE1+DRE3)+"   "+str(DRE2+DRE4))
            print("B:  "+str(DRC1M)+"   "+str(DRC2M)+" --> 0         0")
            print("C: "+str(chr(45))+str(DRC2M)+"  "+str(chr(45))+str(DRC2M)+" --> +"+str(DRC2M)+"     +"+str(DRC2M))
            print("A:  "+str(DRC1M-DRC2M)+"   "+str(int(0))+"   --> "+str(DRC2M)+"      "+str(DRC2M))
            print(str(DRE3+DRE4)+" is the limiting reactant")
            lr=DRE3+DRE4
        if DRC2M > DRC1M:
            print("    "+str(DRE1+DRE2)+" + "+str(DRE3+DRE4)+" --> "+str(DRE1+DRE3)+"   "+str(DRE2+DRE4))
            print("B:  "+str(DRC1M)+"   "+str(DRC2M)+" --> 0         0")
            print("C: "+str(chr(45))+str(DRC1M)+"  "+str(chr(45))+str(DRC1M)+" --> +"+str(DRC2M)+"    +"+str(DRC2M))
            print("A:  "+str(int(0))+"     "+str(float(DRC2M)-float(DRC1M))+" --> "+str(DRC2M)+"    "+str(DRC2M))
            print(str(DRE1+DRE2)+" is the limiting reactant")
            lr=DRE1+DRE2
        elif DRC2M == DRC1M:
            print("    "+str(DRE1+DRE2)+" + "+str(DRE3+DRE4)+" --> "+str(DRE1+DRE3)+"   "+str(DRE2+DRE4))
            print("B:  "+str(DRC1M)+"   "+str(DRC2M)+" --> 0         0")
            print("C: "+str(chr(45))+str(DRC2M)+"  "+str(chr(45))+str(DRC2M)+" --> +"+str(DRC2M)+"    +"+str(DRC2M))
            print("A:  "+str(int(0))+"     "+str(int(0))+"   --> "+str(DRC2M)+"     "+str(DRC2M))
            print("There is no limiting reactant")
            lr=" neither"
        DRClass=Reaction()
        DRClass.new_DRinput("Where "+str(DRC1M)+"moles of "+str(DRCompound1)+" and "+str(DRC2M)+"moles of "+str(DRCompound2)+", the limiting reactant is "+str(lr))
        time.sleep(10)
        runChem();
    elif TReaction.lower() == "single replacement" or TReaction.lower() == "sr":
        print("")
        SRV = 0;
        while SRV !=2:          #Starts to loop to get the elements and compound elements in the reaction
            SRV = 0;
            RCompound = raw_input("What is the compound? ")
            REle = raw_input("What is the single element? ")
            RAEle = REle[0:1].upper()+REle[1:2].lower()
            #Checks for single element as an element
            if RAEle in element:
                SRV+=1;
                #Checks if compound is 2, 1 letter elements
                if len(RCompound)==2:
                    if RCompound[0:1].upper() in element:
                        SRCEle1=RCompound[0:1].upper()
                        if RCompound[-1:].upper() in element:
                            SRCEle2=RCompound[1:2].upper()
                            SRV+=1;
                        else:
                            print("Wrong Second Element")
                    else:
                        print("Wrong First Element")
                #checks if compound is a 1 letter and 2 letter or the other way around
                elif len(RCompound)==3:
                    if RCompound[0:1].upper() in element:
                        SRCEle1=RCompound[0:1].upper()
                        SCREle2=RCompound[1:2].upper()+RCompound[2:3].lower()
                        SRV+=1;
                    elif RCompound[-1:].upper() in element:
                        SRCEle1=RCompound[0:len(RCompound)].upper()+RCompound[2:3].lower()
                        SCREle2=RCompound[-1:].upper()
                        SRV+=1;
                    else:
                        print("Invalid compund")
                #Checks compound for the 2 elements
                elif len(RCompound)==4:
                    SRCEle1=RCompound[0:1].upper()+RCompound[1:2].lower()
                    SRCEle2=RCompound[2:3].upper()+RCompound[3:4].lower()
                    if SRCEle1 in element and SRCEle2 in element:
                        SRV+=1
                        print("")
                    else:
                        print("Invalid compound")
            else:
                print("Those were not valid elements")
                print("")
        #End of while
        SREle1G=input("What was the mass of "+str(RAEle)+"? ")                  #Single Replacement Element 1 Grams
        SRCG=input("What was the mass of "+str(SRCEle1+SRCEle2)+"? ")           #Single Replacement Compound Grams
        SREle1M=float(SREle1G)/float(molarmass[element.index(RAEle)])                      #Single Replacement Element 1 moles
        SRCM=float(SRCG)/float(molarmass[element.index(SRCEle1)]+molarmass[element.index(SRCEle2)]) #Single Replacement Compound Moles
        #BCA Start for Single Replacement reactions
        if SREle1M > SRCM:
            print("    "+str(RAEle)+" + "+str(SRCEle1+SRCEle2)+" --> "+str(RAEle+SRCEle2)+"   "+str(SRCEle1))
            print("B:  "+str(SREle1M)+"   "+str(SRCM)+" --> 0")
            print("C: "+str(chr(45))+str(SRCM)+"  "+str(chr(45))+str(SRCM)+" --> +"+str(SRCM)+"     +"+str(SRCM))
            print("A:  "+str(SREle1M-SRCM)+"   "+str(int(0))+"   --> "+str(SRCM)+"      "+str(SRCM))
            print(str(SRCEle1+SRCEle2)+" is the limiting reactant")
            lr=SRCEle1+SRCEle2
        if SRCM > SREle1M:
            print("    "+str(RAEle)+"   "+str(SRCEle1+SRCEle2)+" --> "+str(RAEle+SRCEle2)+"   "+str(SRCEle1))
            print("B:  "+str(SREle1M)+"   "+str(SRCM)+" --> 0")
            print("C: "+str(chr(45))+str(SREle1M)+"  "+str(chr(45))+str(SREle1M)+" --> +"+str(SRCM)+"    +"+str(SRCM))
            print("A:  "+str(int(0))+"     "+str(float(SRCM)-float(SREle1M))+" --> "+str(SRCM)+"    "+str(SRCM))
            print(str(RAEle)+" is the limiting reactant")
            lr=RAEle
        elif SRCM == SREle1M:
            print("    "+str(RAEle)+"   "+str(SRCEle1+SRCEle2)+" --> "+str(RAEle+SRCEle2)+"   "+str(SRCEle1))
            print("B:  "+str(SREle1M)+"   "+str(SRCM)+" --> 0     0")
            print("C: "+str(chr(45))+str(SRCM)+"  "+str(chr(45))+str(SRCM)+" --> +"+str(SRCM)+"    +"+str(SRCM))
            print("A:  "+str(int(0))+"     "+str(int(0))+"   --> "+str(SRCM)+"     "+str(SRCM))
            print("There is no limiting reactant")
            lr=" neither"
        SRClass=Reaction()
        SRClass.new_SRinput("Where "+str(SREle1M)+"moles of "+str(RAEle)+" and "+str(SRCM)+"moles of "+str(SRCEle1+SRCEle2)+", the limiting reactant is "+str(lr))
        time.sleep(10)
        runChem();
def runChem(): 
    #Asking what the user wants to start
    response = raw_input("Would you like to do Stoichiometry(Stoic), Conversions(Conv)?, or Answers ")
    if response.lower() == "stoic":
        Stoichiometry();
    elif response.lower() == "conv":
        convertMolG();
    elif response.lower() == "answers" or response.lower() == "ans":
        print("")
        answer=Reaction()
        print answer.get_reaction();
        #get_reaction(rxnList)
        print("")
        runChem();
runChem();





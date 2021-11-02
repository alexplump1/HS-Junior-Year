import random
import time
OHplayerHand = []
OHBot1H = [];
OHBot2H = [];
OHBot3H = [];
OHBot4H = [];
OHBot5H = [];
OHBot6H = [];
OHBot7H = [];
OHPlayedCards=[]
OHScore = [0,0,0,0,0,0,0,0];
OHGuesses = [0,0,0,0,0,0,0,0];
def OHell():
    global OHplayerHand;
    global OHBot1H;
    global OHBot2H;
    global OHBot3H;
    global OHBot4H;
    global OHBot5H;
    global OHBot6H;
    global OHBot7H;
    global OHPlayedCards;
    global OHScore;
    global OHGuesses;
    global OHDeck;
    print("")
    print("Oh Hell has been started")
    OHinstructions = raw_input("Would you like to know the rules of Oh Hell? ")
    if OHinstructions.lower() == "yes":
        print("")
        print("To play Oh Hell, each round, there is a random card thrown down that determines the trump, meaning suit with most power."
        " If you have a trump card, you must play it when it is your turn."
        " If you do not have any trump cards, then you can play any other card in your hand."
        " To win a turn in a round, you must have the highest trump, or highest face value card if no one else plays a trump, to gain points."
        #print("If the two highest cards are the same, then they cancel out.(Only if there are so many players there needs to be multiple decks)")
        " The trick of this game is that each player must say how many turns they think they will win."
        " But if you don't win as many, or more rounds than you said you will get as many points as you did rounds."
        " If you say a number, and you win that many rounds, then you get that many points +10."
        " At the start of the game, you will start with one card, and every round after that everyone will get one more card than the previous round."
        " Once there are not enough cards to give everyone, the amount of cards recieved will start decreasing.")
        OHInstDone = raw_input("Type done when you are done reading. ")
    conNumOfBots = False;
    makeTwoDecks=False;
    print("")
    while conNumOfBots == False:                                                #Continue Number of bots, checks to see if it need to make 1 or 2 decks
        numberOfBots = input("How many bots would you like to play against?(2-7) ")
        if numberOfBots >= 2 and numberOfBots <= 7 and type(numberOfBots) == int:
            conNumOfBots = True;
            if numberOfBots > 6:
                makeTwoDecks=True;
                
        else:
            print("That was not a correct input")
    OHMakeBots = 0;
    OHListBotPlayer = ["P1"];
    while OHMakeBots != numberOfBots:                                           #Making bots
        OHMakeBots+=1;
        OHListBotPlayer.append("B" + str(int(OHMakeBots)))
    #print(OHListBotPlayer)                                                     #Printing the list of players and bots
    OHCardsToGiveOut = OHDeck;
    OHMaxReached = False;
    NumCToGiveOut = -1;
    cardStarter=-1;                                                             #Making the game not end
    while NumCToGiveOut != 0:                                                   #Start of the Oh Hell Loop
        OHDeck=[]
        OHMakeDeck();
        if makeTwoDecks==True:
            OHMakeDeck();
        cardStarter+=1;                                                         #Checks who starts guessing and throwing down cards
        if cardStarter>len(OHListBotPlayer):
            cardStarter-=len(OHListBotPlayer);
        if NumCToGiveOut==-1:
            NumCToGiveOut +=1;
        OHMaxReached = False;
        if OHMaxReached==False:                                                 #Going up in cards
            NumCToGiveOut +=1;
        elif OHMaxReached == True:                                              #Going down in cards
            NumCToGiveOut -= 1;
        if len(OHDeck)/(NumCToGiveOut*numberOfBots)>numberOfBots:               #Checking to see if max cards has been reached
            OHMaxReached = True;
        finishLoop=False
        OHplayerHand=[]
        #Loop of give cards to the bots and player
        while int(len(OHplayerHand))!=NumCToGiveOut and finishLoop==False:      #Giving players their cards
            giveCard=random.randint(0,len(OHDeck)-1)
            OHplayerHand.append(OHDeck[giveCard])
            del(OHDeck[giveCard])
            OHGTB=int(len(OHListBotPlayer)-1)                                   #Give to Bots, give 1 card to each bot
            #"""
            if len(OHDeck)==0:
                print("The deck is empty for some reason and no one gets a card")
                OHGTB=0
                finishLoop=True;
            #"""    
            if OHGTB!=0:
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot1H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot2H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot3H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot4H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot5H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot6H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
            if OHGTB!=0:                                                        #If there is a bot 2, give it a card
                OHGTB-=1;
                giveCard=random.randint(0,len(OHDeck)-1)
                OHBot7H.append(OHDeck[giveCard])
                del(OHDeck[giveCard])
        print("Your hand is: " + str(OHplayerHand))                             #Printing Player's hand
        OHTopCard="undetermined"
        if len(OHDeck)>=1:                                                      #Players should have their cards by now, makes a top card
            OHTopCard=OHDeck[random.randint(0,len(OHDeck)-1)]
        else:
            print("Since there are no cards left in the pile, a random one is choosen")
            OHMakeDeck()
            OHTopCard=OHDeck[random.randint(0,len(OHDeck)-1)]
            OHDeck=[]
        if OHTopCard[0:2]=="he":                                                #Making a Trump Suit
            trumpSuit="heart"
        if OHTopCard[0:2]=="sp":
            trumpSuit="spade"
        if OHTopCard[0:2]=="cl":
            trumpSuit="club"
        if OHTopCard[0:2]=="di":
            trumpSuit="diamond"
        print("The trump suit is "+str(trumpSuit)+"s")
        OHPersonToAsk=cardStarter;                                              #Starts the guessing process
        p1Guess=-1;
        OHPersonToAsk+=1
        guessStarter=True;
        while OHPersonToAsk!=cardStarter:                                       #Just once, checks everyone's hand
            if guessStarter==True:
                guessStarter=False;
                OHPersonToAsk-=1;
            if OHPersonToAsk==0:                                                #Starts the guessing for the user
                while p1Guess>NumCToGiveOut or p1Guess<0 or type(p1Guess)!=int:
                    p1Guess=input("How many rounds do you think you will win? ")
                    if p1Guess>NumCToGiveOut or p1Guess<0 or type(p1Guess)!=int:
                        print("You must pick a number between 0 and the number of cards in your hand")
                        print("")
            OHGuesses[0]=p1Guess;
            #Checks bot's hands
            if OHPersonToAsk==1:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot1H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[1]=0;
                elif numOfTrumps==1:
                    OHGuesses[1]=0;
                elif numOfTrumps>1:
                    OHGuesses[1]=int(numOfTrumps)-1;
            if OHPersonToAsk==2:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot2H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[2]=0;
                elif numOfTrumps==1:
                    OHGuesses[2]=0;
                elif numOfTrumps>1:
                    OHGuesses[2]=int(numOfTrumps)-1;
            if OHPersonToAsk==3:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot3H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[3]=0;
                elif numOfTrumps==1:
                    OHGuesses[3]=0;
                elif numOfTrumps>1:
                    OHGuesses[3]=int(numOfTrumps)-1;
            if OHPersonToAsk==4:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot4H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[4]=0;
                elif numOfTrumps==1:
                    OHGuesses[4]=0;
                elif numOfTrumps>1:
                    OHGuesses[4]=int(numOfTrumps)-1;
            if OHPersonToAsk==5:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot5H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[5]=0;
                elif numOfTrumps==1:
                    OHGuesses[5]=0;
                elif numOfTrumps>1:
                    OHGuesses[5]=int(numOfTrumps)-1;
            if OHPersonToAsk==6:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot6H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[6]=0;
                elif numOfTrumps==1:
                    OHGuesses[6]=0;
                elif numOfTrumps>1:
                    OHGuesses[6]=int(numOfTrumps)-1;
            if OHPersonToAsk==7:                                                #Checking Bot 1's hand for trumps to make a guess
                numOfTrumps=0;
                for i in OHBot7H:
                    if trumpSuit in i:
                        numOfTrumps+=1;
                if numOfTrumps==0:
                    OHGuesses[7]=0;
                elif numOfTrumps==1:
                    OHGuesses[7]=0;
                elif numOfTrumps>1:
                    OHGuesses[7]=int(numOfTrumps)-1;
            
            OHPersonToAsk=OHPersonToAsk+1;
            if OHPersonToAsk>=len(OHListBotPlayer)+1:
                OHPersonToAsk-=len(OHListBotPlayer)+1;
        #print OHGuesses                                                        #Printing everyone's guess
        OHTurnStarter=True
        OHStarterCard=""
        OHPlayerToGo=cardStarter;
        priorityCard="";
        while len(OHplayerHand)!=0:                                             #Starts the round
            if OHPlayerToGo==0:
                playerCardAcceptable=False;
                if OHTurnStarter==False:
                    while playerCardAcceptable==False:
                        playerplayCard=raw_input("You are the first player, what card would you like to play? ")
                        if playerplayCard.lower() in OHplayerHand:              #Checks if the card was in their hand
                            playerCardAcceptable=True;
                            priorityCard=playerplayCard.lower()
                        else:
                            print("That was not a card, or was not in your hand")
                elif OHTurnStarter==False:                                      #Players turn if they were not the first one to start
                    anyCardPlayable=False;
                    for i in OHplayerHand:                                      #Checks if the priority suit is even in their hand
                        if i[0:2].lower()==priorityCard[0:2]:
                            anyCardPlayable=False;
                    while playerCardAcceptable==False:
                        playerplayCard=raw_input("The top card is "+str(priorityCard)+". What card would you like to play? ")
                        if playerplayCard.lower() in OHplayerHand:              #Checks if the card was in their hand
                            if anyCardPlayable==True:                           #If the player can even play a priority suit
                                if playerplayCard[0:2].lower()==priorityCard[0:2]:
                                    playerCardAcceptable=True;
                                    OHPlayedCards[0]=playerplayCard[0:2].lower()
                                else:
                                    print("That card was in your hand, but it is not the same suit as the top card")
                            elif anyCardPlayable==False:                        #If the player cannot play a priority suit        
                                playerCardAcceptable=True;
                                OHPlayedCards[0]=playerplayCard[0:2].lower()
                        else:
                            print("That was not a card, or was not in your hand")
            """
            if OHPlayerToGo==1:                                                 #Bot 1's turn
                for i in OHBot1H:
                    
            """
OHSuits=["heart","spade","club","diamond"]
OHCards= [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
OHDeck = []
def OHMakeDeck():
    global OHSuits;
    global OHCards;
    global OHDeck;
    OHS = 0;            #Oh Hell suits
    OHC = 0;            #Oh Hell cards
    while OHS <= 3:
        while OHC <= 12:
            OHDeck.append(str(OHSuits[OHS])+str(OHCards[OHC]))
            OHC +=1;
        OHC = 0;
        OHS +=1;
    #print("done making a whole deck")
OHell()

#print(OHDeck)
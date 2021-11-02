import random
import time
from TicTacToeScore import Score
Player1Name = ""
Player2Name = ""
Player1Score = 0
Player2Score = 0
EndScore = 5;
def war():
    global Player1Name
    global Player2Name
    global Player1Score
    global Player2Score
    global EndScore;
    EndScore = input("What do you want to play to? ")
    def play():  
        global Player1Name
        global Player2Name
        global Player1Score
        global Player2Score
        while Player1Score != int(EndScore) or Player2Score != int(EndScore):                  #Start of War while lopp
            RandomNumber1 = random.randint(0,len(cards)-1)
            RandomNumber2 = random.randint(0,len(cards)-1)
            Player1Card = cards[RandomNumber1]
            Player2Card = cards[RandomNumber2]
            print(Player1Name + "-" + str(Player1Card))
            print(Player2Name + "-" + str(Player2Card))
            time.sleep(3)
            if RandomNumber1 > RandomNumber2:
                print (str(Player1Name) + " wins!!!")
                Player1Score += 1
                print("Score- " + Player1Name + "-" + str(Player1Score))
                print("Score- " + Player2Name + "-" + str(Player2Score))
                print("<------------->")
                time.sleep(3)
            elif RandomNumber2 > RandomNumber1:
                print (str(Player2Name) + " wins!!!")
                Player2Score += 1
                print("Score- " + Player1Name + "-" + str(Player1Score))
                print("Score- " + Player2Name + "-" + str(Player2Score))
                print("<------------->")
                time.sleep(3)
            elif RandomNumber1 == RandomNumber2:
                print("You have tied")
                print("Score- " + Player1Name + "-" + str(Player1Score))
                print("Score- " + Player2Name + "-" + str(Player2Score))
                print("<------------->")
                time.sleep(3)
                play()
            else:
                print("You broke the game. Well played.")
                initial()
            if Player1Score == EndScore:
                print(Player1Name + " wins the game!")
                initial()
            elif Player2Score == EndScore:
                print(Player2Name + " wins the game!")
                initial()
    Player1Score = 0
    Player2Score = 0
    Player1Name = raw_input("What is your name, player 1? ")
    Player2Name = raw_input("What is your name, player 2? ")
    print("Welcome to War, " + Player1Name + " and " + Player2Name)
    cards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    play()

"""
For Alex- Found errors-
    +4 and 4 glitch
    +2 and 2 glitch
    +2 not working for player 2 to 3
    Others bot's +4 not showing color and card.
"""
colors = ["red", "blue", "green", "yellow"]
cards = [1,2,3,4,5,6,7,8,9,10,11,12]       #9 is reverse, 10 is +2, and 11 is +4, 12 is skip
topCard = "red1"
def uno():
    global drawNewCard;
    global colors;
    global cards;
    global topCard;
    global player2Cards;
    global player3Cards;
    #global drawOneCard();
    print("")
    print("")
    print("Uno has been started. ");
    qInst = raw_input("Would you like to read the instructions? ")
    if qInst.lower() == "yes":
        print("")
        print("The instructions of uno: You start with 7 cards.")
        print("You have to match the color, number, or other ending of your card with the corresponding topic of the top card")
    else:
        print("")
    print("If you would like to draw a card, type " + chr(34) +"draw" + chr(34))
    print("Also, the reverses are not perfect")
    if qInst.lower() == "yes":
        time.sleep(15)
    order = ["P1", "P2", "P3"]              #User is player one.
    playerHasWon = False;
    player1Cards = [];
    startTopCard = random.randint(0,8)
    startTopColor = random.randint(0,3)
    topCard = str(colors[int(startTopColor)])+str(cards[int(startTopCard)])
    newCard = random.randint(0, 12)        #Getting new value for card list
    while len(player1Cards) != 7:
        newCard = random.randint(0, 12)
        if newCard <= 8:                                    #Number of cards
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            newCard = cards[newCard]
            player1Cards.insert(0,str(newColor) + str(newCard))             #Giving Cards color and putting them into player1Cards
        elif newCard == 9:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player1Cards.insert(len(player1Cards)-1,str(newColor)+" reverse")             #Giving Reverse
        elif newCard == 10:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player1Cards.insert(len(player1Cards)-1, str(newColor)+" +2")   #Giving +2
        elif newCard == 11:
            player1Cards.insert(len(player1Cards)-1,"+4")                  #Giving +4
        elif newCard == 12:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player1Cards.insert(len(player1Cards)-1, str(newColor)+" skip") #Giving Skip
        else:
            player1Cards.insert(len(player1Cards)-1,"change color")                #If error
    player1Cards.insert(0,player1Cards[6])
    player1Cards.pop(int(len(player1Cards)-1));
    #print(str(player1Cards))
    plusTwo = 0;
    plusFour = 0;
    skipTrue = False;
    bot1GetCards();
    bot2GetCards();
    while playerHasWon == False:            #Starting the Loop!!!!!!!!!!!!!!!!
        if int(len(player1Cards)) == 0 or int(len(player2Cards)) == 0 or int(len(player3Cards)) == 0:     #Checking if player won
            playerHasWon = True;
            order = []
        #playerHasWon = True                #Ending the loop
        #print(player2Cards)
        #print(player3Cards)
        for players in order:
            print("Top Card: " + str(topCard))
            if players == "P1":                         #Player 1's Turn
                if plusTwo > 0:
                        plusTwo = 0
                        drawOneCard();
                        player1Cards.append(drawNewCard);
                        drawOneCard();
                        player1Cards.append(drawNewCard);
                        skipTrue = True;
                if plusFour > 0:
                        plusFour = 0;
                        drawFour = 0;
                        while drawFour != 4:
                            drawFour +=1;
                            drawOneCard();
                            player1Cards.append(drawNewCard);
                        skipTrue = True;
                if skipTrue == False:
                    cardPlayable = False;
                    while cardPlayable == False:
                        print("")
                        printhand = "";
                        handLength = 0
                        while handLength != len(player1Cards):
                            
                            printhand += player1Cards[int(handLength)] + "    "
                            handLength+=1;
                        print("Your hand:  " + str(printhand))
                        #print(player1Cards)                         #Printing Players Hand
                        playedCard = raw_input("What card would you like to play? ")
                        works = playedCard.lower() in player1Cards
                        if works == True and playedCard.lower() != "draw":
                            #print("That card is in your deck")
                            acceptChangeC = False;
                            if playedCard[-2:] == "+4":
                                plusFour = 1;
                                acceptChangeC = True;
                                topCard = playedCard.lower();
                            elif playedCard[-5:].lower() == "color":
                                print("You have played a change color card.")
                                acceptChangeC = True;
                            elif playedCard[:3].lower() == topCard[:3] or playedCard[-2:].lower() == topCard[-2:] or playedCard[-1:] == topCard[-1:]:          #checks same color or +2, change color, skip
                                if playedCard[-2:].lower() == topCard[-2:]:
                                    #print("Same ending")
                                    player1Cards.remove(playedCard.lower())
                                    topCard = playedCard.lower()
                                    cardPlayable = True;
                                    if playedCard[-2:] == "+2":
                                        plusTwo = 1;
                                    elif playedCard[-2:] == "ip":
                                        skipTrue = True;
                                    elif playedCard[-4:] == "erse":
                                        order.reverse();
                                        #print("The order should be reversed.")
                                elif playedCard[-1:] == topCard[-1:]:
                                    #print("Same number")
                                    cardPlayable = True;
                                    player1Cards.remove(playedCard.lower())
                                    topCard = playedCard.lower()
                                elif playedCard[:3] == topCard[:3]:
                                    #print("Same start")
                                    player1Cards.remove(playedCard.lower())
                                    topCard = playedCard.lower()
                                    cardPlayable = True;
                                    if playedCard[-2:] == "+2":
                                        plusTwo = 1;
                                    elif playedCard[-2:] == "ip":
                                        skipTrue = True;
                                    elif playedCard[-4:] == "erse":
                                        order.reverse();
                                        #print("The order should be reversed.")
                                else:
                                    print("You broke the code")
                            else:
                                print("That card is not playable")
                                print("")
                                print("Top Card: "+ str(topCard))
                            while acceptChangeC == True:
                                RColor = raw_input("What color would you ike to change it to? ")
                                if RColor.lower() in colors:
                                    acceptChangeC = False;
                                    cardPlayable = True;
                                    topCard = (RColor.lower())
                                    if playedCard.lower() == "change color":
                                        player1Cards.remove("change color")
                                    elif playedCard.lower() == "+4":
                                        player1Cards.remove("+4")
                                else:
                                    print("That was an invalid color.")
                        elif playedCard.lower() == "draw":
                            drawOneCard()
                            player1Cards.append(drawNewCard)
                            cardPlayable = True;
                        else:
                            print("That was not one of your cards. ");
                else:
                    print("")
                    print("Your Turn has been skipped.")
                    time.sleep(3)
                    skipTrue = False;
            if players == "P2":                                     #Player 2's Turn
                print("")
                print("Player 2's turn")
                reason = "Player 2's turn has been skipped";
                if plusTwo > 0:
                    plusTwo = 0
                    drawOneCard();
                    player2Cards.append(drawNewCard);
                    drawOneCard();
                    player2Cards.append(drawNewCard);
                    skipTrue = True;
                    print("player 2 drew 2 cards")
                    reason = "";
                if plusFour > 0:
                    plusFour = 0;
                    drawFour = 0;
                    while drawFour != 4:
                        drawFour +=1;
                        drawOneCard();
                        player2Cards.append(drawNewCard);
                    skipTrue = True;
                    print("Player 2 drew 4 cards")
                    reason = "";
                if skipTrue == True:
                    print(reason)
                    skipTrue = False;
                else:
                    print("Checking P2 cards")                  #Checking the bots cards
                    cardPlayable = False;
                    for card in player2Cards:
                        #print(card)                     #Checking card
                        if cardPlayable == False:
                            if card == "+4":
                                plusFour = 1;
                                botColor = random.randint(0,3)
                                topCard = colors[int(botColor)]
                                player2Cards.remove("+4")
                                cardPlabyable = True;
                            elif card == "change color":
                                botColor = random.randint(0,3)
                                topCard = colors[int(botColor)]
                                player2Cards.remove("change color")
                                cardPlayable = True;
                            if card[:3].lower() == topCard[:3] or card[-2:].lower() == topCard[-2:] or card[-1:] == topCard[-1:]:          #checks same color or +2, change color, skip
                                if card[-2:].lower() == topCard[-2:]:           #Special Cards
                                    #print("Same ending")
                                    player2Cards.remove(card)
                                    if card != "+4" or card[-2:] != "+2":
                                        topCard = card.lower()
                                    cardPlayable = True;
                                    if card[-2:] == "+2":
                                        plusTwo = 1;
                                        #print("A plus 2 has been played")
                                    elif card[-2:].lower() == "ip":
                                        skipTrue = True;
                                    elif card[-2:].lower() == "se":
                                        order.reverse();
                                elif card[-1:] == topCard[-1:]:                 #Same Number Cards
                                    #print("Same number")
                                    cardPlayable = True;
                                    player2Cards.remove(card)
                                    if card != "+4" or card[-2:] != "+2":
                                        topCard = card.lower()
                                elif card[:3] == topCard[:3]:                   #Same Color Cards
                                    #print("Same start")
                                    player2Cards.remove(card)
                                    topCard = card.lower()
                                    cardPlayable = True;
                                    if card[-2:] == "+2":
                                        plusTwo = 1;
                                    elif card[-2:] == "ip":
                                        skipTrue = True;
                                    elif card[-4:] == "erse":
                                        order.reverse();
                                        #print("The order should be reversed.")
                    if cardPlayable == False:
                        drawOneCard();
                        player2Cards.append(drawNewCard)
                        print("Player 2 drew a card")
                time.sleep(2);
            if players == "P3":                                     #Player 3's Turn
                print("")
                print("Player 3's turn");
                reason = "Player 3's turn has been skipped";
                if plusTwo > 0:
                    plusTwo = 0
                    drawOneCard();
                    player3Cards.append(drawNewCard);
                    drawOneCard();
                    player3Cards.append(drawNewCard);
                    reason = "";
                    skipTrue = True;
                    print("Player 3 drew 2 cards")
                if plusFour > 0:
                    plusFour = 0;
                    drawFour = 0;
                    while drawFour != 4:
                        drawFour +=1;
                        drawOneCard();
                        player3Cards.append(drawNewCard);
                    skipTrue = True;
                    reason = "";
                    print("")
                if skipTrue == True:
                    print(reason)
                    skipTrue = False;
                else:
                    print("Checking P3 cards")                  #Checking the bots cards
                    cardPlayable = False;
                    for card in player3Cards:
                        #print(card)         #Checking card
                        if cardPlayable == False:
                            if card == "+4":
                                plusFour = 1;
                                botColor = random.randint(0,3)
                                topCard = colors[int(botColor)]
                                player3Cards.remove("+4")
                                cardPlayable = True;
                            elif card == "change color":
                                botColor = random.randint(0,3)
                                topCard = colors[int(botColor)]
                                player3Cards.remove("change color")
                                cardPlayable = True;
                            if card[:3].lower() == topCard[:3] or card[-2:].lower() == topCard[-2:] or card[-1:] == topCard[-1:]:          #checks same color or +2, change color, skip
                                if card[-2:].lower() == topCard[-2:]:
                                    #print("Same ending")
                                    player3Cards.remove(card)
                                    if card != "+4" or card[-2:] != "+2":
                                        topCard = card.lower()
                                    cardPlayable = True;
                                    if card[-2:] == "+2":
                                        plusTwo = 1;
                                    elif card[-2:].lower() == "ip":
                                        skipTrue = True;
                                    elif card[-2:].lower() == "se":
                                        order.reverse();
                                elif card[-1:] == topCard[-1:]:
                                    #print("Same number")
                                    cardPlayable = True;
                                    player3Cards.remove(card)
                                    if card != "+4" or card[-2:] != "+2":
                                        topCard = card.lower()
                                elif card[:3] == topCard[:3]:
                                    #print("Same color")
                                    player3Cards.remove(card)
                                    topCard = card.lower()
                                    cardPlayable = True;
                                    if card[-2:] == "+2":
                                        plusTwo = 1;
                                    elif card[-2:] == "ip":
                                        skipTrue = True;
                                    elif card[-4:] == "erse":
                                        order.reverse();
                                        #print("The order should be reversed.")
                    if cardPlayable == False:
                        drawOneCard();
                        player3Cards.append(drawNewCard);
                        print("Player 3 drew a card")
                time.sleep(2);
    if int(len(player1Cards)) == 0:
        print("You have won!")
    elif int(len(player2Cards)) == 0:
        print("Player 2 has won!")
    elif int(len(player2Cards)) == 0:
        print("Player 3 has won!")
    #start code again line?
player = 1;
drawNewCard = "";
def drawOneCard():
    global colors;
    global cards;
    global drawNewCard;
    newCard = random.randint(0, 12)        #Getting new value for card list
    if newCard <= 8:                                    #Number of cards
        randColor = random.randint(0,3)
        newColor = colors[randColor]
        newCard = cards[newCard]
        drawNewCard = str(newColor) + str(newCard)             #Giving Cards color and putting them into player2Cards
    elif newCard == 9:
        randColor = random.randint(0,3)
        newColor = colors[randColor]
        drawNewCard = str(newColor) + " reverse"                                 #Giving Reverse
    elif newCard == 10:
        randColor = random.randint(0,3)
        newColor = colors[randColor]
        drawNewCard = str(newColor)+ " +2"   #Giving +2
    elif newCard == 11:
        drawNewCard = "+4"                  #Giving +4
    elif newCard == 12:
        randColor = random.randint(0,3)
        newColor = colors[randColor]
        drawNewCard = str(newColor)+" skip" #Giving Skip
    else:
        drawNewCard = newCard                #If error
player2Cards = [];
def bot1GetCards():
    global player2Cards;
    global colors;
    global cards;
    newCard = random.randint(0, 12)        #Getting new value for card list
    while len(player2Cards) != 7:
        newCard = random.randint(0, 12)
        if newCard <= 8:                                    #Number of cards
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            newCard = cards[newCard]
            player2Cards.insert(0,str(newColor) + str(newCard))             #Giving Cards color and putting them into player2Cards
        elif newCard == 9:
            player2Cards.insert(len(player2Cards)-1," reverse")             #Giving Reverse
        elif newCard == 10:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player2Cards.insert(len(player2Cards)-1, str(newColor)+" +2")   #Giving +2
        elif newCard == 11:
            player2Cards.insert(len(player2Cards)-1," +4")                  #Giving +4
        elif newCard == 12:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player2Cards.insert(len(player2Cards)-1, str(newColor)+" skip") #Giving Skip
        else:
            player2Cards.insert(len(player2Cards)-1,newCard)                #If error
    player2Cards.insert(0,player2Cards[6])
    player2Cards.pop(int(len(player2Cards)-1));
    #print(str(player2Cards))
player3Cards = [];
def bot2GetCards():
    global player3Cards;
    global colors;
    global cards;
    newCard = random.randint(0, 12)        #Getting new value for card list
    while len(player3Cards) != 7:
        newCard = random.randint(0, 12)
        if newCard <= 8:                                    #Number of cards
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            newCard = cards[newCard]
            player3Cards.insert(0,str(newColor) + str(newCard))             #Giving Cards color and putting them into player2Cards
        elif newCard == 9:
            player3Cards.insert(len(player3Cards)-1," reverse")             #Giving Reverse
        elif newCard == 10:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player3Cards.insert(len(player3Cards)-1, str(newColor)+" +2")   #Giving +2
        elif newCard == 11:
            player3Cards.insert(len(player3Cards)-1," +4")                  #Giving +4
        elif newCard == 12:
            randColor = random.randint(0,3)
            newColor = colors[randColor]
            player3Cards.insert(len(player3Cards)-1, str(newColor)+" skip") #Giving Skip
        else:
            player3Cards.insert(len(player3Cards)-1,newCard)                #If error
    player3Cards.insert(0,player3Cards[6])
    player3Cards.pop(int(len(player3Cards)-1));
    #print(str(player3Cards))
RandomNumber = 0;
def gofish(): 
    number1 = 1
    number2 = 1
    matchedcards = []
    print "Welcome to Gofish!"
    hearts = "hearts"
    spades = "spades"
    clubs = "clubs"
    diamonds = "diamonds"
    global RandomNumber;
    allCards=[]
    num = 1
    num2 = 1
    num3 = 1
    num4= 1
    winscore = input("What do you want to play to? (How many matching sets) ")
    while num != 10:
        num+=1
        allCards.append(hearts+str(num))
    allCards.append(hearts+"King")
    allCards.append(hearts+"Queen")
    allCards.append(hearts+"Jack")
    allCards.append(hearts+"Ace")
    while num2 != 10:
        num2+=1
        allCards.append(spades+str(num2))
    allCards.append(spades+"King")
    allCards.append(spades+"Queen")
    allCards.append(spades+"Jack")
    allCards.append(spades+"Ace")
    while num3 != 10:
        num3+=1
        allCards.append(clubs+str(num3))
    allCards.append(clubs+"King")
    allCards.append(clubs+"Queen")
    allCards.append(clubs+"Jack")
    allCards.append(clubs+"Ace")
    while num4 != 10:
        num4+=1
        allCards.append(diamonds+str(num4))
    allCards.append(diamonds+"King")
    allCards.append(diamonds+"Queen")
    allCards.append(diamonds+"Jack")
    allCards.append(diamonds+"Ace")
    

    #print(allCards)
    player1hand = []
    player2hand = []
    player3hand = []
    RandomNumber = random.randint(0, len(allCards)-1)
    while len(player1hand) < 7:
        NewCard = allCards[int(RandomNumber)]
        player1hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    while len(player2hand) < 7:
        NewCard = allCards[int(RandomNumber)]
        player2hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    while len(player3hand) < 7:
        NewCard = allCards[int(RandomNumber)]
        player3hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    print("Your hand is ")
    #print player1hand
    for i in player1hand:
      print(i),
    #print player2hand
    #print player3hand
    #print("Guess the strength, not the suit")
    
    
    while player1hand != winscore or player2hand != winscore or player3hand != winscore:
        """
        print player1hand
        print player2hand
        print player3hand
        """
        print ""
        requestingplayer = input("Would you like to guess from bot 2 or 3? ")
        if requestingplayer == 2:
            requestinghand = player2hand
        elif requestingplayer == 3:
            requestinghand = player3hand
        else:
            print "Please enter a 2 or a 3"
            requestingplayer = input("Would you like to guess from bot 2 or 3? ")
        currentguess = raw_input("I want to guess ")
        currentcheck = 1
        player1score = 0
        player2score = 0
        player3score = 0
        correct = 1
        foundcorrect = 0
        for i in requestinghand:
                if str(currentguess)[-1:] in str(i)[-1:]:
                    print "You have received:"
                    print i
                    player1hand.append(i)
                    requestinghand.remove(i)
                    foundcorrect = 1
                    correct = 1
                    #check()
                elif str(currentguess)[-1:] not in str(i)[-1:] and foundcorrect == 0:
                    correct = 0
        if correct == 0:
            print "Go fish!"
            print"You received "
            RandomNumber = random.randint(0,len(allCards)-1)
            NewCard = allCards[int(RandomNumber)]
            player1hand.append(NewCard)
            del allCards[RandomNumber]
            print NewCard
            #check()
        print "Your new hand is:"
        for i in player1hand:
            print str(i),
        #print player2hand
        foundcorrect = 0
        time.sleep(3)
        print ""
        print "Bot 2 is now playing"
        time.sleep(3)
        RandomGuessingFrom = random.randint(1,2)
        if RandomGuessingFrom == 1:
            OpponentGuess = 1
            requestinghand = player1hand
        elif RandomGuessingFrom == 2:
            OpponentGuess = 3
            requestinghand = player3hand
        print ("Bot 2 will be guessing from player " + str(OpponentGuess))
        time.sleep(3)
        RandomGuessingIndex = random.randint(0,len(player2hand)-1)
        BotGuess = player2hand[RandomGuessingIndex]
        currentguess = BotGuess[-1:]
        if currentguess == "e":
            print("Bot 2 will be guessing a " + str(BotGuess)[-3:])
        elif currentguess == "g":
            print("Bot 2 will be guessing a " + str(BotGuess)[-4:])
        elif currentguess == "n":  
            print("Bot 2 will be guessing a " + str(BotGuess)[-5:])
        elif currentguess == "0":
            print("Bot 2 will be guessing a " + str(BotGuess)[-2:])
        elif currentguess == "k":
            print("Bot 2 will be guessing a " + str(BotGuess)[-4:])
        else:
            print("Bot 2 will be guessing a " + str(currentguess))
        foundcorrect = 0
        for i in requestinghand:
            if str(currentguess)[-1:] in str(i)[-1:]:
                #print "Bot 2 received:"
                #print i
                player2hand.append(i)
                requestinghand.remove(i)
                foundcorrect = 1
                correct = 1
                #check()
            elif str(currentguess)[-1:] not in str(i)[-1:] and foundcorrect == 0:
                correct = 0
        if correct == 0:
            print "Bot 2 had to go fish!"
            #print"Bot 2 received "
            RandomNumber = random.randint(0,len(allCards)-1)
            NewCard = allCards[int(RandomNumber)]
            player2hand.append(NewCard)
            del allCards[RandomNumber]
            #print NewCard
            #check()
        time.sleep(3)
        print "Bot 3 is now playing"
        time.sleep(3)
        RandomGuessingFrom = random.randint(1,2)
        if RandomGuessingFrom == 1:
            OpponentGuess = 1
            requestinghand = player1hand
        elif RandomGuessingFrom == 2:
            OpponentGuess = 2
            requestinghand = player2hand
        print ("Bot 3 will be guessing from player " + str(OpponentGuess))
        time.sleep(3)
        RandomGuessingIndex = random.randint(0,len(player3hand)-1)
        BotGuess = player3hand[RandomGuessingIndex]
        currentguess = BotGuess[-1:]
        if currentguess == "e":
            print("Bot 3 will be guessing a " + str(BotGuess)[-3:])
        elif currentguess == "g":
            print("Bot 3 will be guessing a " + str(BotGuess)[-4:])
        elif currentguess == "n":  
            print("Bot 3 will be guessing a " + str(BotGuess)[-5:])
        elif currentguess == "0":
            print("Bot 3 will be guessing a " + str(BotGuess)[-2:])
        elif currentguess == "k":
            print("Bot 3 will be guessing a " + str(BotGuess)[-4:])
        else:
            print("Bot 3 will be guessing a " + str(currentguess))
        foundcorrect = 0
        for i in requestinghand:                
                if str(currentguess)[-1:] in str(i)[-1:]:
                    #print "Bot 3 received:"
                    #print i
                    player3hand.append(i)
                    requestinghand.remove(i)
                    foundcorrect = 1
                    correct = 1
                    #check()
                elif str(currentguess)[-1:] not in str(i)[-1:] and foundcorrect == 0:
                    correct = 0
        if correct == 0:
            print "Bot 3 had to go fish!"
            #print"Bot 3 received "
            RandomNumber = random.randint(0,len(allCards)-1)
            NewCard = allCards[int(RandomNumber)]
            player3hand.append(NewCard)
            del allCards[RandomNumber]
            #print NewCard
            #check()
    
    """
    currentcheck1 = 1
    p1checkcomplete = 0
    p2checkcomplete = 0
    p3checkcomplete = 0
    while currentcheck1 != 11 and p1checkcomplete == 0: 
        if "hearts" + str(currentcheck1) in player1hand and "spades" + str(currentcheck1) in player1hand and "clubs" + str(currentcheck1) in player1hand and "diamonds" + str(currentcheck1) in player1hand:
            print("You completed the " + str(currentcheck1) + " set!")
            player1hand.remove("hearts" + str(currentcheck1))
            player1hand.remove("spades" + str(currentcheck1))
            player1hand.remove("clubs" + str(currentcheck1))
            player1hand.remove("diamonds" + str(currentcheck1))
            player1score += 1
        currentcheck1 += 1
        if currentcheck1 == 10:
            p1checkcomplete = 1
    currentcheck1 = 1
    currentcheck2 = 1
    p2checkcomplete = 0
    while currentcheck2 != 11 and p2checkcomplete == 0:    
        if "hearts" + str(currentcheck2) and "spades" + str(currentcheck2) and "clubs" + str(currentcheck2) and "diamonds" + str(currentcheck2) in player2hand:
            print("Bot 2 completed the " + str(currentcheck2) + " set!")
            player2hand.remove("hearts" + str(currentcheck2))
            player2hand.remove("spades" + str(currentcheck2))
            player2hand.remove("clubs" + str(currentcheck2))
            player2hand.remove("diamonds" + str(currentcheck2))
            player2score += 1
        currentcheck2 += 1
        if currentcheck2 == 10:
            p2checkcomplete = 1
    currentcheck2 = 1
    currentcheck3 = 1
    while currentcheck3 != 11 and p3checkcomplete == 0:    
        if "hearts" + str(currentcheck3) and "spades" + str(currentcheck3) and "clubs" + str(currentcheck3) and "diamonds" + str(currentcheck3)  in player3hand:
            print("Bot 3 completed the " + str(currentcheck3) + " set!")
            player3hand.remove("hearts" + str(currentcheck3))
            player3hand.remove("spades" + str(currentcheck3))
            player3hand.remove("clubs" + str(currentcheck3))
            player3hand.remove("diamonds" + str(currentcheck3))
            player3score += 1
        currentcheck3 += 1
        if currentcheck3 == 10:
            p3checkcomplete = 1
        
    """
    
    index = 0
    matches = 0;
    while index != len(player1hand)-1:
        matches = 0
        print "checking"
        for i in player1hand:
            if player1hand[[index][-1:]]==i[-1:]:
                matches +=1;
                print("There was a match")
                matchedcards.append(player1hand[index])
                if matches == 3:
                    print("There was a set")
                    player1score += 1
                    for i in matchedcards:
                        player1hand.remove(i)
                        matchedcards.remove(i)
        index += 1
    
    """
    
        print player1hand
        print player2hand
        print player3hand
    """
    if player1score == winscore:
        print "Player 1 won!"
        initial()
    elif player2score == winscore:
        print "Player 2 won!"
        initial()
    elif player3score == winscore:
        print "Player 3 won!"
        initial()


def print_TTT(board):
    l = "  | ";
    for r in range(3):
        print(board[r][0]+l+board[r][1]+l+board[r][2])
        if (r < 2):
            print(12*"-")
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
resetBoard = [[" "," "," "],[" "," "," "],[" "," "," "]];
#print_TTT(board)
XorO = "X";
X=Score()
O=Score()
def TTT(XorO):
    global board;
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    global resetBoard;
    print("")
    print("TicTacToe has been started. ")
    print("Remeber rows go left to right, and coloumns go top to bottom.")
    time.sleep(3);
    #board=resetBoard
    print_TTT(board)
    TTTdone = False;
    TTTPlayed = False;
    list123 = [0,1,2]
    while TTTdone == False:                  #Making sure game isn't over
        TTTPlayed=False;
        for i in list123:                   #Checink 1 person
            if board[i][0]==XorO and board[i][1]==XorO and board[i][2]==XorO:                         #Checking horizontal outcomes.
                TTTDone = True;
                for i in board:
                    i = [" "," "," "]
                print_TTT(board)
                if XorO == "X":
                    X.addScore()
                    print("X score- "+str(X.score))
                    print("X has won")
                elif XorO == "O":
                    O.addScore()
                    print("O score- "+str(O.score))
                    print("O has won")
                TTT(XorO)
            elif board[0][i]==XorO and board[1][i]==XorO and board[2][i]==XorO:                         #Checking vertical outcomes
                TTTDone = True;
                if XorO == "X":
                    X.addScore()
                    print("X score- "+str(X.score))
                    print("X has won")
                elif XorO == "O":
                    O.addScore()
                    print("O score- "+str(O.score))
                    print("O has won")
                    TTT(XorO)
        if board[0][2]==XorO and board[1][1]==XorO and board[2][0]==XorO:                         #Checking diagonal
            TTTDone = True;
            if XorO == "X":
                X.addScore()
                print("X score- "+str(X.score))
                print("X has won")
            elif XorO == "O":
                O.addScore()
                print("O score- "+str(O.score))
                print("O has won")
                TTT(XorO)
        elif board[0][0]==XorO and board[1][1]==XorO and board[2][2]==XorO:                         #Checking other diagonal
            TTTDone = True;
            if XorO == "X":
                X.addScore()
                print("X score- "+str(X.score))
                print("X has won")
            elif XorO == "O":
                O.addScore()
                print("O score- "+str(O.score))
                print("O has won")
                TTT(XorO)
        if XorO == "X":
            XorO = "O"
        elif XorO == "O":
            XorO = "X";
        #print("done checking")
        if TTTdone != True:    
            while TTTPlayed == False:                                               #Making sure player answered
                row = input("Row: ")
                col = input("Column: ")
                if row >= 1 and row <= 3 and col >= 1 and col <= 3:     #checks if coordinate is on grid
                    if board[int(row)-1][int(col)-1] == " ":             #checks if the space is empty
                        board[int(row)-1][int(col)-1] = XorO;           #fills space 
                        TTTPlayed = True;                               #end loop
                        print_TTT(board)                                #reprint board
                    else:
                        print("That space is already taken")
                        TTTPlayed = False;
                else:
                    print("That coordinate is not on the grid")
                    TTTPlayed = False;
        #if TTTdone == True:
        #    print_TTT(board)
    
def initial():
    print("Welcome, what game would you like to play?")
    print("War")
    print("Uno")
    print("Gofish")
    print"TicTacToe"
    gameselection = raw_input()
    if gameselection.lower() == "war":
        war()
    elif gameselection.lower() == "uno":
        uno()
    elif gameselection.lower() == "gofish" or gameselection.lower() == "go fish":
        gofish()
    elif gameselection.lower() == "tictactoe" or gameselection.lower() == "tic tac toe":
        TTT(XorO)
    elif gameselection.lower() == "quit" or "end":
        print("You have ended the program.")
    else:
        print("Please enter one of the card games.")
        initial()

initial()
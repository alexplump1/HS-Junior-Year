import random
import time
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
    print("Uno has been started. ");
    order = ["P1", "P2", "P3"]              #User is player one.
    playerHasWon = False;
    player1Cards = [];
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
                        print(player1Cards)                         #Printing Players Hand
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
                                        print("The order should be reversed.")
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
                                        print("The order should be reversed.")
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
                    print("Your Turn has been skipped.")
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
                                    topCard = card.lower()
                                    cardPlayable = True;
                                    if card[-2:] == "+2":
                                        plusTwo = 1;
                                        print("a plus 2 has been played")
                                    elif card[-2:].lower() == "ip":
                                        skipTrue = True;
                                    elif card[-2:].lower() == "se":
                                        order.reverse();
                                elif card[-1:] == topCard[-1:]:                 #Same Number Cards
                                    #print("Same number")
                                    cardPlayable = True;
                                    player2Cards.remove(card)
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
                                        print("The order should be reversed.")
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
                    skipTrue = True
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
                                        print("The order should be reversed.")
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
    
    
uno()
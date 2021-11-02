allcards = []
num = 0
num2 = 0
num3 = 0
num4 = 0
hearts = "hearts"
spades = "spades"
clubs = "clubs"
diamonds = "diamonds"
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
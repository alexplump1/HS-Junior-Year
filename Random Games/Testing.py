import random
"""
def gofish():
    hearts = "hearts"
    spades = "spades"
    clubs = "clubs"
    diamonds = "diamonds"
    allCards=[]
    num = 0
    num2 = 0
    num3 = 0
    num4= 0
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
    RandomNumber = random.randint(0, 51)
    while len(player1hand) < 7:
        global RandomNumber
        NewCard = allCards[int(RandomNumber)]
        player1hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    while len(player2hand) < 7:
        global RandomNumber
        NewCard = allCards[int(RandomNumber)]
        player2hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    while len(player3hand) < 7:
        global RandomNumber
        NewCard = allCards[int(RandomNumber)]
        player3hand.append(NewCard)
        del allCards[RandomNumber]
        RandomNumber = random.randint(0, len(allCards)-1)
    print player1hand
    print player2hand
    print player3hand
    print allCards
gofish()

listone = ["one", "two", "one", "three", "fivene", "fourne", "seven", "oinrfoefoemrfofene"]
listtwo = []
print(listone)
response = raw_input("Guess ")
for i in listone:
    if response.lower() == i[-2:]:
        listone.remove(i)
print(listone)



list = ["kajsdflsajfdoislj3", "jakjdsfj;5", "hjadjf8"]
listguess = raw_input()

if listguess in list[-1:]:
    print("in list")
elif listguess not in list[-1:]:
    print"not in list"

for i in list:
    if listguess in str(i)[-1:]:
        print("in list")
    elif listguess not in str(i)[-1:]:
        print"not in list"
"""

"""
list2 = ["pizza4", "cheese2"]
var = 4
five  = 2 
if "pizza" + str(var) and "cheese" + str(five) in list2:
    print "in list"

print "i am running"

currentcheck = 1
list = ["hearts2", "spades2", "clubs2", "diamonds2"]

if "hearts" + str(currentcheck) and "spades" + str(currentcheck) and "clubs" + str(currentcheck) and "diamonds" + str(currentcheck) in list:
    print "set complete"
    currentcheck += 1

print ("hearts" + str(currentcheck))
"""

list5 = ["hearts5", "spades5", "diamonds5", "clubs5"]
currentcheck1 = 1
player1score = 0
print list5
while currentcheck1 < 11: 
    if "hearts" + str(currentcheck1) and "spades" + str(currentcheck1) and "clubs" + str(currentcheck1) and "diamonds" + str(currentcheck1)  in list5:
        print("You completed the " + str(currentcheck1) + " set!")
        list5.remove("hearts" + str(currentcheck1))
        list5.remove("spades" + str(currentcheck1))
        list5.remove("clubs" + str(currentcheck1))
        list5.remove("diamonds" + str(currentcheck1))
        player1score += 1
        currentcheck1 += 1
print list5
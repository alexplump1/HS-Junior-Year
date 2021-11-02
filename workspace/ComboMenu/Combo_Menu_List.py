"""
key_words = ("screen", "power", "wifi")
user_input = raw_input("Type a word: ")
if any (i in key_words for i in user_input.split()):
    
    print("You have ordered a " + str(key_words[i]));
"""



sandwichB = False;      
beverageB = False;
friesB = False;
sandwichList = ["chicken", "beef", "tofu"];
sandwichCosts = [5.25, 6.25, 5.75];
drinkSizeList = ["small", "medium", "large"];
drinkSizeCosts = [1.00, 1.75, 2.25];
frySizeList = ["small", "medium", "large"];
frySizeCost = [1.00, 1.50, 2.00];
desiredSandwich = raw_input("What sandwich would you like?\nChicken $5.25\nBeef $6.25\nTofu $5.75 ")    #Asking for a sandwhich
sandwichB = True;
sandwichReal = desiredSandwich.lower() in sandwichList
if sandwichReal == True:
    costSandwich = sandwichCosts[sandwichList.index(desiredSandwich.lower())]
else:
    print("That was not an option")
    sandwichB = False;
    costSandwich = 0.00;
    desiredSandwich = "no sandwich";
if sandwichB == True:
    print("You have ordered a " + desiredSandwich.upper()[ : 1] + desiredSandwich.lower()[1 : 8] +" sandwich")   #Telling them what sandwhich they bought

desiredDrink = raw_input("Would you like a drink? ")    #Asking someone for a drink yes/no
if desiredDrink.lower() == "yes":
    beverageB = True;
    drinkSize = raw_input("What size would you like?\nSmall $1.00\nMedium $1.75\nLarge $2.25 ") #What size drink do they want
    drinkReal = drinkSize in drinkSizeList;
    if drinkReal == True:
        costDrink = drinkSizeCosts[drinkSizeList.index(drinkSize.lower())];
    else:
        print("That was not a valid choice.")
        costDrink = 0.00;
        beverageB = False;
else:
    drinkSize = "no";
    costDrink = 0.00;
if beverageB == True:
    print("You have ordered a " + drinkSize.upper()[ : 1] + drinkSize.lower()[1 : 8] +" drink")   #Telling them what drink size they bought
desiredFries = raw_input("Would you like fries? ")  #Ordering fries yes/no
if desiredFries.lower() == "yes":
    friesB = True;
    friesSize = raw_input("What size of fries would you like?\nSmall $1.00\nMedium $1.50\nLarge $2.00 ")    #Asking what size fries
    friesReal = friesSize in frySizeList;
    if friesReal == True:
        costFries = frySizeCost[frySizeList.index(friesSize.lower())];
    else:
        print("That was not a valid size.")
        friesB = False;
        costFries = 0.00;
else:
    friesSize = "no";
    costFries = 0.00;
if friesB == True:
    print("You have ordered a " + friesSize.upper()[ : 1] + friesSize.lower()[1 : 8] +" fry")   #Telling them what fry size they ordered
desiredKetchup = raw_input("Would you like ketchup packets? ")  #Ordering ketchup packets yes/no
if desiredKetchup.lower() == "yes":
    numOfKP = input("How many ketchup packets would you like $.25 per packet? ")     #Ordering how many packets
    if numOfKP == int or float:
        costOfKP = int(numOfKP) * 0.25;
    else:
        numOfKP = int(0);
        costOfKP = float(0.00);
else:
    numOfKP = int(0);
    costOfKP = float(0.00);
if sandwichB == True and beverageB == True and friesB == True:      #Finding cost with combo
    costMeal = costSandwich + costDrink + costFries + costOfKP - 1.00;
else:
    costMeal = costSandwich + costDrink + costFries + costOfKP;     #Finding cost without combo
print("You have ordered " + desiredSandwich.upper()[ : 1] + desiredSandwich.lower()[1 : 12] + ", " + drinkSize + " drink, " + friesSize + " fry, and " + str(int(numOfKP)) +" ketchup packets for " + str(costMeal) + " dollars.")

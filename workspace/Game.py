#import time
word = "                             ";
listOne = list(word)
shownWord = "";
place = 0;
spot = 0;
x=0;
def blankSpace():
    global listOne
    global shownWord;
    localx = 0;
    print("Blank Space Started")
    while localx != len(listOne):
        localx +=1;
        shownWord+=listOne[int(localx)-1]
    print(shownWord)
        
up = 5
timesLooped = 0
miniLoop = 0
while timesLooped != 10:
    timesLooped +=1
    miniLoop=0
    while miniLoop != 10:
        miniLoop+=1
        if miniLoop==up:
            print("o")
            
        else:
            print(" ")
"""
while x!=3:
    place = 0;
    while place != 10:
        #time.sleep(.5)
        if spot == place:
            listOne[3] = "o";
        else:
            listOne[3] = " ";
        print(listOne)
        place+=1;
    print("New loop")
    spot += 1;
    x+=1;
print("x is three")
"""
response = raw_input();
#blankSpace();
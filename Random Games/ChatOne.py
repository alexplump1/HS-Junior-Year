class Words:
    def __init__(self, message):
        self.mes = "";
        
    def getMessage(self):
        sendMessage()
        
from ChatTwo import Words2     
returned = Words2()
import time
x = 0
while x != 5:
    y = 0;
    
    while y != 20:
        y+=1;
        time.sleep(.5)
        if len(returned.mes2) > 0:
            print(returned.mes2)
            returned = "";
    x+=1
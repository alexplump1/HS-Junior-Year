response = "";
class Words2:
    def __init__(self):
        self.mes2 = "";
        
    def sendMessage(self):
        self.mes2 = str(response);
        
from ChatOne import Words                   


response = "";
change=Words()
while response.lower() != "quit":
    response = raw_input("What message would you like to send? ")
    if response != "":
        change.getMessage()
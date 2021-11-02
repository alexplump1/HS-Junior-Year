class Reaction():
    
    id_Num=0
    rxnList=[]
    
    def __init__(self):
        self.id_Num=Reaction.id_Num;
        Reaction.id_Num+=1;
        
    def new_SRinput(self, reaction):
        self.rxnList.append(reaction)
        
    def new_DRinput(self, reaction):
        self.rxnList.append(reaction)
        
    def new_Syninput(self, reaction):
        self.rxnList.append(reaction)
        
    def get_reaction(self):
        for i in self.rxnList:
            return i

solos=[]


class Band():
    def __init__(self,name="",members=[],band_name=""):
        self.name=str(name)
        self.members=list(members)
        self.band_name=str(band_name)
        
    def play_solos(self):
        return solos
        
    


        
# __________________________________________________



class Musician(Band):
    def __init__(self,name="",instrument="",type_person="",solo=""):
        self.name=str(name)
        self.instrument=str(instrument)
        self.type_person=str(type_person)
        self.sound=str(solo)
        

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.type_person} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        solos.append(str(self.solo))
        return self.solo
    

# __________________________________________________

class Guitarist(Musician):
    def __init__(self,name="",type_person="",solo=""):
        self.name=str(name)
        self.instrument="guitar"
        self.type_person="Guitarist"
        self.solo="face melting guitar solo"
# __________________________________________________
class Bassist(Musician):
    def __init__(self, name="", type_person="",solo="" ):
        self.name=str(name)
        self.instrument="bass"
        self.type_person="Bassist"
        self.solo="bom bom buh bom"
# __________________________________________________
class Drummer(Musician):
    def __init__(self,name="",type_person="",solo=""):
        self.name=str(name)
        self.instrument="drums"
        self.type_person="Drummer"
        self.solo="rattle boom crash"



    

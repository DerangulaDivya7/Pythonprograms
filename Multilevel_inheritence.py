class grandfather:
    def land(self):
        print("land...")
class father(grandfather):
    def car(self):
        print("parent property...")
class child(father):
    def mobile (self):
        print("child property ....")
obj =child()
obj.mobile()
obj.car()
obj.land()              

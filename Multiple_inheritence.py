class grandfather:
    def designer(self):
        print("designer...")
class father:
    def engineer(self):
        print("cooking...")
class mother:
     def actress(self):
         print("actress....")     
class child(father,mother, grandfather):
    def programming(self):
        print("programming skill....")
obj =child()
obj.programming()
obj.engineer()
obj.actress()             
obj.designer() 

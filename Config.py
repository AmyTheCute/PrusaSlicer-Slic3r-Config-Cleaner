
#Because hashmaps in python make your eyes bleed

class Attribute: 
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __eq__(self, __value: object) -> bool:
        return(self.name == __value.name and self.value == __value.value)

class Config:
    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category
        self.attrs = []


    def addAttr(self, name, value):
        if(self.existsAttr(name)):
            if(self.getAttr(name).value != value):
                print(f'Warning, Attr {name} already exists in {self.name} with a different value, changing')
                self.delAttr(name)
            else:
                return
        self.attrs.append(Attribute(name, value))

    # def addAttr(self, attr: Attribute):
    #     self.attrs.append(attr)

    def getAttr(self, name):
        for i in self.attrs:
            if i.name == name:
                return i
        return None
    
    def existsAttr(self, name):
        for i in self.attrs:
            if i.name == name:
                return True
        return False
            
    def delAttr(self, name):
        for i in self.attrs[:]:
            if i.name == name:
                self.attrs.remove(i)
                return
        print(f'Error, attr {name} not found')
            
    def isDefault(self):
        if "common" in self.name:
            return True
        else: 
            return False
        
        return None
    


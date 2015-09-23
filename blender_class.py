import bge

def init(cont):
    dothings(cont.owner)
        
class dothings(bge.types.KX_GameObject):
    def __init__(self, owner):
        self._name = "omgbbq"
        self._numvalue = 0
        if self._numvalue == 5:
            print("what?")
        self.runthings()
                                        
    def runthings(self):
        print(self._name)
        #print(dir(self))
        self._numvalue = 5

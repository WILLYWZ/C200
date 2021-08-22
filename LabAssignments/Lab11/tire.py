class tire:
    def __init__(self, pressure, flat, leak):
        self.pressure = pressure
        self.flat = flat
        self.leak = leak



        def isflat(self):
            if self.pressure > 80:
                self.flat = False
                self.leak = False
            elif self.pressure == 0:
                self.flat = True
                self.leak = False
            else:
                self.flat = True
                self.leak = False

object = tire(80,0,0)
object.detail()        
u
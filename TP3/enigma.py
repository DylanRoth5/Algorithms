class Enigma:


    def __init__(self,re,r1,r2,r3,kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.kb = kb


    def set_key(self,key):
        self.r1.rotate_to(key[0])
        self.r2.rotate_to(key[1])
        self.r3.rotate_to(key[2])

    def encipher(self,letter):
        # rotate https://www.youtube.com/watch?v=W6NfcxP8ffY&ab_channel=JoshuaZeitsoff
        # double stepping https://www.youtube.com/watch?v=5StZlF-clPc&t=24s&ab_channel=JoshuaZeitsoff
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()
        
        
        #pass signal
        signal = self.kb.forward(letter)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.re.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        letter = self.kb.backward(signal)
        return letter
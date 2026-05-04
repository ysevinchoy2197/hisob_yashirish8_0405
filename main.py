#4-misol
class Telefon:
    def __init__(self, model, batareya):
        self.model = model
        self.batareya = batareya
        self.__batareya = 0

    def zaryad_qil(self, foiz):
        self.__batareya += foiz

    def foydalan(self, foiz):
        self.__batareya -= foiz

    def info(self):
        print(f"Modeli: {self.model}")
        print(f"Batargiyasi: {self.__batareya}")

t1 = Telefon("iphone", "80")
t1.info()

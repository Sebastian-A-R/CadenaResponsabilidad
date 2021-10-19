from iaprobador import IAprobador

class Gerente(IAprobador):

    def __init__(self):
        self.next = IAprobador

    def getNext(self):
        
        return self.next
    
    def solicitudPrestamo(self,monto):
        if (monto > 50000 and monto <= 100000):
            print("Lo manejo yo, el Gerente")
        else:
            self.next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        self.next=aprobador
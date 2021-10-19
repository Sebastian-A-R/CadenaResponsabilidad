from iaprobador import IAprobador

class EjecutivoCuenta(IAprobador):

    def __init__(self):
        self.next = IAprobador

    def getNext(self):
        return self.next
    
    def solicitudPrestamo(self,monto):
        if (monto <= 10000):
            print("Lo manejo yo, el ejecutivo de cuenta")
        else:
            self.next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        self.next=aprobador
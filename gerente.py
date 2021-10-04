from iaprobador import IAprobador

class Gerente(IAprobador):

    next = IAprobador

    def getNext(self):
        next = IAprobador
        return next
    
    def solicitudPrestamo(self,monto):
        if (monto > 50000 and monto <= 100000):
            print("Lo manejo yo, el Gerente")
        else:
            next = IAprobador
            next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        next=aprobador
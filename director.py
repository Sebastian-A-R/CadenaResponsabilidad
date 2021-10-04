from iaprobador import IAprobador

class Director(IAprobador):
    
    next = IAprobador

    def getNext(self):
        next = IAprobador
        return next
    
    def solicitudPrestamo(self,monto):
        if (monto > 100000):
            print("Lo manejo yo, el Director")
        else:
            next = IAprobador
            next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        next=aprobador
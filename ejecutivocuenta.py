from iaprobador import IAprobador

class EjecutivoCuenta(IAprobador):

    next = IAprobador

    def getNext(self):
        next = IAprobador
        return next
    
    def solicitudPrestamo(self,monto):
        if (monto <= 10000):
            print("Lo manejo yo, el ejecutivo de cuenta")
        else:
            next = IAprobador
            next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        next=aprobador
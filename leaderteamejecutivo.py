from iaprobador import IAprobador

class LeaderTeamEjecutivo(IAprobador):
    
    next = IAprobador

    def getNext(self):
        next = IAprobador
        return next
    
    def solicitudPrestamo(self,monto):
        if (monto > 10000 and monto<=50000):
            print("Lo manejo yo, el Lider")
        else:
            next.solicitudPrestamo(monto)

    def setNext(self,aprobador):
        next=aprobador
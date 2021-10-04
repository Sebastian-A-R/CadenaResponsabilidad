from iaprobador import IAprobador
from gerente import Gerente
from ejecutivocuenta import EjecutivoCuenta
from director import Director
from leaderteamejecutivo import LeaderTeamEjecutivo

class Banco(IAprobador):

    
    next1 = IAprobador


    def getNext(self):

        return next

    
    def solicitudPrestamo(self,monto):
        
        ejecutivo = EjecutivoCuenta()
        self.setNext(ejecutivo)
        
        lider = LeaderTeamEjecutivo()
        ejecutivo.setNext(lider)

        gerente = Gerente()
        lider.setNext(gerente)

        director = Director()
        gerente.setNext(director)

        next = IAprobador

        next.solicitudPrestamo(monto)


    def setNext(self,aprobador):
        next=aprobador
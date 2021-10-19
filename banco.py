from iaprobador import IAprobador
from gerente import Gerente
from ejecutivocuenta import EjecutivoCuenta
from director import Director
from leaderteamejecutivo import LeaderTeamEjecutivo

class Banco(IAprobador):

    def __init__(self):
        self.next = IAprobador


    def getNext(self):

        return self.next

    
    def solicitudPrestamo(self,monto):
        
        ejecutivo = EjecutivoCuenta()
        self.setNext(ejecutivo)
        
        lider = LeaderTeamEjecutivo()
        ejecutivo.setNext(lider)

        gerente = Gerente()
        lider.setNext(gerente)

        director = Director()
        gerente.setNext(director)

        self.next.solicitudPrestamo(monto)


    def setNext(self,aprobador):
        self.next=aprobador
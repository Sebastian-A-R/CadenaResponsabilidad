from abc import ABCMeta, abstractclassmethod, abstractmethod

class IAprobador:

    __metaclass__ = ABCMeta

    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def solicitudPrestamo(self,monto):
        pass

    @abstractmethod
    def setNext(self,aprobador):
        pass

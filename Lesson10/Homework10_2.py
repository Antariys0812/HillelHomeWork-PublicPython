from abc import abstractmethod, ABC

class Figura(ABC):

    @abstractmethod
    def plosha(self):
        pass

    @abstractmethod
    def perymetr(self):
        pass

class Kvadrat(Figura):
    def __init__(self, storona = 0):
        self.__storona = storona

    def get_storona(self):
        return self.__storona

    def set_storona(self, storona):
             self.__storona = storona

    def plosha(self):
        return self.get_storona()*self.get_storona()

    def perymetr(self):
        return self.get_storona()*4

class Prjamokutnyk(Figura):
    def __init__(self, storona_a = 0, storona_b = 0):
        self.__storona_a = storona_a
        self.__storona_b = storona_b

    def get_storona_a(self):
        return self.__storona_a

    def set_storona_a(self, storona_a):
        self.__storona_a = storona_a

    def get_storona_b(self):
        return self.__storona_b

    def set_storona_b(self, storona_b):
            self.__storona_b = storona_b

    def plosha(self):
        return self.get_storona_a()*self.get_storona_b()

    def perymetr(self):
        return (self.get_storona_a()+self.get_storona_b())*2

class Romb(Figura):
    def __init__(self, storona = 0, vysota = 0):
        self.__storona = storona
        self.__vysota = vysota

    def get_storona(self):
        return self.__storona

    def set_storona(self, storona):
        self.__storona = storona

    def get_vysota(self):
        return self.__vysota

    def set_vysota(self, vysota):
            self.__vysota = vysota

    def plosha(self):
        return (self.get_storona()*self.get_vysota())

    def perymetr(self):
        return self.get_storona()*4

figura1 = Prjamokutnyk()
figura1.set_storona_a(10)
figura1.set_storona_b(3)
figura2 = Kvadrat()
figura2.set_storona(5)
figura3 = Romb()
figura3.set_storona(5)
figura3.set_vysota(6)

list_figur = [figura1, figura2, figura3]

for figura in list_figur:
        print(f' Площа - {figura.plosha()}, Периметр - {figura.perymetr()}')


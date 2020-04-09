from interface import implements, Interface

class ISample(Interface):

    def ApplyTitration(self, i):
        pass

    def Euler(self):
        pass

    @staticmethod
    def Animate(i):
        pass



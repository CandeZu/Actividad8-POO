class Conjunto:
    __conjunto = []

    def __init__(self, lista):
        self.__conjunto = lista
    
    def mostrar (self):
        return self.__conjunto
    
    def getLista (self):
        return self.__conjunto

    def __add__(self, otroConjunto):
        union = self.__conjunto + otroConjunto.getLista()
        return Conjunto(union)

    def __sub__(self, otroConjunto):
        nuevo = self.__conjunto.copy()
        for x in otroConjunto.getLista():
            if x in nuevo:
                nuevo.remove(x)
        return Conjunto(nuevo)
        
    def __eq__(self, otroConjunto):
        if self.__conjunto == otroConjunto.getLista():
            return True
        else:
            return False
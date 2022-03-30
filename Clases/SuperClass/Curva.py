import math
import numpy


class curva():
    def __init__(self, v1, v2, v3, ra) -> None:
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__ra = ra

# -----------geters and setters---------------------

    @property
    def GetV1(self):
        return self.__v1

    @property
    def GetV2(self):
        return self.__v2

    @property
    def GetV3(self):
        return self.__v3

    @property
    def GetRa(self):
        return self.__ra

    @GetV1.setter
    def SetV1(self, valor):
        try:
            if type(valor) == float or type(valor) == int:
                self.__v1 = valor
        except TypeError:
            return "no es un valor numerico"

    @GetV2.setter
    def SetV2(self, valor):
        try:
            if type(valor) == float or type(valor) == int:
                self.__v2 = valor
        except TypeError:
            return "no es un valor numerico"

    @GetV3.setter
    def SetV3(self, valor):
        try:
            if type(valor) == float or type(valor) == int:
                self.__v3 = valor
        except TypeError:
            return "no es un valor numerico"

    @GetRa.setter
    def SetRa(self, valor):
        try:
            if type(valor) == float or type(valor) == int:
                self.__ra = valor
        except TypeError:
            return "no es un valor numerico"

# -----------Metodos o funciones---------------------
    def Azimut_1_2(self):
        dn = self.__v2[1]-self.__v1[1]
        de = self.__v2[0]-self.__v1[0]
        if len(self.__v1) == 2 and len(self.__v2) == 2:
            if dn > 0 and de > 0:  # -->primer cuadrante
                return math.atan(de/dn)
            elif dn < 0 and de > 0:  # --> segundo cuadrante
                return math.radians(180) + math.atan(de/dn)
            elif dn < 0 and de < 0:  # --> tercer cuadrante
                return math.radians(180) + math.atan(de/dn)
            elif dn > 0 and de < 0:  # -->cuarto cuadrante
                return math.radians(360) + math.atan(de/dn)

    def Azimut_2_3(self):
        dn = self.__v3[1]-self.__v2[1]
        de = self.__v3[0]-self.__v2[0]
        if len(self.__v2) == 2 and len(self.__v3) == 2:
            if dn > 0 and de > 0:  # -->primer cuadrante
                return math.atan(de/dn)
            elif dn < 0 and de > 0:  # --> segundo cuadrante
                return math.radians(180) + math.atan(de/dn)
            elif dn < 0 and de < 0:  # --> tercer cuadrante
                return math.radians(180) + math.atan(de/dn)
            elif dn > 0 and de < 0:  # -->cuarto cuadrante
                return math.radians(360) + math.atan(de/dn)


curv = curva((100, 100), (200, 150), (100, 50), 20)

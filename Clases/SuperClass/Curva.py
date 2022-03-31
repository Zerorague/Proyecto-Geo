from turtle import *
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

    def SetV1(self, este, norte):
        try:
            if (type(este) == float, type(norte) == float):
                self.__v1 = (este, norte)
        except TypeError:
            return "no es un valor numerico"

    def SetV2(self, este, norte):
        try:
            if (type(este) == float, type(norte) == float):
                self.__v2 = (este, norte)
        except TypeError:
            return "no es un valor numerico"

    def SetV3(self, este, norte):
        try:
            if (type(este) == float, type(norte) == float):
                self.__v3 = (este, norte)
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

# ----------azimut-------------
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

# -------------distancias alineamientos-------------
    def dh_1_2(self):
        dn = self.__v2[1]-self.__v1[1]
        de = self.__v2[0]-self.__v1[0]
        return math.sqrt(dn**2 + de**2)

    def dh_2_3(self):
        dn = self.__v3[1]-self.__v2[1]
        de = self.__v3[0]-self.__v2[0]
        return math.sqrt(dn**2 + de**2)

    def dh_1_3(self):
        dn = self.__v3[1]-self.__v1[1]
        de = self.__v3[0]-self.__v1[0]
        return math.sqrt(dn**2 + de**2)

# --------------elementos geometricos de la curva---------------
    def Omega(self):
        try:
            if self.Azimut_1_2() > self.Azimut_2_3():
                return (self.Azimut_1_2()-self.Azimut_2_3)/2
            else:
                return (self.Azimut_2_3()-self.Azimut_1_2())/2
        except:
            return "No existe deflexion"

    def Alfa(self):  # -----identificar problema
        if 0 < self.Azimut_1_2() < math.radians(90) and math.radians(90) < self.Azimut_2_3() < math.radians(180) or 0 < self.Azimut_1_2() < math.radians(90) and 0 < self.Azimut_2_3() < math.radians(90) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(90) < self.Azimut_1_2() < math.radians(180) and math.radians(90) < self.Azimut_2_3() < math.radians(180) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(180) < self.Azimut_1_2() < math.radians(270) and math.radians(180) < self.Azimut_2_3() < math.radians(270) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(270) < self.Azimut_1_2() < math.radians(360) and math.radians(270) < self.Azimut_2_3() < math.radians(360) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(90) < self.Azimut_1_2() < math.radians(180) and math.radians(180) < self.Azimut_2_3() < math.radians(270) or math.radians(90) < self.Azimut_1_2() < math.radians(180) and math.radians(90) < self.Azimut_2_3() < math.radians(180) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(270) < self.Azimut_1_2() < math.radians(360) and 0 < self.Azimut_2_3() < math.radians(90) or math.radians(270) < self.Azimut_1_2() < math.radians(360) and math.radians(270) < self.Azimut_2_3() < math.radians(360) and self.Azimut_1_2() < self.Azimut_2_3() or math.radians(180) < self.Azimut_1_2() < math.radians(270) and math.radians(270) < self.Azimut_2_3() < math.radians(360):
            return math.radians(180) + (self.Omega()*2)

        else:
            return math.radians(180) - (self.Omega()*2)


curv = curva((100, 100), (200, 150), (100, 50), 20)

# curv.SetV1(300, 85)
# curv.SetV2(75, 689)


print(numpy.degrees(curv.Omega()))

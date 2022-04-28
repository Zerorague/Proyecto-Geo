
from user_class import User, usuario
from math import radians, sqrt, atan, tan, sin, degrees, cos, acos, pi


class Curva():
    def __init__(self, id, project_name, vertices, radio=200, intervalo=10, dm_inicial=0, vp=30) -> None:
        self.__id = id
        self.__project_name = project_name
        self.__vertices = vertices
        self.__intervalo = intervalo
        self.__dm_inicial = dm_inicial
        self.__vp = vp
        self.__radio = radio
        # ---------variables globales (desempaquetado)---------
        self.__v1, self.__v2, self.__v3 = self.__vertices
        self.__e1, self.__n1 = self.__v1
        self.__e2, self.__n2 = self.__v2
        self.__e3, self.__n3 = self.__v3
        self.__DeltaEste1 = self.__e2-self.__e1
        self.__DeltaNorte1 = self.__n2-self.__n1
        self.__DeltaEste2 = self.__e3-self.__e2
        self.__DeltaNorte2 = self.__n3-self.__n2
        self.__DeltaEste3 = self.__e3-self.__e1
        self.__DeltaNorte3 = self.__n3-self.__n1

    @property
    def Get_id(self):
        return self.__id

    @property
    def Get_project_name(self):
        return self.__project_name

    @property
    def Get_vp(self):
        return self.__vp

    @property
    def Get_intervalo(self):
        return self.__intervalo

    @property
    def Get_vertices(self):
        return self.__vertices

    @property
    def Get_dm_inicial(self):
        return self.__dm_inicial

    @property
    def Get_radio(self):
        return self.__radio

    @Get_project_name.setter
    def Set_project_name(self, valor):
        if valor == str:
            self.__project_name = valor
        else:
            return "caracter no valido"

    @Get_vertices.setter
    def Set_vertices(self, valor):
        if len(valor) == 3:
            for i in valor:
                for j in i:
                    if type(j) == float:
                        self.__vertices = valor
                    else:
                        return "Se esperaban numeros Reales"

    @Get_intervalo.setter
    def Set_intervalo(self, valor):
        if type(valor) == int:
            self.__intervalo = valor
        else:
            return "intervalo debe pertenecer a los enteros"

    @Get_vp.setter
    def Set_vp(self, valor):
        if type(valor) == float or type(valor) == int:
            self.__vp = valor
        else:
            return "valor debe pertenecer a los reales"

    @Get_dm_inicial.setter
    def Set_dm_inicial(self, valor):
        if type(valor) == float or type(valor) == int:
            self.__dm_inicial = valor
        else:
            return "valor debe pertenecer a los reales"

    @Get_radio.setter
    def Set_radio(self, valor):
        if (type(valor) == float or type(valor) == int) and valor > 0:
            self.__radio = valor
        else:
            return "radio debe ser mayor a cero y pertenecer a los reales"

# --------------------elementos geometricos-----------------------

    def distancias_vertices(self):
        distancia_v_1_2 = sqrt(self.__DeltaEste1**2+self.__DeltaNorte1**2)
        distancia_v_2_3 = sqrt(self.__DeltaEste2**2+self.__DeltaNorte2**2)
        distancia_v_1_3 = sqrt(self.__DeltaEste3**2+self.__DeltaNorte3**2)
        return (distancia_v_1_2, distancia_v_2_3, distancia_v_1_3)

    def azimuts(self):
        try:
            if self.__DeltaEste1 > 0 and self.__DeltaNorte1 > 0:
                azimutOne = atan(self.__DeltaEste1/self.__DeltaNorte1)
            elif self.__DeltaEste1 > 0 and self.__DeltaNorte1 < 0:
                azimutOne = pi + atan(self.__DeltaEste1/self.__DeltaNorte1)
            elif self.__DeltaEste1 < 0 and self.__DeltaNorte1 < 0:
                azimutOne = pi + atan(self.__DeltaEste1/self.__DeltaNorte1)
            else:
                azimutOne = 2*pi + atan(self.__DeltaEste1/self.__DeltaNorte1)

            if self.__DeltaEste2 > 0 and self.__DeltaNorte2 > 0:
                azimutTwo = atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 > 0 and self.__DeltaNorte2 < 0:
                azimutTwo = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 < 0 and self.__DeltaNorte2 < 0:
                azimutTwo = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            else:
                azimutTwo = 2*pi + atan(self.__DeltaEste2/self.__DeltaNorte2)

            if self.__DeltaEste3 > 0 and self.__DeltaNorte3 > 0:
                azimuthThree = atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 > 0 and self.__DeltaNorte3 < 0:
                azimuthThree = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 < 0 and self.__DeltaNorte3 < 0:
                azimuthThree = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            else:
                azimuthThree = 2*pi + \
                    atan(self.__DeltaEste3/self.__DeltaNorte3)
        except ZeroDivisionError:
            return "Ha ocurridio una division por 0"

        return (azimutOne, azimutTwo, azimuthThree)

    def anguloExterior(self):
        distancia_1_2, distancia_2_3, distancia_1_3 = self.distancias_vertices()
        return 2*pi-(acos((distancia_1_2**2+distancia_2_3**2-(distancia_1_3**2))/(2*distancia_1_2*distancia_2_3)))

    def curvaDerecha(self):  # arreglar
        az1, az2, az3 = self.azimuts()
        del az3
        if az1 > pi and az2 < pi/2:
            az2 = 2*pi + az2
        elif az1 < pi/2 and az2 > pi:
            az1 = 2*pi + az1

        if az1 < az2:
            return True
        return False

    def alpha_medio(self):
        try:
            azimutOne, azimutTwo, azimuthThree = self.azimuts()
            del azimuthThree
            if azimutOne > azimutTwo:
                return radians((azimutOne-azimutTwo)/2)
            return radians((azimutTwo-azimutOne)/2)
        except ValueError:
            pass

    def Alfa(self):
        if self.curvaDerecha():
            return pi+(self.alpha_medio()*2)
        else:
            return pi-(self.alpha_medio()*2)

    def Tangente(self):
        try:
            return self.__radio*tan(self.alpha_medio())
        except TypeError:
            pass

    def Secante(self):
        return self.__radio*((1/cos(self.alpha_medio()))-1)

    def desarrolloCurva(self):
        return (pi*self.__radio*self.alpha_medio())/2*pi

    def cuerdaMaxima(self):
        return 2*self.__radio*sin(self.alpha_medio())

    def ensanche(self):
        pass

    def Peralte(self):
        pass

    def Resumen(self):
        return f"VP: {self.__vp} km/h\nA: {round(degrees(self.Alfa())*(10/9),4)}g\nR: {round(self.__radio,3)}m\nT: {round(self.Tangente(),3)}m\nS: {round(self.Secante(),3)}m\nDC: {round(self.desarrolloCurva(),3)}m"

    # -------------main------------------------

    def DmsLineaEntrada(self):
        distancia = self.__dm_inicial + \
            self.distancias_vertices()[1]-self.Tangente()
        dms = []
        try:
            for i in range(int(self.__dm_inicial), int(distancia), self.__intervalo):
                dms.append(i)
            dms.pop(0)
            dms.insert(0, self.__dm_inicial)
            return dms
        except TypeError:
            pass

    def DmsCurva(self):
        distancia = self.__dm_inicial + \
            self.distancias_vertices()[1]-self.Tangente()
        dms = []
        try:
            for i in range(self.DmsLineaEntrada()[-1], int(distancia+self.desarrolloCurva()), self.__intervalo):
                if i > distancia:
                    dms.append(i)
                else:
                    continue
            dms.insert(0, distancia)
            dms.append(distancia+self.desarrolloCurva())
            return dms
        except TypeError:
            pass

    def DmsLineaSalida(self):
        distanciaFc = self.__dm_inicial + \
            self.distancias_vertices()[1] - \
            self.Tangente()+self.desarrolloCurva()
        distanciaentrada = self.__dm_inicial + \
            self.distancias_vertices()[1]-self.Tangente()
        distancia = distanciaentrada + \
            self.desarrolloCurva() + \
            self.distancias_vertices()[2]-self.Tangente()
        dms = []
        try:
            for i in range(self.DmsCurva()[-2], int(distancia), self.__intervalo):
                if i > distanciaFc:
                    dms.append(i)
            dms.append(distancia)
            return dms
        except TypeError:
            pass

    def coordenadasEntrada(self):
        az1, az2, az3 = self.azimuts()
        del az2, az3
        dh = []
        coordenadas = []
        for i in self.DmsLineaEntrada():
            dh.append(i-self.__dm_inicial)
        for i in dh:
            coordenadas.append(
                (round(self.__e1+i*sin(az1), 3), round(self.__n1 + i*cos(az1), 3)))
        return coordenadas


curva = Curva(1, "Linares", ((1000, 1000), (1500, 1450),
              (500, 1400)), 3000, 10, 50, 30)
print(curva.DmsLineaEntrada())
print(curva.DmsCurva())
print(curva.DmsLineaSalida())
print(curva.curvaDerecha())
curva.Set_vp = 40
print(curva.Resumen())
print(curva.coordenadasEntrada())

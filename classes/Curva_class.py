
from user_class import User, usuario
from math import radians, sqrt, atan, tan, sin, degrees, cos, acos, pi
import xlwt


class Curva():
    def __init__(self, id, project_name, vertices, radio=200, intervalo_recto=10, intervalo_curva=5, dm_inicial=0, vp=30) -> None:
        self.__id = id
        self.__project_name = project_name
        self.__vertices = vertices
        self.__intervalo_recto = intervalo_recto
        self.__intervalo_curva = intervalo_curva
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
    def Get_intervalo_recto(self):
        return self.__intervalo_recto

    @property
    def Get_intervalo_curva(self):
        return self.__intervalo_curva

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

    @Get_intervalo_recto.setter
    def Set_intervalo_recto(self, valor):
        if type(valor) == int:
            self.__intervalo_recto = valor
        else:
            return "intervalo debe pertenecer a los enteros"

    @Get_intervalo_curva.setter
    def Set_intervalo_curva(self, valor):
        if type(valor) == int:
            self.__intervalo_curva = valor
        else:
            return "Intervalor debe pertenecer a los enteros"

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
            elif self.__DeltaEste1 < 0 and self.__DeltaNorte1 > 0:
                azimutOne = 2*pi + atan(self.__DeltaEste1/self.__DeltaNorte1)

            if self.__DeltaEste2 > 0 and self.__DeltaNorte2 > 0:
                azimutTwo = atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 > 0 and self.__DeltaNorte2 < 0:
                azimutTwo = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 < 0 and self.__DeltaNorte2 < 0:
                azimutTwo = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 < 0 and self.__DeltaNorte2 > 0:
                azimutTwo = 2*pi + atan(self.__DeltaEste2/self.__DeltaNorte2)

            if self.__DeltaEste3 > 0 and self.__DeltaNorte3 > 0:
                azimuthThree = atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 > 0 and self.__DeltaNorte3 < 0:
                azimuthThree = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 < 0 and self.__DeltaNorte3 < 0:
                azimuthThree = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 < 0 and self.__DeltaNorte3 > 0:
                azimuthThree = (
                    2*pi + atan(self.__DeltaEste3/self.__DeltaNorte3))
        except ZeroDivisionError:
            return "Ha ocurridio una division por 0"

        return (azimutOne, azimutTwo, azimuthThree)

    def curvaDerecha(self):
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
                return (azimutOne-azimutTwo)/2
            else:
                return (azimutTwo-azimutOne)/2
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
        return (pi*self.__radio*self.alpha_medio())/(pi/2)

    def cuerdaMaxima(self):
        return 2*self.__radio*sin(self.alpha_medio())

    def ensanche(self):
        pass

    def Peralte(self):
        pass

    def Resumen(self):
        return f"VP: {self.__vp} km/h\nA: {round(degrees(self.Alfa())*(10/9),4)}g\nR: {round(self.__radio,3)}m\nT: {round(self.Tangente(),3)}m\nS: {round(self.Secante(),3)}m\nDC: {round(self.desarrolloCurva(),3)}m\nC: {round(self.cuerdaMaxima(),3)}m"

    # -------------main------------------------

    def DmsLineaEntrada(self):
        distancia = self.__dm_inicial + \
            self.distancias_vertices()[0]-self.Tangente()
        dms = []
        try:
            for i in range(int(self.__dm_inicial), int(distancia), self.__intervalo_recto):
                dms.append(i)
            dms.pop(0)
            dms.insert(0, self.__dm_inicial)
            return dms
        except TypeError:
            pass

    def DmsCurva(self):
        distancia = self.__dm_inicial + \
            self.distancias_vertices()[0]-self.Tangente()
        dms = []
        try:
            for i in range(self.DmsLineaEntrada()[-1], int(distancia+self.desarrolloCurva()), self.__intervalo_curva):
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
            self.distancias_vertices()[0] - \
            self.Tangente()+self.desarrolloCurva()
        distanciaentrada = self.__dm_inicial + \
            self.distancias_vertices()[0]-self.Tangente()
        distancia = distanciaentrada + \
            self.desarrolloCurva() + \
            self.distancias_vertices()[1]-self.Tangente()
        dms = []
        try:
            for i in range(self.DmsCurva()[-2], int(distancia), self.__intervalo_recto):
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

    def coordenadasCurva(self):
        az1, az2, az3 = self.azimuts()
        del az2, az3
        coordenadaPrincipioCurva = ((self.__e1+(self.distancias_vertices()[0]-self.Tangente())*sin(
            az1)), (self.__n1+(self.distancias_vertices()[0]-self.Tangente())*cos(az1)))
        valor_a = []
        for i in self.DmsCurva():
            valor_a.append(i-self.DmsCurva()[0])
        delta = []
        for i in valor_a:
            delta.append(((pi/2)*i)/(pi*self.__radio))
        cuerdas_dh = []
        for i in delta:
            cuerdas_dh.append(2*self.__radio*sin(i))
        azimuts = []
        for i in delta:
            if self.curvaDerecha():
                azimuts.append(self.azimuts()[0]+i)
            else:
                azimuts.append(self.azimuts()[0]-i)
        coordenadas = []
        contador_dm_curva = 0
        contador_cuerdas_dh = 0
        contador_azimuts = 0
        while contador_dm_curva < len(self.DmsCurva()):
            coordenadas.append((round((coordenadaPrincipioCurva[0]+(cuerdas_dh[contador_cuerdas_dh]*sin(azimuts[contador_azimuts]))), 3), (round(
                coordenadaPrincipioCurva[1]+(cuerdas_dh[contador_cuerdas_dh]*cos(azimuts[contador_azimuts])), 3))))
            contador_dm_curva += 1
            contador_cuerdas_dh += 1
            contador_azimuts += 1
        return coordenadas

    def coordenadasSalida(self):
        az1, az2, az3 = self.azimuts()
        coordenadaFc = self.coordenadasCurva()[-1]
        del az1, az3
        dh = []
        coordenadas = []
        for i in self.DmsLineaSalida():
            dh.append(i-self.DmsCurva()[-1])
        for i in dh:
            coordenadas.append((
                (round(coordenadaFc[0]+i*sin(az2), 3)), (round(coordenadaFc[1]+i*cos(az2), 3))))
        return coordenadas

    def exportaExcel(self, directorio):
        nuevoArchivo = xlwt.Workbook()
        hoja = nuevoArchivo.add_sheet(self.__project_name)
        hoja.write(0, 0, "Desc")
        hoja.write(0, 1, "Dm")
        hoja.write(0, 2, "Este")
        hoja.write(0, 3, "Norte")

        hoja.write(0, 5, "VP")
        hoja.write(1, 5, "A")
        hoja.write(2, 5, "R")
        hoja.write(3, 5, "T")
        hoja.write(4, 5, "S")
        hoja.write(5, 5, "DC")

        hoja.write(0, 6, f"{self.__vp}km/hr")
        hoja.write(1, 6, f"{round(degrees(self.Alfa())*(10/9),4)}g")
        hoja.write(2, 6, f"{round(self.__radio,3)}m")
        hoja.write(3, 6, f"{round(self.Tangente(),3)}m")
        hoja.write(4, 6, f"{round(self.Secante(),3)}m")
        hoja.write(5, 6, f"{round(self.desarrolloCurva(),3)}m")

        hoja.write(len(self.DmsLineaEntrada())+1, 0, "PC")
        hoja.write(len(self.DmsLineaEntrada())+len(self.DmsCurva()), 0, "FC")

        contador = 1
        for i in self.DmsLineaEntrada():
            hoja.write(contador, 1, i)
            contador += 1
        contador = 1+len(self.DmsLineaEntrada())
        for i in self.DmsCurva():
            hoja.write(contador, 1, i)
            contador += 1
        contador = 1+len(self.DmsLineaEntrada())+len(self.DmsCurva())
        for i in self.DmsLineaSalida():
            hoja.write(contador, 1, i)
            contador += 1

        contador = 1
        for i in self.coordenadasEntrada():
            hoja.write(contador, 2, i[0])
            hoja.write(contador, 3, i[1])
            contador += 1
        contador = 1+len(self.coordenadasEntrada())
        for i in self.coordenadasCurva():
            hoja.write(contador, 2, i[0])
            hoja.write(contador, 3, i[1])
            contador += 1
        contador = 1+len(self.coordenadasEntrada()) + \
            len(self.coordenadasCurva())
        for i in self.coordenadasSalida():
            hoja.write(contador, 2, i[0])
            hoja.write(contador, 3, i[1])
            contador += 1

        nuevoArchivo.save(directorio)


curva = Curva(1, "Linares", ((43.595, 448.897), (191.724, 404.958),
                             (314.465, 358.866)), 3000, 10, 1, 51.32, 30)

curva.exportaExcel("C:/Users/julio/Desktop/Proyecto/prueba2.xls")

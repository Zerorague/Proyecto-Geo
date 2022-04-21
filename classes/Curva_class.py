
from user_class import User, usuario
from math import sqrt, atan, tan, sin, degrees, cos, acos, pi


class Curva():
    def __init__(self, id, project_name, vertices, radio=200) -> None:
        self.__id = id
        self.__project_name = project_name
        self.__vertices = vertices
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
    def Get_vertices(self):
        # count = 1
        # for i in self.__vertices:
        #     print(f"V{count}= ESTE: {i[0]} NORTE: {i[1]}")
        #     count += 1
        return self.__vertices

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
                        return "Esperaba numeros"

    @Get_radio.setter
    def Set_radio(self, valor):
        if type(valor) == float and valor > 0:
            self.__radio = valor
        else:
            return "radio debe ser mayor a cero"

# --------------------elementos geometricos-----------------------

    def distancias_vertices(self):
        distancia_v_1_2 = sqrt(self.__DeltaEste1**2+self.__DeltaNorte1**2)
        distancia_v_2_3 = sqrt(self.__DeltaEste2**2+self.__DeltaNorte2**2)
        distancia_v_1_3 = sqrt(self.__DeltaEste3**2+self.__DeltaNorte3**2)
        return (distancia_v_1_2, distancia_v_2_3, distancia_v_1_3)

    def azimuts(self):
        try:
            if self.__DeltaEste1 > 0 and self.__DeltaNorte1 > 0:
                az1 = atan(self.__DeltaEste1/self.__DeltaNorte1)
            elif self.__DeltaEste1 > 0 and self.__DeltaNorte1 < 0:
                az1 = pi + atan(self.__DeltaEste1/self.__DeltaNorte1)
            elif self.__DeltaEste1 < 0 and self.__DeltaNorte1 < 0:
                az1 = pi + atan(self.__DeltaEste1/self.__DeltaNorte1)
            else:
                az1 = 2*pi + atan(self.__DeltaEste1/self.__DeltaNorte1)

            if self.__DeltaEste2 > 0 and self.__DeltaNorte2 > 0:
                az2 = atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 > 0 and self.__DeltaNorte2 < 0:
                az2 = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            elif self.__DeltaEste2 < 0 and self.__DeltaNorte2 < 0:
                az2 = pi + atan(self.__DeltaEste2/self.__DeltaNorte2)
            else:
                az2 = 2*pi + atan(self.__DeltaEste2/self.__DeltaNorte2)

            if self.__DeltaEste3 > 0 and self.__DeltaNorte3 > 0:
                az3 = atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 > 0 and self.__DeltaNorte3 < 0:
                az3 = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            elif self.__DeltaEste3 < 0 and self.__DeltaNorte3 < 0:
                az3 = pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
            else:
                az3 = 2*pi + atan(self.__DeltaEste3/self.__DeltaNorte3)
        except ZeroDivisionError:
            return "Ha ocurridio una division por 0"

        return (az1, az2, az3)

    def Alfa(self):
        distancia_1_2, distancia_2_3, distancia_1_3 = self.distancias_vertices()
        return 2*pi-(acos((distancia_1_2**2+distancia_2_3**2-(distancia_1_3**2))/(2*distancia_1_2*distancia_2_3)))

    def alpha_medio(self):
        try:
            az1, az2, az3 = self.azimuts()
            if az1 > az2:
                return (az1-az2)/2
            return(az2-az1)/2
        except ValueError:
            pass

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

    # -------------main------------------------


curva = Curva(1, "Linares", ((1000, 1000), (1500, 1600), (900, 2600)), 3000)
print(curva.Get_project_name)
print(curva.distancias_vertices())
print(curva.azimuts())
print(curva.Tangente())
print(curva.Secante())
print(curva.desarrolloCurva())
print(curva.cuerdaMaxima())
print(degrees(curva.alpha_medio()))
print(degrees(curva.Alfa()))

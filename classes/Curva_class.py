
from ctypes import alignment
from doctest import master

from pyparsing import col
from user_class import User, usuario
from math import radians, sqrt, atan, tan, sin, degrees, cos, acos, pi
import xlwt
from tkinter import CENTER, W, Canvas, Tk, Label, Entry, Button, filedialog, Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --------------------elementos geometricos-----------------------


def distancias_vertices():
    DeltaEste1 = float(entryV2_este.get())-float(entryV1_este.get())
    DeltaEste2 = float(entryV3_este.get())-float(entryV2_este.get())
    DeltaEste3 = float(entryV3_este.get())-float(entryV1_este.get())

    DeltaNorte1 = float(entryV2_norte.get())-float(entryV1_norte.get())
    DeltaNorte2 = float(entryV3_norte.get())-float(entryV2_norte.get())
    DeltaNorte3 = float(entryV3_norte.get())-float(entryV1_norte.get())

    distancia_v_1_2 = sqrt(DeltaEste1**2+DeltaNorte1**2)
    distancia_v_2_3 = sqrt(DeltaEste2**2+DeltaNorte2**2)
    distancia_v_1_3 = sqrt(DeltaEste3**2+DeltaNorte3**2)
    return (distancia_v_1_2, distancia_v_2_3, distancia_v_1_3)


def azimuts():
    DeltaEste1 = float(entryV2_este.get())-float(entryV1_este.get())
    DeltaEste2 = float(entryV3_este.get())-float(entryV2_este.get())
    DeltaEste3 = float(entryV3_este.get())-float(entryV1_este.get())

    DeltaNorte1 = float(entryV2_norte.get())-float(entryV1_norte.get())
    DeltaNorte2 = float(entryV3_norte.get())-float(entryV2_norte.get())
    DeltaNorte3 = float(entryV3_norte.get())-float(entryV1_norte.get())

    try:
        if DeltaEste1 > 0 and DeltaNorte1 > 0:
            azimutOne = atan(DeltaEste1/DeltaNorte1)
        elif DeltaEste1 > 0 and DeltaNorte1 < 0:
            azimutOne = pi + atan(DeltaEste1/DeltaNorte1)
        elif DeltaEste1 < 0 and DeltaNorte1 < 0:
            azimutOne = pi + atan(DeltaEste1/DeltaNorte1)
        elif DeltaEste1 < 0 and DeltaNorte1 > 0:
            azimutOne = 2*pi + atan(DeltaEste1/DeltaNorte1)

        if DeltaEste2 > 0 and DeltaNorte2 > 0:
            azimutTwo = atan(DeltaEste2/DeltaNorte2)
        elif DeltaEste2 > 0 and DeltaNorte2 < 0:
            azimutTwo = pi + atan(DeltaEste2/DeltaNorte2)
        elif DeltaEste2 < 0 and DeltaNorte2 < 0:
            azimutTwo = pi + atan(DeltaEste2/DeltaNorte2)
        elif DeltaEste2 < 0 and DeltaNorte2 > 0:
            azimutTwo = 2*pi + atan(DeltaEste2/DeltaNorte2)

        if DeltaEste3 > 0 and DeltaNorte3 > 0:
            azimuthThree = atan(DeltaEste3/DeltaNorte3)
        elif DeltaEste3 > 0 and DeltaNorte3 < 0:
            azimuthThree = pi + atan(DeltaEste3/DeltaNorte3)
        elif DeltaEste3 < 0 and DeltaNorte3 < 0:
            azimuthThree = pi + atan(DeltaEste3/DeltaNorte3)
        elif DeltaEste3 < 0 and DeltaNorte3 > 0:
            azimuthThree = (
                2*pi + atan(DeltaEste3/DeltaNorte3))
    except ZeroDivisionError:
        return "Ha ocurridio una division por 0"

    return (azimutOne, azimutTwo, azimuthThree)


def curvaDerecha():
    az1, az2, az3 = azimuts()
    del az3
    if az1 > pi and az2 < pi/2:
        az2 = 2*pi + az2
    elif az1 < pi/2 and az2 > pi:
        az1 = 2*pi + az1

    if az1 < az2:
        return True
    return False


def alpha_medio():
    try:
        azimutOne, azimutTwo, azimuthThree = azimuts()
        del azimuthThree
        if azimutOne > azimutTwo:
            return (azimutOne-azimutTwo)/2
        else:
            return (azimutTwo-azimutOne)/2
    except ValueError:
        pass


def Alfa():

    if curvaDerecha():
        return pi+(alpha_medio()*2)
    else:
        return pi-(alpha_medio()*2)


def Tangente():
    radio = float(entryRadio.get())
    try:
        return(radio*tan(alpha_medio()))
    except TypeError:
        pass


def Secante():
    radio = float(entryRadio.get())
    return radio*((1/cos(alpha_medio()))-1)


def desarrolloCurva():
    radio = float(entryRadio.get())
    return (pi*radio*alpha_medio())/(pi/2)


def cuerdaMaxima():
    radio = float(entryRadio.get())
    return 2*radio*sin(alpha_medio())


def ensanche():
    pass


def Peralte():
    pass


def Resumen():
    vp = float(entryVP.get())
    radio = float(entryRadio.get())
    return f"VP: {vp} km/h\nA: {round(degrees(Alfa())*(10/9),4)}g\nR: {round(radio,3)}m\nT: {round(Tangente(),3)}m\nS: {round(Secante(),3)}m\nDC: {round(desarrolloCurva(),3)}m\nC: {round(cuerdaMaxima(),3)}m"

# -------------main------------------------


def DmsLineaEntrada():
    dm_inicial = float(entryDmIni.get())
    intervalo_recto = int(entryIntervaloRecto.get())
    distancia = dm_inicial + \
        distancias_vertices()[0]-Tangente()
    dms = []
    try:
        for i in range(int(dm_inicial), int(distancia), intervalo_recto):
            dms.append(i)
        dms.pop(0)
        dms.insert(0, dm_inicial)
        return dms
    except TypeError:
        pass


def DmsCurva():
    dm_inicial = float(entryDmIni.get())
    intervalo_curva = int(entryIntervaloCurva.get())

    distancia = dm_inicial + \
        distancias_vertices()[0]-Tangente()
    dms = []
    try:
        for i in range(DmsLineaEntrada()[-1], int(distancia+desarrolloCurva()), intervalo_curva):
            if i > distancia:
                dms.append(i)
            else:
                continue
        dms.insert(0, distancia)
        dms.append(distancia+desarrolloCurva())
        return dms
    except TypeError:
        pass


def DmsLineaSalida():
    dm_inicial = float(entryDmIni.get())
    intervalo_recto = int(entryIntervaloRecto.get())
    distanciaFc = dm_inicial + \
        distancias_vertices()[0] - \
        Tangente()+desarrolloCurva()
    distanciaentrada = dm_inicial + \
        distancias_vertices()[0]-Tangente()
    distancia = distanciaentrada + \
        desarrolloCurva() + \
        distancias_vertices()[1]-Tangente()
    dms = []
    try:
        for i in range(DmsLineaEntrada()[-1], int(distancia), intervalo_recto):
            if i > distanciaFc:
                dms.append(i)
        dms.append(distancia)
        return dms
    except TypeError:
        pass


def coordenadasEntrada():
    dm_inicial = float(entryDmIni.get())
    e1 = float(entryV1_este.get())
    n1 = float(entryV1_norte.get())
    az1, az2, az3 = azimuts()
    del az2, az3
    dh = []
    coordenadas = []
    for i in DmsLineaEntrada():
        dh.append(i-dm_inicial)
    for i in dh:
        coordenadas.append(
            (round(e1+i*sin(az1), 3), round(n1 + i*cos(az1), 3)))
    return coordenadas


def coordenadasCurva():
    radio = float(entryRadio.get())
    e1 = float(entryV1_este.get())
    n1 = float(entryV1_norte.get())
    az1, az2, az3 = azimuts()
    del az2, az3
    coordenadaPrincipioCurva = ((e1+(distancias_vertices()[0]-Tangente())*sin(
        az1)), (n1+(distancias_vertices()[0]-Tangente())*cos(az1)))
    valor_a = []
    for i in DmsCurva():
        valor_a.append(i-DmsCurva()[0])
    delta = []
    for i in valor_a:
        delta.append(((pi/2)*i)/(pi*radio))
    cuerdas_dh = []
    for i in delta:
        cuerdas_dh.append(2*radio*sin(i))
    azimutes = []
    for i in delta:
        if curvaDerecha():
            azimutes.append(azimuts()[0]+i)
        else:
            azimutes.append(azimuts()[0]-i)
    coordenadas = []
    contador_dm_curva = 0
    contador_cuerdas_dh = 0
    contador_azimuts = 0
    while contador_dm_curva < len(DmsCurva()):
        coordenadas.append((round((coordenadaPrincipioCurva[0]+(cuerdas_dh[contador_cuerdas_dh]*sin(azimutes[contador_azimuts]))), 3), (round(
            coordenadaPrincipioCurva[1]+(cuerdas_dh[contador_cuerdas_dh]*cos(azimutes[contador_azimuts])), 3))))
        contador_dm_curva += 1
        contador_cuerdas_dh += 1
        contador_azimuts += 1
    return coordenadas


def coordenadasSalida():
    az1, az2, az3 = azimuts()
    coordenadaFc = coordenadasCurva()[-1]
    del az1, az3
    dh = []
    coordenadas = []
    for i in DmsLineaSalida():
        dh.append(i-DmsCurva()[-1])
    for i in dh:
        coordenadas.append((
            (round(coordenadaFc[0]+i*sin(az2), 3)), (round(coordenadaFc[1]+i*cos(az2), 3))))
    return coordenadas


def exportaExcel():
    project_name = str(entryProyecto.get())
    vp = float(entryVP.get())
    radio = entryRadio.get()
    radio = float(radio)
    nuevoArchivo = xlwt.Workbook()
    hoja = nuevoArchivo.add_sheet(project_name)
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

    hoja.write(0, 6, f"{vp}km/hr")
    hoja.write(1, 6, f"{round(degrees(Alfa())*(10/9),4)}g")
    hoja.write(2, 6, f"{round(radio,3)}m")
    hoja.write(3, 6, f"{round(Tangente(),3)}m")
    hoja.write(4, 6, f"{round(Secante(),3)}m")
    hoja.write(5, 6, f"{round(desarrolloCurva(),3)}m")

    hoja.write(len(DmsLineaEntrada())+1, 0, "PC")
    hoja.write(len(DmsLineaEntrada())+len(DmsCurva()), 0, "FC")

    contador = 1
    for i in DmsLineaEntrada():
        hoja.write(contador, 1, i)
        contador += 1
    contador = 1+len(DmsLineaEntrada())
    for i in DmsCurva():
        hoja.write(contador, 1, i)
        contador += 1
    contador = 1+len(DmsLineaEntrada())+len(DmsCurva())
    for i in DmsLineaSalida():
        hoja.write(contador, 1, i)
        contador += 1

    contador = 1
    for i in coordenadasEntrada():
        hoja.write(contador, 2, i[0])
        hoja.write(contador, 3, i[1])
        contador += 1
    contador = 1+len(coordenadasEntrada())
    for i in coordenadasCurva():
        hoja.write(contador, 2, i[0])
        hoja.write(contador, 3, i[1])
        contador += 1
    contador = 1+len(coordenadasEntrada()) + \
        len(coordenadasCurva())
    for i in coordenadasSalida():
        hoja.write(contador, 2, i[0])
        hoja.write(contador, 3, i[1])
        contador += 1

    nuevoArchivo.save(f"{project_name}.xlsx")


# ----------------------------interfaz--------------------------------------------
raiz = Tk()


def estes():
    x = []
    for i in coordenadasEntrada():
        x.append(i[0])
    for i in coordenadasCurva():
        x.append(i[0])
    for i in coordenadasSalida():
        x.append(i[0])
    return x


def nortes():
    y = []
    for i in coordenadasEntrada():
        y.append(i[1])
    for i in coordenadasCurva():
        y.append(i[1])
    for i in coordenadasSalida():
        y.append(i[1])
    return y


raiz.title("CCAz")
raiz.geometry("1000x750")
raiz.resizable(0, 0)
raiz.config(background="white")

labelGrafico = Label(raiz, text="Grafico", width="10", height="2")
labelGrafico.grid(row=0, column=2, pady=5, padx=10)

frame_grafica = Frame(raiz, bg="black")
frame_grafica.grid(row=1, column=2, sticky="nesw",
                   rowspan=11, padx=20, pady=10)
frame_grafica.config(width=500, height=500)


labelProyecto = Label(raiz, text="Proyecto", width="10", height="2")
labelProyecto.grid(row=0, column=0, pady=5, padx=10)

labelVertice1 = Label(raiz, text="E\nN\nV1", width="10", height="5")
labelVertice1.grid(row=1, column=0, rowspan=2, pady=10, padx=10)

labelVertice2 = Label(raiz, text="E\nN\nV2", width="10", height="5")
labelVertice2.grid(row=3, column=0, rowspan=2, pady=10, padx=10)

labelVertice3 = Label(raiz, text="E\nN\nV3", width="10", height="5")
labelVertice3.grid(row=5, column=0, rowspan=2, pady=10, padx=10)

labelRadio = Label(raiz, text="Radio", width="10", height="2")
labelRadio.grid(row=7, column=0, pady=10, padx=10)

labelIntervaloRecto = Label(
    raiz, text="Inter recto", width="10", height="2")
labelIntervaloRecto.grid(row=8, column=0, pady=10, padx=10)

labelIntervaloCurva = Label(
    raiz, text="Inter curva", width="10", height="2")
labelIntervaloCurva.grid(row=9, column=0, pady=10, padx=10)

labelVp = Label(raiz, text="Vp", width="10", height="2")
labelVp.grid(row=10, column=0, pady=10, padx=10)

labelDmIni = Label(raiz, text="Dm Ini", width="10", height="2")
labelDmIni.grid(row=11, column=0, pady=10, padx=10)

entryProyecto = Entry(raiz, background="white")
entryProyecto.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
entryProyecto.config(width="50")

entryV1_este = Entry(raiz, background="white")
entryV1_este.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)
entryV1_este.config(width="50")

entryV1_norte = Entry(raiz, background="white")
entryV1_norte.grid(row=2, column=1, sticky="nsew", pady=10, padx=10)
entryV1_norte.config(width="50")

entryV2_este = Entry(raiz, background="white")
entryV2_este.grid(row=3, column=1, sticky="nsew", pady=10, padx=10)
entryV2_este.config(width="50")

entryV2_norte = Entry(raiz, background="white")
entryV2_norte.grid(row=4, column=1, sticky="nsew", pady=10, padx=10)
entryV2_norte.config(width="50")

entryV3_este = Entry(raiz, background="white")
entryV3_este.grid(row=5, column=1, sticky="nsew", pady=10, padx=10)
entryV3_este.config(width="50")

entryV3_norte = Entry(raiz, background="white")
entryV3_norte.grid(row=6, column=1, sticky="nsew", pady=10, padx=10)
entryV3_norte.config(width="50")

entryRadio = Entry(raiz, background="white")
entryRadio.grid(row=7, column=1, sticky="nsew", pady=10, padx=10)
entryRadio.config(width="50")

entryIntervaloRecto = Entry(raiz, background="white")
entryIntervaloRecto.grid(
    row=8, column=1, sticky="nsew", pady=10, padx=10)
entryIntervaloRecto.config(width="50")

entryIntervaloCurva = Entry(raiz, background="white")
entryIntervaloCurva.grid(
    row=9, column=1, sticky="nsew", pady=10, padx=10)
entryIntervaloCurva.config(width="50")

entryVP = Entry(raiz, background="white")
entryVP.grid(row=10, column=1, sticky="nsew", pady=10, padx=10)
entryVP.config(width="50")

entryDmIni = Entry(raiz, background="white")
entryDmIni.grid(row=11, column=1, sticky="nsew", pady=10, padx=10)
entryDmIni.config(width="50")

botonExportExcel = Button(raiz, text="ExportExcel",
                          command=exportaExcel)
botonExportExcel.grid(row=12, column=0, pady=15,
                      padx=10, columnspan=2, sticky="ns")
botonExportExcel.config(width=20)


def graficar():
    fig, axs = plt.subplots(dpi=80, figsize=(
        6, 8), sharey=True, facecolor='white')
    axs.plot(estes(), nortes())
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=1)


botonGraficar = Button(raiz, text="Graficar",
                       command=graficar)
botonGraficar.grid(row=12, column=2, pady=15,
                   padx=10, columnspan=2, sticky="ns")
botonGraficar.config(width=20)

raiz.mainloop()

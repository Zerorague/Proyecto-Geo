print("Guia diagrama de peraltes")

ancho_calzada=float(input("ingrese ancho calzada: "))
numero_de_pistas=float(input("ingrese numero de pistas: "))
variacion_peralte=float(input("ingrese variacion de peralte%: "))
bombeo=float(input("ingrese bombeo%: "))
tasa_giro=float(input("ingrese tasa de giro: "))
distancia=((ancho_calzada*numero_de_pistas*variacion_peralte)/tasa_giro)

def puntos_singulares(ancho_calzada,numero_de_pistas,variacion_peralte,tasa_giro,distancia,bombeo):

	print("Lb: ",(ancho_calzada*numero_de_pistas*bombeo)/tasa_giro)
	print("Lc: ",(ancho_calzada*numero_de_pistas*bombeo*2)/tasa_giro)
	print("L70: ",((ancho_calzada*numero_de_pistas*bombeo)/tasa_giro)+(ancho_calzada*numero_de_pistas*((variacion_peralte-bombeo)*0.7))/tasa_giro)
	print("Ld: ",distancia)

puntos_singulares(ancho_calzada,numero_de_pistas,variacion_peralte,tasa_giro,distancia,bombeo)

Enter=input("Presione enter para salir")

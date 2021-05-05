from decimal import Decimal, ROUND_HALF_UP
import random
def montecarlo(n,
            probabilidad_venta_mujer,
            probabilidad_venta_hombre,
            probabilidad_1_subscripcion_mujer,
            probabilidad_2_subscripcion_mujer,
            probabilidad_3_subscripcion_mujer,
            probabilidad_4_subscripcion_mujer,
            probabilidad_1_subscripcion_hombre,
            probabilidad_2_subscripcion_hombre,
            probabilidad_3_subscripcion_hombre,
            probabilidad_4_subscripcion_hombre,
            probabilidad_puerta,
            probabilidad_puerta_mujer,
            probabilidad_puerta_hombre,
            utilidad_vendedor):
    intervalo_puerta_hombre = probabilidad_puerta * probabilidad_puerta_hombre
    intervalo_puerta_mujer = intervalo_puerta_hombre + (probabilidad_puerta * probabilidad_puerta_mujer)
    response = []
    utilidad_total = 0
    subscripcion_total = 0
    subscripcion_count = 0
    for i in range(0,n):
        probabilidad_venta = ["-",0]
        hombre = False
        utilidad = 0
        probabilidad_puerta = 0
        probabilidad_subscripcion = ["-",0]
        probabilidad_puerta = random.uniform(0, 1)
        if probabilidad_puerta <= intervalo_puerta_hombre:
            hombre = True
            probabilidad_venta = venta(probabilidad_venta_hombre)
            if probabilidad_venta[1] != 0:
                probabilidad_subscripcion = subscripcion(probabilidad_1_subscripcion_hombre, probabilidad_2_subscripcion_hombre, probabilidad_3_subscripcion_hombre, probabilidad_4_subscripcion_hombre)
        elif probabilidad_puerta <= intervalo_puerta_mujer:
            probabilidad_venta = venta(probabilidad_venta_mujer)
            if probabilidad_venta[1] != 0:
                probabilidad_subscripcion = subscripcion(probabilidad_1_subscripcion_mujer, probabilidad_2_subscripcion_mujer, probabilidad_3_subscripcion_mujer, probabilidad_4_subscripcion_mujer)

        aux_venta_hombre = "-"
        aux_venta_mujer = "-"
        if hombre:
            aux_venta_hombre = probabilidad_venta[0]
        else:
            aux_venta_mujer = probabilidad_venta[0]
        utilidad = probabilidad_subscripcion[1] * utilidad_vendedor
        utilidad_total += utilidad
        aux_subscripcion_hombre = ["-","-","-","-"]
        aux_subscripcion_mujer = ["-","-","-","-"]
        for j in range(0, 4):
            if hombre == True and (probabilidad_subscripcion[1] == j+1):
                aux_subscripcion_hombre[j] = probabilidad_subscripcion[0]
                subscripcion_count += 1
            elif hombre == False and (probabilidad_subscripcion[1] == j+1):
                aux_subscripcion_mujer[j] = probabilidad_subscripcion[0]
                subscripcion_count += 1
        subscripcion_total += probabilidad_subscripcion[1]
        prob_subscripcion = (subscripcion_total / (i+1))  * 100 
        prob_venta = (subscripcion_count / (i+1)) * 100 
        response.append([i+1, probabilidad_puerta,  aux_venta_hombre, aux_venta_mujer, aux_subscripcion_hombre[0], aux_subscripcion_hombre[1], aux_subscripcion_hombre[2], aux_subscripcion_hombre[3], aux_subscripcion_mujer[0], aux_subscripcion_mujer[1], aux_subscripcion_mujer[2], aux_subscripcion_mujer[3],  utilidad, utilidad_total, subscripcion_total, prob_venta, prob_subscripcion])
    return response

def venta(prob):
    probabilidad_venta = random.uniform(0, 1)
    if probabilidad_venta <= prob:
        return [probabilidad_venta, 1]
    else:
        return [probabilidad_venta, 0]

def subscripcion(prob1, prob2, prob3, prob4):
    probabilidad_subscripcion = random.uniform(0, 1)
    intervalo_1 = round(prob1,4)
    intervalo_2 = round(intervalo_1 + prob2,4)
    intervalo_3 = round(intervalo_2 + prob3,4)
    intervalo_4 = round(intervalo_3 + prob4,4)
    
    if probabilidad_subscripcion <= intervalo_1:
        return [probabilidad_subscripcion, 1]
    if probabilidad_subscripcion <= intervalo_2:
        return [probabilidad_subscripcion, 2]
    if probabilidad_subscripcion <= intervalo_3:
        return [probabilidad_subscripcion, 3]
    if probabilidad_subscripcion <= intervalo_4:
        return [probabilidad_subscripcion, 4]
    else:
        return [probabilidad_subscripcion, 0]

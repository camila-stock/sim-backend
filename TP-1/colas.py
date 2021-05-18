## aprendiz demora U(20;30) - atiende 15% - cobra 300
## veterano A demora U(11;13) - atiene 45% - cobra 500
## veterano B demora U(12;18) - atiende 40% - cobra 500
##
## los clientes llegan  U(2;12)
## a los 30' de espera, se van.

import random

def colasPeluqueria(n, tiempo, iteraciones, hora_desde, hora_hasta):
    evento_anterior_llegada_cliente = Evento("-", 0, 0)
    demora_actual_aprendiz = Evento("-", 0, 0)
    demora_actual_veteranoA = Evento("-", 0, 0)
    demora_actual_veteranoB = Evento("-", 0, 0)
    peluqueroA = Peluquero(0, 0, 0)
    peluqueroVa = Peluquero(0, 0, 0)
    peluqueroVb = Peluquero(0, 0, 0)

    fila_anterior = Fila(0, evento_anterior_llegada_cliente, demora_actual_aprendiz, demora_actual_veteranoA,
                         demora_actual_veteranoB, 0, peluqueroA, peluqueroVa, peluqueroVb)


    if tiempo > fila_anterior.reloj:

        fila_actual = Fila()

        rnd_atenc = random.uniform(0, 1)
        llega_cliente = calcularUniformeLlegadaCliente(rnd_atenc)
        atencion = calcularAtencion(llega_cliente)

        prox_lc = llega_cliente + evento_anterior_llegada_cliente.tiempo_demora
        demora_actual_llegada_cliente = Evento(rnd_atenc, llega_cliente, prox_lc)

        if atencion == "a":
            if fila_anterior.peluqueroA.estado == 0:
                peluqueroA = Peluquero(1, 0, 0)

                a = random.uniform(0, 1)
                unif_a = calcularUniformeVeteranoA(a)
                prox_a = unif_a + demora_actual_aprendiz.tiempo_demora
                demora_actual_aprendiz = Evento(a, unif_a, prox_a)

                fila_actual.demoraA = demora_actual_aprendiz
                fila_actual.peluqueroA = peluqueroA

            ##El resto de los Peluqueros santis, estan al pedo son ñoquis.

        elif atencion == "va":
            if fila_anterior.peluqueroVa.estado == 0:
                peluqueroVa = Peluquero(1, 0)

                va = random.uniform(0, 1)
                unif_va = calcularUniformeVeteranoA(va)
                prox_va = unif_va + demora_actual_veteranoA.tiempo_demora
                demora_actual_veteranoA = Evento(va, unif_va, prox_va)

                fila_actual.demoraVa = demora_actual_veteranoA
                fila_actual.peluqueroVa = peluqueroVa

        elif atencion == "vb":
            if fila_anterior.peluqueroVb.estado == 0:
                peluqueroVb = Peluquero(1, 0)

                vb = random.uniform(0, 1)
                unif_vb = calcularUniformeVeteranoB(vb)
                prox_vb = unif_vb + demora_actual_veteranoB.tiempo_demora
                demora_actual_veteranoB = Evento(vb, unif_vb, prox_vb)

                fila_actual.demoraVb = demora_actual_veteranoB
                fila_actual.peluqueroVb = peluqueroVb

        tiempos = [demora_actual_aprendiz.tiempo_demora, demora_actual_veteranoA.tiempo_demora, demora_actual_veteranoB.tiempo_demora]
        tiempos.sort(False)

        fila_actual.reloj = tiempos.pop()
        fila_actual.demoraLc = demora_actual_llegada_cliente
        fila_actual.demoraA = demora_actual_aprendiz
        fila_actual.demoraVa = demora_actual_veteranoA
        fila_actual.demoraVb = demora_actual_veteranoB
        fila_actual.cantidad_atendidos = 0
        fila_actual.cantidad_perdidos = 0

    return fila_actual


def calcularUniformeAbrendiz(rnd):
    return 20 + (rnd * (30 - 20))

def calcularUniformeVeteranoA(rnd):
    return 11 + (rnd * (13 - 11))

def calcularUniformeVeteranoB(rnd):
    return 12 + (rnd * (18 - 12))

def calcularUniformeLlegadaCliente(rnd):
    return 2 + (rnd * (12 - 2))

def calcularAtencion(rnd):
    if rnd < 0.15:
        return "a"
    elif rnd < 0.45:
        return "va"
    else:
        return "vb"



class Fila:
    def __init__(self, reloj, demoraLc, demoraA, demoraVa, demoraVb, cantidad_atendidos, cantidad_perdidos,
                  peluqueroA, peluqueroVa, peluqueroVb):
        self.reloj = reloj
        self.demoraLc = demoraLc
        self.demoraA = demoraA
        self.demoraVa = demoraVa
        self.demoraVb = demoraVb
        self.cantidad_atendidos = cantidad_atendidos
        self.cantidad_perdidos = cantidad_perdidos
        self.peluqueroA = peluqueroA
        self.peluqueroVa = peluqueroVa
        self.peluqueroVb = peluqueroVb



## Evento - Llegada cliente
##        - fin atención aprendiz
##        - fin atención veterano A
##        - fin atención veterano B

class Evento:
    def __init__(self, rnd, tiempo_demora, proximo):
        self.rnd = rnd
        self.tiempo_demora = tiempo_demora
        self.proximo = proximo


##TODO
## Aprendiz + 2 veteranos
class Peluquero:
    def __init__(self, estado, cola, utilidad):
        self.estado = estado
        self.cola = cola
        self.utilidad = utilidad



class Cliente:
    def __init__(self, estado, cola):
        self.estado = estado
        self.cola = cola

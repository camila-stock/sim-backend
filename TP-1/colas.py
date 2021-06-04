## aprendiz demora U(20;30) - atiende 15% - cobra 300
## veterano A demora U(11;13) - atiene 45% - cobra 500
## veterano B demora U(12;18) - atiende 40% - cobra 500
##
## los clientes llegan  U(2;12)
## a los 30' de espera, se van.

import random
import file_writer as w

contador_cliente = 0
peluqueroA = None
peluqueroVa = None
peluqueroVb = None
eventos = []
clientes = []
reloj = 0
tiempo_maximo = 0
fila_actual = None
fila_anterior = None


def inicio_de_simulacion(hora_evento, horario_cierre):
    global contador_cliente
    global peluqueroA
    global peluqueroVa
    global peluqueroVb
    global eventos
    global tiempo_maximo
    global fila_anterior
    global fila_actual
    fila_anterior = Fila(None, None, None, None, None, None, None, None, None, None, None)
    fila_actual = Fila(None, None, None, None, None, None, None, None, None, None, None)
    tiempo_maximo = 60 * horario_cierre
    peluqueroA = Peluquero("a", "libre", [], 300, 0, "")
    peluqueroVa = Peluquero("va", "libre", [], 500, 0, "")
    peluqueroVb = Peluquero("vb", "libre", [], 500, 0, "")
    llegada_cliente_vacia = LlegadaCliente("", "", "")
    fin_atencion_vacio = FinDeAtencion("", "", "")
    evento_vacio = Evento("", "", "", "")

    rnd = random.uniform(0, 1)
    llegada_cliente = 2 + (rnd * (12 - 2))
    event = Evento("llegada_cliente", llegada_cliente, "", llegada_cliente)
    eventos.append(event)

    pre_header = ["reloj", "llegada_cliente", "", "", "peluquero", "","aprendiz", "", "", "", "veterano A", "", "", "",
                  "veterano B", "", "", "", "fin atencion aprendiz", "", "", "fin atencion veterano A", "", "",
                  "fin atencion veterano B", "", "", "Clientes"]
    header = ["reloj", "rnd", "tiempo entre llegadas", "próxima llegada", "rnd", "peluquero", "cola", "estado", "utilidad","utilidad acumulada","cola", "estado", "utilidad", "utilidad acumulada", "cola", "estado", "utilidad","utilidad acumulada", "rnd", "tiempo atencion", "fin atencion", "rnd", "tiempo atencion", "fin atencion","rnd", "tiempo atencion", "fin atencion", "estado", "hora_llegada"]

    headers = [pre_header, header]
    w.headers(headers)

    fila_anterior.fila_anterior = fila_anterior
    fila_anterior.reloj = 0
    fila_anterior.llegada_cliente = llegada_cliente_vacia
    fila_anterior.peluquero = [0, "-"]
    fila_anterior.peluqueroA = peluqueroA
    fila_anterior.peluqueroVa = peluqueroVa
    fila_anterior.peluqueroVb = peluqueroVb
    fila_anterior.fin_atencion_aprendiz = fin_atencion_vacio
    fila_anterior.fin_atencion_veterano_a = fin_atencion_vacio
    fila_anterior.fin_atencion_veterano_b = fin_atencion_vacio
    fila_anterior.clientes = []

    w.colas(fila_anterior)

    fila_actual.peluquero = [0, 0]
    fila_actual.peluqueroA = peluqueroA
    fila_actual.peluqueroVa = peluqueroVa
    fila_actual.peluqueroVb = peluqueroVb
    fila_actual.llegada_cliente = llegada_cliente_vacia
    fila_actual.fin_atencion_aprendiz = fin_atencion_vacio
    fila_actual.fin_atencion_veterano_a = fin_atencion_vacio
    fila_actual.fin_atencion_veterano_b = fin_atencion_vacio
    fila_actual.clientes = []


    while (len(eventos) != 0):
        ejecutarEvento(eventos)
        ordenarEventos()


def ordenarEventos():
    aux = None  ## TODO revisar
    global eventos
    global fila_actual
    global fila_anterior
    global clientes
    for i in range(0, len(eventos)):
        print(eventos[i])
        for j in range(0, len(eventos)):
            if eventos[i].tiempo < eventos[j].tiempo:
                aux = eventos[i]
                eventos[i] = eventos[j]
                eventos[j] = aux
    fila_actual.clientes = clientes
    fila_actual.fila_anterior = fila_anterior
    w.colas(fila_actual)
    fila_anterior = fila_actual


def ejecutarEvento(eventos):
    ##### Switch de evento
    global tiempo_maximo
    global reloj
    global fila_actual
    global clientes
    evento = eventos.pop(0)
    reloj = evento.tiempo

    fila_actual.reloj = reloj

    if evento.tipo_evento == "llegada_cliente":
        if evento.tiempo > tiempo_maximo:
            return
        atencion = calcularAtencion()
        fila_actual.peluquero[1] = atencion
        verQueMiercoleHacerConLaAtencionDelChango(atencion)

        rnd = random.uniform(0, 1)
        llegada_cliente = 2 + (rnd * (12 - 2))

        fila_actual.llegada_cliente = LlegadaCliente(rnd,llegada_cliente, llegada_cliente + reloj)

        event = Evento("llegada_cliente", llegada_cliente + reloj, "", llegada_cliente)
        eventos.append(event)

    elif evento.tipo_evento == "fin_de_atencion":
        for i in range(0, len(clientes)):
            if clientes[i].id == evento.data.cliente_atendido.id:
                clientes.pop(i)
                break
        if len(evento.data.cola) == 0:
            evento.data.estado = "libre"
        else:
            cliente_a_atender = evento.data.cola.pop(0)
            atender(evento.data, cliente_a_atender)
        evento.data.utilidad_acumulada += evento.data.utilidad

    elif evento.tipo_evento == "fin_espera_cliente":
        cliente = evento.data[0]
        peluquero = evento.data[1]
        for i in range(0, len(peluquero.cola)):
            if peluquero.cola[i] == cliente.id:
                peluquero.cola.pop(i)
        for i in range(0, len(clientes)):
            if clientes[i].id == cliente.id:
                clientes.pop(i)
                break


def calcularAtencion():
    global fila_actual

    rnd = random.uniform(0, 1)
    fila_actual.peluquero[0] = rnd

    if rnd < 0.15:
        return "a"
    elif rnd < 0.45:
        return "va"
    else:
        return "vb"


def atender(peluquero, cliente):
    global eventos
    global reloj
    global fila_actual
    global clientes

    if peluquero.estado == "libre":
        peluquero.estado = "ocupado"
        peluquero.cliente_atendido = cliente

        tiempo_atencion = 0
        if peluquero.id == "a":
            rnd = random.uniform(0, 1)
            tiempo_atencion = 20 + (rnd * (30 - 20))
            fila_actual.peluqueroA.estado = peluquero.estado
            fila_actual.peluqueroA.cola = peluquero.cola
            fila_actual.peluqueroA.utilidad = peluquero.utilidad
            fila_actual.peluqueroA.utilidad_acumulada = peluquero.utilidad_acumulada

            fila_actual.fin_atencion_aprendiz.rnd = rnd
            fila_actual.fin_atencion_aprendiz.tiempo_atencion = tiempo_atencion
            fila_actual.fin_atencion_aprendiz.fin_atencion = reloj + tiempo_atencion
        elif peluquero.id == "va":
            rnd = random.uniform(0, 1)
            tiempo_atencion = 11 + (rnd * (13 - 11))
            fila_actual.peluqueroVa.estado = peluquero.estado
            fila_actual.peluqueroVa.cola = peluquero.cola
            fila_actual.peluqueroVa.utilidad = peluquero.utilidad
            fila_actual.peluqueroVa.utilidad_acumulada = peluquero.utilidad_acumulada

            fila_actual.fin_atencion_veterano_a.rnd = rnd
            fila_actual.fin_atencion_veterano_a.tiempo_atencion = tiempo_atencion
            fila_actual.fin_atencion_veterano_a.fin_atencion = reloj + tiempo_atencion
        elif peluquero.id == "vb":
            rnd = random.uniform(0, 1)
            tiempo_atencion = 12 + (rnd * (18 - 12))
            fila_actual.peluqueroVb.estado = peluquero.estado
            fila_actual.peluqueroVb.cola = peluquero.cola
            fila_actual.peluqueroVb.utilidad = peluquero.utilidad
            fila_actual.peluqueroVb.utilidad_acumulada = peluquero.utilidad_acumulada

            fila_actual.fin_atencion_veterano_b.rnd = rnd
            fila_actual.fin_atencion_veterano_b.tiempo_atencion = tiempo_atencion
            fila_actual.fin_atencion_veterano_b.fin_atencion = reloj + tiempo_atencion

        eventos.append(Evento("fin_de_atencion", tiempo_atencion + reloj, peluquero, ""))

    elif peluquero.estado == "ocupado":
        aux = []
        for i in range(0, len(eventos)):
            if eventos[i].tipo_evento == "fin_espera_cliente" and eventos[i].data[0].id == cliente.id:
                aux.append(i)
        for j in range(0, len(aux)):
            for i in range(0, len(eventos)):
                if aux[j] == i:
                    eventos.pop(i)
        cliente.estado = "esperando"
        clientes[-1].estado = "esperando"
        peluquero.cola.append(cliente)
        tiempo_de_espera_max = reloj + 30

        eventos.append(Evento("fin_espera_cliente", tiempo_de_espera_max, [cliente, peluquero], ""))


def verQueMiercoleHacerConLaAtencionDelChango(atencion):
    global reloj
    global contador_cliente
    global peluqueroA
    global peluqueroVa
    global peluqueroVb

    contador_cliente += 1
    cliente = Cliente("Cliente " + str(contador_cliente), "siendo_atendido", reloj)
    clientes.append(cliente)

    if atencion == "a":
        peluquero = peluqueroA
    elif atencion == "va":
        peluquero = peluqueroVa
    elif atencion == "vb":
        peluquero = peluqueroVb

    atender(peluquero, cliente)


class Evento:
    def __init__(self, tipo_evento, tiempo, data, rnd):
        self.tipo_evento = tipo_evento
        self.tiempo = tiempo
        self.data = data
        self.rnd = rnd


class Peluquero:
    def __init__(self, id, estado, cola, utilidad, utilidad_acumulada, cliente_atendido):
        self.id = id
        self.estado = estado
        self.cola = cola
        self.utilidad = utilidad
        self.utilidad_acumulada = utilidad_acumulada
        self.cliente_atendido = cliente_atendido

class FinDeAtencion:
    def __init__(self, rnd, tiempo_atencion, fin_atencion):
        self.rnd = rnd
        self.tiempo_atencion = tiempo_atencion
        self.fin_atencion = fin_atencion

class LlegadaCliente:
    def __init__(self, rnd, tiempo_entre_llegadas, prox_llegada):
        self.rnd = rnd
        self.tiempo_entre_llegadas = tiempo_entre_llegadas
        self.prox_llegada = prox_llegada

class Cliente:
    def __init__(self, id, estado, hora_llegada):
        self.id = id
        self.estado = estado
        self.hora_llegada = hora_llegada


##TODO   imprimir en el excel toda la magia, modificar los parametros de inicio y arreglar el router
class Fila:
    def __init__(self, reloj, llegada_cliente, peluquero, peluqueroA, peluqueroVa, peluqueroVb, fin_atencion_aprendiz,
                 fin_atencion_veterano_a,
                 fin_atencion_veterano_b, clientes, fila_anterior):
        self.reloj = reloj
        self.llegada_cliente = llegada_cliente
        self.peluquero = peluquero
        self.peluqueroA = peluqueroA
        self.peluqueroVa = peluqueroVa
        self.peluqueroVb = peluqueroVb
        self.fin_atencion_aprendiz = fin_atencion_aprendiz
        self.fin_atencion_veterano_a = fin_atencion_veterano_a
        self.fin_atencion_veterano_b = fin_atencion_veterano_b
        self.clientes = clientes
        self.fila_anterior = fila_anterior

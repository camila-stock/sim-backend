## aprendiz demora U(20;30) - atiende 15% - cobra 300
## veterano A demora U(11;13) - atiene 45% - cobra 500
## veterano B demora U(12;18) - atiende 40% - cobra 500
##
## los clientes llegan  U(2;12)
## a los 30' de espera, se van.

import random

contador_cliente = 0
peluqueroA = None
peluqueroVa = None
peluqueroVb = None
eventos = []
reloj = 0
tiempo_maximo = 0

def inicio_de_simulacion(hora_evento, horario_cierre):
    global contador_cliente
    global peluqueroA
    global peluqueroVa
    global peluqueroVb
    global eventos
    global tiempo_maximo
    tiempo_maximo = 60 * horario_cierre
    peluqueroA = Peluquero("a", "libre", [], 300, 0, "-")
    peluqueroVa = Peluquero("va", "libre", [], 500, 0, "-")
    peluqueroVb = Peluquero("vb", "libre", [], 500, 0, "-")

    llegada_cliente = calcularUniformeLlegadaCliente()
    eventos.append(Evento("llegada_cliente", llegada_cliente))
    while (len(eventos) != 0):
        ejecutarEvento(eventos)
        ordenarEventos()

def ordenarEventos():
    aux = None
    global eventos
    for i in range(0, len(eventos)):
        for j in range(0, len(eventos)):
            if eventos[i].tiempo > eventos[j].tiempo:
                aux = eventos[i]
                eventos[i] = eventos[j]
                eventos[j] = aux



def ejecutarEvento(eventos):
    ##### Switch de evento
    global tiempo_maximo
    evento = eventos.pop(0)
    if evento.tipo_evento == "llegada_cliente":
        if evento.tiempo > tiempo_maximo:
            return
        atencion = calcularAtencion()
        verQueMiercoleHacerConLaAtencionDelChango(atencion)
        llegada_cliente = calcularUniformeLlegadaCliente()
        eventos.append(Evento("llegada_cliente", llegada_cliente, "-"))

    elif evento.tipo_evento == "fin_de_atencion":
        cliente_a_atender = evento.data.cola.pop(0)
        evento.data.utilidad_acumulada += evento.data.utilidad
        atender(evento.data, cliente_a_atender)

    elif evento.tipo_evento == "fin_espera_cliente":
        cliente = evento.data[0]
        peluquero = evento.data[1]
        for i in range(0, len(peluquero.cola)):
            if peluquero.cola[i] == cliente.id:
                peluquero.cola.pop(i)


def calcularUniformeAbrendiz():
    rnd = random.uniform(0, 1)
    return 20 + (rnd * (30 - 20))


def calcularUniformeVeteranoA():
    rnd = random.uniform(0, 1)
    return 11 + (rnd * (13 - 11))


def calcularUniformeVeteranoB():
    rnd = random.uniform(0, 1)
    return 12 + (rnd * (18 - 12))


def calcularUniformeLlegadaCliente():
    rnd = random.uniform(0, 1)
    return 2 + (rnd * (12 - 2))


def calcularAtencion():
    rnd = random.uniform(0, 1)
    if rnd < 0.15:
        return "a"
    elif rnd < 0.45:
        return "va"
    else:
        return "vb"


def atender(peluquero, cliente):
    global eventos
    global reloj

    if peluquero.estado == "libre":
        peluquero.estado = "ocupado"
        peluquero.cliente_atendido = cliente

        tiempo_atencion = 0
        if peluquero.id == "a":
            tiempo_atencion = calcularUniformeAbrendiz()
        elif peluquero.id == "va":
            tiempo_atencion = calcularUniformeVeteranoA()
        elif peluquero.id == "vb":
            tiempo_atencion = calcularUniformeVeteranoB()

        eventos.append(Evento("fin_de_atencion", tiempo_atencion, peluquero))

    elif peluquero.estado == "ocupado":
        for i in range(0, len(eventos)):
            if eventos[i].tipo_evento == "fin_espera_cliente" and eventos[i].data[0].id == cliente.id:
                eventos.pop(i)

        cliente.estado = "esperando"
        peluquero.cola.append(cliente)
        tiempo_de_espera_max = reloj + 30
        eventos.append(Evento("fin_espera_cliente", tiempo_de_espera_max, [cliente, peluquero]))


def verQueMiercoleHacerConLaAtencionDelChango(atencion):
    global reloj
    global contador_cliente
    global peluqueroA
    global peluqueroVa
    global peluqueroVb

    contador_cliente += 1
    cliente = Cliente(contador_cliente, "siendo_atendido", reloj)

    if atencion == "a":
        peluquero = peluqueroA
    elif atencion == "va":
        peluquero = peluqueroVa
    elif atencion == "vb":
        peluquero = peluqueroVb

    atender(peluquero, cliente)


class Evento:
    def __init__(self, tipo_evento, tiempo, data):
        self.tipo_evento = tipo_evento
        self.tiempo = tiempo
        self.data = data


class Peluquero:
    def __init__(self, id, estado, cola, utilidad, utilidad_acumulada, cliente_atendido):
        self.id = id
        self.estado = estado
        self.cola = cola
        self.utilidad = utilidad
        self.utilidad_acumulada = utilidad_acumulada
        self.cliente_atendido = cliente_atendido


class Cliente:
    def __init__(self, id, estado, hora_llegada):
        self.id = id
        self.estado = estado
        self.hora_llegada = hora_llegada


##TODO   imprimir en el excel toda la magia, modificar los parametros de inicio y arreglar el router
class Fila:
    def __init__(self, reloj, llegada_cliente, peluquero, peluqueroA, peluqueroVa, peluqueroVb, fin_atencion_aprendiz,
                 fin_atencion_veterano_a,
                 fin_atencion_veterano_b, cliente):
        self.reloj = reloj
        self.llegada_cliente = llegada_cliente
        self.peluquero = peluquero
        self.peluqueroA = peluqueroA
        self.peluqueroVa = peluqueroVa
        self.peluqueroVb = peluqueroVb
        self.fin_atencion_aprendiz = fin_atencion_aprendiz
        self.fin_atencion_veterano_a = fin_atencion_veterano_a
        self.fin_atencion_veterano_b = fin_atencion_veterano_b
        self.cliente = cliente

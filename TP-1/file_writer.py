import os
from shutil import rmtree

VALUE = 0

listDir = os.listdir()

if 'numbers' in listDir:
    rmtree("./numbers")
os.mkdir("./numbers", 0o777)

if 'montecarlo' in listDir:
    rmtree("./montecarlo")
os.mkdir("./montecarlo", 0o777)

if 'montecarloMemoria' in listDir:
    rmtree("./montecarloMemoria")
os.mkdir("./montecarloMemoria", 0o777)

if 'colas' in listDir:
    rmtree("./colas")
os.mkdir("./colas", 0o777)


def headers(data):
    global VALUE
    VALUE
    n = open("./colas/colas-{}.csv".format(VALUE), "w")

    n.write("Peluqueria" + os.linesep)
    for index in data:
        for index2 in index:
            n.write(str(index2) + " , ")
        n.write(os.linesep)
    n.close()


def colas(fila):
    global VALUE
    VALUE = VALUE
    n = open("./colas/colas-{}.csv".format(VALUE), "a")

    aux = []
    aux.append(round(fila.reloj, 2))
    aux.append(round(fila.llegada_cliente.rnd, 2))
    aux.append(round(fila.llegada_cliente.tiempo_entre_llegadas, 2))
    aux.append(round(fila.llegada_cliente.prox_llegada, 2))

    aux.append(round(fila.peluquero[0], 2))
    aux.append(fila.peluquero[1])

    aux.append(len(fila.peluqueroA.cola))
    aux.append(fila.peluqueroA.estado)
    aux.append(fila.peluqueroA.utilidad)
    aux.append(fila.peluqueroA.utilidad_acumulada)

    aux.append(len(fila.peluqueroVa.cola))
    aux.append(fila.peluqueroVa.estado)
    aux.append(fila.peluqueroVa.utilidad)
    aux.append(fila.peluqueroVa.utilidad_acumulada)

    aux.append(len(fila.peluqueroVb.cola))
    aux.append(fila.peluqueroVb.estado)
    aux.append(fila.peluqueroVb.utilidad)
    aux.append(fila.peluqueroVb.utilidad_acumulada)

    aux.append(round(fila.fin_atencion_aprendiz.rnd, 2))
    aux.append(round(fila.fin_atencion_aprendiz.tiempo_atencion, 2))
    aux.append(round(fila.fin_atencion_aprendiz.fin_atencion, 2))

    aux.append(round(fila.fin_atencion_veterano_a.rnd, 2))
    aux.append(round(fila.fin_atencion_veterano_a.tiempo_atencion, 2))
    aux.append(round(fila.fin_atencion_veterano_a.fin_atencion, 2))

    aux.append(round(fila.fin_atencion_veterano_b.rnd, 2))
    aux.append(round(fila.fin_atencion_veterano_b.tiempo_atencion, 2))
    aux.append(round(fila.fin_atencion_veterano_b.fin_atencion, 2))

    if fila.fin_espera_cliente is not None:
        aux.append(round(fila.fin_espera_cliente.tiempo, 2))
        aux.append(fila.fin_espera_cliente.cliente_id)
        aux.append(fila.fin_espera_cliente.peluquero_id)

    clientes_aux = []
    for i in fila.clientes:
        clientes_aux.append(i.id)
        clientes_aux.append(i.estado)
        if i.hora_de_partida != "-":
            clientes_aux.append(round(i.hora_de_partida, 2))
        clientes_aux.append(i.peluquero)
    for i in aux:
        n.write(str(i) + " , ")
    for i in clientes_aux:
        n.write(str(i) + " , ")

    n.write(os.linesep)


def numbers(numbers):
    global VALUE

    VALUE = VALUE + 1
    n = open("./numbers/numbers-{}.csv".format(VALUE), "w")

    n.write("Números pseudo - aleatorios generados" + os.linesep)
    for index in numbers:
        n.write(str(index) + os.linesep)
    n.close()

def montecarlo(header, data):
    global VALUE

    VALUE = VALUE + 1
    n = open("./montecarlo/montecarlo-{}.csv".format(VALUE), "w")

    for i in header:
        n.write(str(i) + " , ")
    n.write(os.linesep)
    for index in data:
        for index2 in index:
            n.write(str(index2) + " , ")
        n.write(os.linesep)
    n.close()


def montecarloMemoria(header, data):
    global VALUE

    VALUE = VALUE + 1
    n = open("./montecarloMemoria/montecarloMemoria-{}.csv".format(VALUE), "w")

    for i in header:
        n.write(str(i) + " , ")
    n.write(os.linesep)

    for index1 in data[-2]:
        n.write(str(index1) + " , ")
    n.write(os.linesep)

    for index2 in data[-1]:
        n.write(str(index2) + " , ")
    n.write(os.linesep)

    n.close()

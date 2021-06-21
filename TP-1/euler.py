import os
from shutil import rmtree
VALUE = 0
listDir = os.listdir()

if 'colas-euler' in listDir:
    rmtree("./colas-euler")
os.mkdir("./colas-euler", 0o777)


def colas_euler(c, T, h, corte):
    inicializacion()
    fila_anterior = FilaColaEuler(0, 0, 0, 0, 0.3)
    impresar(fila_anterior)

    while (fila_anterior.to < corte):
        derivada = c + 0.2 * T + fila_anterior.to

        fila_siguiente = FilaColaEuler(fila_anterior.t_1, fila_anterior.T_1, derivada, fila_anterior.t_1 + h,
                                       fila_anterior.T_1 + h * derivada)
        fila_anterior = fila_siguiente

        impresar(fila_siguiente)

    resumen([])

    return fila_anterior.to

class FilaColaEuler:
    def __init__(self, to, To, dT_dt, t_1, T_1):
        self.to = to
        self.To = To
        self.dT_dt = dT_dt
        self.t_1 = t_1
        self.T_1 = T_1


def inicializacion():
    n = open("./colas-euler/colas-euler-{}.csv".format(VALUE), "w")

    headers = ["to", "To", "dT_dt", "t_1", "T_1"]
    for index in headers:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()


def ini_resumen():
    n = open("./colas-euler/resumen.csv", "w")

    headers = ["cliente", "T", "?"]
    for index in headers:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()


def resumen(aux):
    n = open("./colas-euler/resumen.csv", "a")
    for index in aux:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()


def impresar(fila_siguiente):
    global VALUE

    VALUE = VALUE
    n = open("./colas-euler/colas-euler-{}.csv".format(VALUE), "a")

    aux = []

    aux.append(fila_siguiente.to)
    aux.append(fila_siguiente.To)
    aux.append(fila_siguiente.dT_dt)
    aux.append(fila_siguiente.t_1)
    aux.append(fila_siguiente.T_1)
    for index in aux:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()

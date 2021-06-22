import os
from shutil import rmtree
VALUE = 0
listDir = os.listdir()

if 'colas-euler' in listDir:
    rmtree("./colas-euler")
os.mkdir("./colas-euler", 0o777)


def colas_euler(cliente, to, do, T, c, h):
    fila_anterior = FilaColaEuler("", "", "", 0, 0)
    derivada = c + 0.2 * T + to
    fila_siguiente = FilaColaEuler(to, do, derivada, to + h,
                                   to + h * derivada)
    fila_anterior = fila_siguiente
    impresar(fila_siguiente)

    return fila_anterior

class FilaColaEuler:
    def __init__(self, to, do, dD_dt, t_1, D_1):
        self.to = to
        self.do = do
        self.dD_dt = dD_dt
        self.t_1 = t_1
        self.D_1 = D_1


def inicializacion():
    n = open("./colas-euler/colas-euler-{}.csv".format(VALUE), "w")

    headers = ["to", "Do", "dD_dt", "t_1", "D_1"]
    for index in headers:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()


def impresar(fila_siguiente):
    global VALUE

    VALUE = VALUE
    n = open("./colas-euler/colas-euler-{}.csv".format(VALUE), "a")

    aux = []

    aux.append(fila_siguiente.to)
    aux.append(fila_siguiente.do)
    aux.append(fila_siguiente.dD_dt)
    aux.append(fila_siguiente.t_1)
    aux.append(fila_siguiente.D_1)
    for index in aux:
        n.write(str(index) + ", ")
    n.write(os.linesep)
    n.close()

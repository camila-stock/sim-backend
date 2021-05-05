import csv
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
    
    n.write(str(header) + os.linesep)
    for index in data:
        n.write(str(index) + os.linesep)
    n.close()


def montecarloMemoria(header, data):
    global VALUE

    VALUE = VALUE + 1
    n = open("./montecarloMemoria/montecarloMemoria-{}.csv".format(VALUE), "w")
    
    n.write(str(header) + os.linesep)
    n.write(str(data[-2]) + os.linesep)
    n.write(str(data[-1]) + os.linesep)
    
    n.close()

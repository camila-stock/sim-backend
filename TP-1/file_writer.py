import csv
import os
from shutil import rmtree

VALUE = 0

listDir = os.listdir()

if 'numbers' in listDir:
    rmtree("./numbers")
os.mkdir("./numbers", 0o777)
def numbers(numbers):
    global VALUE

    VALUE = VALUE + 1
    n = open("./numbers/numbers-{}.csv".format(VALUE), "w")

    n.write("Números pseudo - aleatorios generados" + os.linesep)
    for index in numbers:
        n.write(str(index) + os.linesep)
    n.close()

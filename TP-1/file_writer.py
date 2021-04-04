import csv
import os
from shutil import rmtree


def numbers(numbers):
    listDir = os.listdir()
    if 'numbers' in listDir:
        rmtree("./numbers")
    os.mkdir("./numbers", 0o777)

    n = open("./numbers/numbers.csv", "w")

    n.write("Números aleatorios generados" + os.linesep)
    for index in numbers:
        n.write(str(index) + os.linesep)
    n.close()

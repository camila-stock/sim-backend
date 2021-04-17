from decimal import Decimal, ROUND_HALF_UP
import random
import math

def normal(n, media, desviacion, intervalos):
    cota_sup = 0
    res = []
    numbers = []
    minimum = 0
    maximum = 0

    value = int(n/2)
    for i in range(0, value):
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)

        aux1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2)) * desviacion + media
        aux2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * math.pi * x2)) * desviacion + media

        output1 = Decimal(Decimal(aux1).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        output2 = Decimal(Decimal(aux2).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))

        if output1 > maximum:
            maximum = output1
        if output2 > maximum:
            maximum = output2
        
        if output1 < minimum:
            minimum = output1
        if output2 < minimum:
            minimum = output2
        
        numbers.append(float(output1))
        numbers.append(float(output2))

        if output1 > 0.9999:
            output1 = 0.9999
        if output2 > 0.9999:
            output2 = 0.9999

    tam_interval = (abs(minimum) + abs(maximum)) / intervalos
    cota_sup = minimum

    for i in range(0,intervalos):
        intervalo = Intervalo(i,cota_sup)
        cota_sup = tam_interval + cota_sup
        res.append(intervalo)
    

    for i in range(0, len(numbers)):
        for j in range(0, len(res)):
            if numbers[i] <= res[j].cota_superior:
                res[j].frecuencia += 1
                break


    response = {
        'data': res,
        'numbers': numbers
    }
    return response


class Intervalo:
  frecuencia = 0
  def __init__(self, numero_intervalo, cota_superior):
    self.numero_intervalo = numero_intervalo
    self.cota_superior = cota_superior

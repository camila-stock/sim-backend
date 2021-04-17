from decimal import Decimal, ROUND_HALF_UP
import random
import math

def normal(n, media, desviacion, intervalos):
    tam_interval = n / intervalos
    cota_sup = 0
    res = []
    numbers = []
    for i in range(0,intervalos):
        cota_sup = tam_interval + cota_sup
        intervalo = Intervalo(i,cota_sup)
        res.append(intervalo)
    if res[-1].cota_superior < 0.9999:
            res[-1].cota_superior = 0.9999

    value = int(n/2)
    print("value: {}".format(value))
    for i in range(0, value):
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)

        aux1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2)) * desviacion + media
        aux2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * math.pi * x2)) * desviacion + media

        output1 = Decimal(Decimal(aux1).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        output2 = Decimal(Decimal(aux2).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))

        numbers.append(float(output1))
        numbers.append(float(output2))

        if output1 > 0.9999:
            output1 = 0.9999
        if output2 > 0.9999:
            output2 = 0.9999

        for item in range(0, len(res)):
            if output1 <= res[item].cota_superior:
                res[item].frecuencia += 1
                break

            if output2 <= res[item].cota_superior:
                res[item].frecuencia += 1
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

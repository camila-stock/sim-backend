from decimal import Decimal, ROUND_HALF_UP
import random
import math

def exponencial(n, lambd, intervalos):
    tam_interval = n / intervalos
    cota_sup = 0
    res = []
    numbers = []
    for i in range(0, intervalos):
        cota_sup = tam_interval + cota_sup
        intervalo = Intervalo(i, cota_sup)
        res.append(intervalo)
    if res[-1].cota_superior < n:
            res[-1].cota_superior = n
    for i in range(0, n):
        x = random.uniform(0, 1)
        valor_final = (-1 / lambd) * math.log(1 - x)
        output = Decimal(Decimal(valor_final).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        numbers.append(float(output))
        if output > n:
            output = n
        for item in range(0, len(res)):
            if output <= res[item].cota_superior:
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

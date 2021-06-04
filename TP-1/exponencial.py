from decimal import Decimal, ROUND_HALF_UP
import random
import math

def exponencial(n, lambd, intervalos):
    minimum = 0
    maximum = 0
    res = []
    numbers = []

    for i in range(0, n):
        x = random.uniform(0, 1)
        valor_final = (-1 / lambd) * math.log(1 - x)
        output = Decimal(Decimal(valor_final).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        if output > n:
            output = n
        
        if output > maximum:
            maximum = output
        
        if output < minimum:
            minimum = output
    
        numbers.append(float(output))
    
    tam_interval = (abs(minimum) + abs(maximum)) / intervalos
    cota_sup = minimum + tam_interval

    for i in range(0,intervalos):
        cota_inferior = cota_sup
        cota_sup = tam_interval + cota_sup
        intervalo = Intervalo(i, cota_sup, cota_inferior)
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
  def __init__(self, numero_intervalo, cota_superior, cota_inferior):
    self.numero_intervalo = numero_intervalo
    self.cota_superior = cota_superior
    self.cota_inferior = cota_inferior


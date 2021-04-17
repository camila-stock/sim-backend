from decimal import Decimal, ROUND_HALF_UP
import random
import math

   
def exponencial(n, a, b,):

   sumatoria = 0
   cota_superior = 0

   tam_interval = b - a
   rnd = []
   for i in range (0,n)
    value = random.uniform(0, 1)
    rnd.append(value)
    sumatoria =+ value
   
   media = sumatoria / n
   lda = 1 / media

   res = []
   for i in range rnd
    x = ( -1 / lda ) * math.log(1-rnd[i])
    res.append(x)

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
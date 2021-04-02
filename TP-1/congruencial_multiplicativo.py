from decimal import Decimal, ROUND_HALF_UP

def multiplicativeMethod(n, x, k, g, intervalos):
    a = 3 + 8 * k
    m = pow(2, g)
    tam_interval = 0.9999 / intervalos
    cota_sup = 0
    res = []
    numbers = []
    for i in range(0,intervalos):
        cota_sup = tam_interval + cota_sup
        intervalo = Intervalo(i,cota_sup)
        res.append(intervalo)
    if res[-1].cota_superior < 0.9999:
            res[-1].cota_superior = 0.9999
    for i in range(0,n):
        x = ((a * x) % m)
        ran = Decimal(x) / Decimal(m - 1)
        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        numbers.append(float(output))
        if output > 0.9999:
            output = 0.9999
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

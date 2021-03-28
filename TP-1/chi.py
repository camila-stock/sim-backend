
def chiMethod(data):
    lista_chi = []
    for i in range(0,len(data)):
        lista_chi.append(Chi(data[i].frecuencia,0,0,0))
    return lista_chi
    """ a = 1 + 4 * k
    m = pow(2, g)
    lista_valores = []
    tam_interval = 0.9999 / intervalos
    cota_superior = 0
    res = []
    for i in range(0,intervalos):
        cota_superior = tam_interval + cota_superior
        intervalo = Intervalo(i,cota_superior)
        res.append(intervalo)
    if res[-1].cota_superior < 0.9999:
            res[-1].cota_superior = 0.9999
    for i in range(0,n):
        x = ((a * x + c) % m)
        ran = Decimal(x) / Decimal(m - 1)

        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        if output > 0.9999:
            output = 0.9999
        for item in range(0, len(res)):
            if output <= res[item].cota_superior:
                res[item].frecuencia += 1
                break
    for i in range(0,len(res)):
        res[i] = json.dumps(res[i].__dict__) """


class Chi:
  def __init__(self, fo, fe, C, CA):
    self.fo = fo
    self.fe = fe
    self.C = C
    self.CA = CA

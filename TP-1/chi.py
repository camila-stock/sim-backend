def chiMethod(data):
    lista_chi = []
    sumatoria = 0

    for i in data:
        sumatoria = sumatoria + i.frecuencia

    fe = sumatoria / len(data)
    ca = 0
    for i in range(0,len(data)):
        c = pow(float(float(fe) - float(data[i].frecuencia)), 2) / fe
        ca = ca + c
        lista_chi.append(Chi(data[i].cota_superior,data[i].frecuencia, fe, c,ca))
    return lista_chi

class Chi:
  def __init__(self, intervalo, fo, fe, C, CA):
    self.intervalo = intervalo
    self.fo = fo
    self.fe = fe
    self.C = C
    self.CA = CA

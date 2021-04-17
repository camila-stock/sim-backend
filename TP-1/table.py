def table(data):
    lista = []
    sumatoria = 0

    for i in data:
        sumatoria = sumatoria + i.frecuencia

    fe = sumatoria / len(data)
    for i in range(0,len(data)):
        lista.append(Table(data[i].cota_superior, data[i].frecuencia, fe))
    return lista

class Table:
  def __init__(self, intervalo, fo, fe):
    self.intervalo = intervalo
    self.fo = fo
    self.fe = fe

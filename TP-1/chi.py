
def chiMethod(data):
    lista_chi = []
    for i in range(0,len(data)):
        lista_chi.append(Chi(data[i].frecuencia,0,0,0))
    return lista_chi

class Chi:
  def __init__(self, fo, fe, C, CA):
    self.fo = fo
    self.fe = fe
    self.C = C
    self.CA = CA

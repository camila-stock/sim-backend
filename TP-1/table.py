import math 
def table(data):
    lista = []
    sumatoria = 0

    for i in data:
        sumatoria = sumatoria + i.frecuencia

    fe = sumatoria / len(data)
    for i in range(0,len(data)):
        lista.append(Table(str(round(data[i].cota_inferior,4)) +" - "+ str(round(data[i].cota_superior,4)), data[i].frecuencia, fe))
    return lista

def tableExponencial(data, lb):
    lista = []
    sumatoria = 0
    

    for i in range (0,len(data)):
        cota_inf = float(round(data[i].cota_inferior,4))
        cota_sup = float(round(data[i].cota_superior,4) )
        mc = (cota_sup + cota_inf) /2
        pcpac = ( 1 - math.exp( - lb * cota_sup   ) ) - ( 1 - math.exp( - lb * cota_inf   ) )
        fe = mc * pcpac
        lista.append(Table(str(round(data[i].cota_inferior,4)) +" - "+ str(round(data[i].cota_superior,4)), data[i].frecuencia, str(round(fe,4))))
       
    return lista

def tableNormal(data, m, n, d):
    lista = []
    sumatoria = 0
    

    for i in range (0,len(data)):
        cota_inf = float(round(data[i].cota_inferior,4))
        cota_sup = float(round(data[i].cota_superior,4) )
        mc = (cota_sup + cota_inf) /2
        exponente = (mc - m) / d
        exp = math.exp(-0.5 * math.pow(exponente,2))
        denominador = d * math.sqrt(math.pi * 2)

        division = (exp / denominador)
        pcpac = abs(division * mc)

        fe = pcpac * n
        lista.append(Table(str(round(data[i].cota_inferior,4)) +" - "+ str(round(data[i].cota_superior,4)), data[i].frecuencia, str(round(fe,4))))
       
    return lista

class Table:
  def __init__(self, intervalo, fo, fe):
    self.intervalo = intervalo
    self.fo = fo
    self.fe = fe

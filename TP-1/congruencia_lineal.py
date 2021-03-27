from decimal import Decimal, ROUND_HALF_UP

def linearMethod(x, k, c, g):
    periodo = 0
    bandera = 0
    a = 1 + 4 * k
    m = pow(2, g)

    lista_intervalos = [0]
    lista_valores = []
    count_intervalo = 10

    tam_intervalo = Decimal(0.9999) / Decimal(count_intervalo)
    lugar_intervalo = tam_intervalo
    print("tam_intervalo: {0}".format(tam_intervalo))

    lista_intervalos.append(tam_intervalo)

    while (bandera != x):
        if (periodo == 0):
            bandera = x
        x = ((a * x + c) % m)
        ran = Decimal(x) / Decimal(m - 1)

        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        print(output)
        lista_valores.append(output)
        lugar_intervalo = tam_intervalo + lugar_intervalo
        lista_intervalos.append(lugar_intervalo)
        periodo = periodo + 1

    count_valor_x_intervalo = []


     for i in range(len(M)):
     print '[',
     for j in range(len(M[i])):
     print '{:>3s}'.format(str(M[i][j])),
     print ']'

    print("Range: {0}".format(range(1, periodo)))
    for i in range(1, periodo):
        print("valor de i: {0}".format(i))
        for j in lista_intervalos
            if (lista_valores[i-1] < lista_intervalos[j])

        print("valor anterior: {0}".format(valor_anterior))
        print("tam_intervalo: {0}".format(tam_intervalo))
        aux = valor_anterior + tam_intervalo
        print("Valor anterior + intrevalo: {0}".format(aux))
        lista_intervalos.append(aux)

    print("### Lista de intervalos: {0}".format(lista_intervalos))

#    if(periodo == m):
#        print("El periodo es completo: ", periodo)
#    else:
#        print("El periodo es incompleto:", periodo)


def main():
    x = int(input("Introduce el valor de la semilla: "))
    k = int(input("Introduce el valor de k: "))
    c = int(input("Introduce el valor de c: "))
    g = int(input("Introduce el valor de g: "))
    linearMethod(x, k, c, g)


if __name__ == "__main__":
    main()

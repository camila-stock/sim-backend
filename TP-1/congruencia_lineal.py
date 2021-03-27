from decimal import Decimal, ROUND_HALF_UP


def linearMethod(x, k, c, g):
    periodo = 1
    bandera = 0
    a = 1 + 4 * k
    mod = pow(2, g)

    lista_intervalos = []
    count_intervalo = 10

    tam_intervalo = Decimal(periodo) / Decimal(count_intervalo)
    print("tam_intervalo: {0}".format(tam_intervalo))

    lista_intervalos.append(0)

    print("Range: {0}".format(range(0, periodo)))
    for i in range(0, periodo):
        print("valor de i: {0}".format(i))
        valor_anterior = lista_intervalos[i]
        print("valor anterior: {0}".format(valor_anterior))
        print("tam_intervalo: {0}".format(tam_intervalo))
        aux = valor_anterior + tam_intervalo
        print("Valor anterior + intrevalo: {0}".format(aux))
        lista_intervalos.append(aux)


    print("### Lista de intervalos: {0}".format(lista_intervalos))
    while (bandera != x):
        if (periodo == 0):
            bandera = x
        x = ((a * x + c) % mod)
        ran = Decimal(x) / Decimal(mod - 1)

        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        print(output)
        periodo = periodo + 1

#    if(periodo == mod):
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

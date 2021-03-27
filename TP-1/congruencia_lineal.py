from decimal import Decimal, ROUND_HALF_UP

def linearMethod(x, k, c, g):

    periodo = 0
    bandera = 0
    a = 1+ 4 * k
    mod = pow(2,g)

    while(bandera != x):
        if (periodo == 0):
            bandera = x
        x =  ( (a * x + c) % mod )
        ran =Decimal(x) / Decimal( mod - 1 )

        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        print(output)
        periodo = periodo + 1

'''
    if(periodo == mod):
        print("El periodo es completo: ", periodo)
    else:
        print("El periodo es incompleto:", periodo)
'''

def main():
    x = int(raw_input("Introduce el valor de la semilla: "))
    k = int(raw_input("Introduce el valor de k: "))
    c = int(raw_input("Introduce el valor de c: "))
    g = int(raw_input("Introduce el valor de g: "))
    linearMethod(x,k,c,g)

if __name__ == "__main__":
    main()

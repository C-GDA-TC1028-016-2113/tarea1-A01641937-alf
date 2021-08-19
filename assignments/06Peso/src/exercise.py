def main():
    #escribe tu código abajo de esta línea
    peso = int(input("Dame el peso inicial: "))
    pesof = int(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    kg = float((peso - pesof) / meses)
    print ("Lo que debes bajar por mes es:",kg)


if __name__ == '__main__':
    main()

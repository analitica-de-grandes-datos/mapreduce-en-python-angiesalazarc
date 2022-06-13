#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    contador = 0

    for line in sys.stdin:
        lista = line.split("  ")

        sys.stdout.write("{}   {}   {}\n".format(lista[0], lista[1].strip(), int(lista[2])))

        if contador >= 5:
            break

        contador = contador + 1

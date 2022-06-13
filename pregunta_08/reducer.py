#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    suma = 0
    cont = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            suma = suma + val
            cont = cont + 1

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/cont))

            curkey = key
            suma = val
            cont = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/cont))
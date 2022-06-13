#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


if __name__ == "__main__":

    for line in sys.stdin:
        cl, val = line.split('\t')
        val = list(val.strip().split(','))
        cl = cl.zfill(4)

        for letra in val:
            sys.stdout.write("{}\t{}\n".format(letra, cl))
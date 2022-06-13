#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    curkey = None
    count = 0
    suma = 0

    for line in sys.stdin:

        key, value = line.split("\t")
        value = int(value)

        if key == curkey:
            suma = suma + value
            count = count + 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/count))
            curkey = key
            suma = value
            count = 1

        sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/count))
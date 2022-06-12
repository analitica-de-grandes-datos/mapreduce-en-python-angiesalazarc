#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    curkey = None
    max = 0

    for line in sys.stdin:
        key, value = line.split("\t")
        value = float(value)

        if key == curkey:
            if value > max:
                max = value
            if value < min:
                min = value

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))
            curkey = key
            max = value
            min = value

        sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    curkey = None
    count = 0

    for line in sys.stdin:

        key, value = line.split("\t")
        value = int(value)

        if key == curkey:
            t = t + value
            count = count + 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, t, t/count))
            curkey = key
            t = value

        sys.stdout.write("{}\t{}\t{}\n".format(curkey, t, t))
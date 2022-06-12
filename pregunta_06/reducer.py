#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    vmax  = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            if val > vmax:
                vmax = val
            if val < vmin:
                vmin = val

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, vmax, vmin))

            curkey = key
            vmax = val
            vmin = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, vmax, vmin))
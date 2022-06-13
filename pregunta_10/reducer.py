#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    vector = []

    for line in sys.stdin:
        letter, value = line.split("\t")
        value = int(value)
        vector.append((letter, value))

    vector.sort(key=lambda orden: (orden[0], orden[1]))

    curkey = None

    for line in vector:
        if curkey == line[0]:
            sys.stdout.write(",{}".format(line[1]))
        else:
            if curkey is not None:
                sys.stdout.write("\n{}\t{}".format(line[0], line[1]))
                curkey = line[0]
            else:
                sys.stdout.write("{}\t{}".format(line[0], line[1]))
                curkey = line[0]

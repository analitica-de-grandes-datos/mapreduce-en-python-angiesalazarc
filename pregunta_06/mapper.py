#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        column = line.split(" ")

        sys.stdout.write("{}\t{}\n".format(column[0], float(column[2])))
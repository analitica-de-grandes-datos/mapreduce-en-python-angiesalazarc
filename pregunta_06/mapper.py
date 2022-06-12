#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        column1 = line.split(" ")[0]
        column2 = line.split(" ")[2]

        sys.stdout.write("{}\t{}\n".format(column1, column2))
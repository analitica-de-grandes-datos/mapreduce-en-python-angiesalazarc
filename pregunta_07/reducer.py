#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    vector = []

    for line in sys.stdin:
        letter, date, value = line.split("\t")
        value = int(value)
        vector.append((letter, date, value))
    vector.sort(key=lambda orden: (orden[0], orden[2]))

    for line in vector:
        sys.stdout.write("{}   {}   {}\n".format(line[0], line[1].strip(), line[2]))
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
      esp = line.strip().split(",",3)
      sys.stdout.write("{}\t1\n".format(esp[2]))

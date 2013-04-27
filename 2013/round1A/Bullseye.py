__author__ = 'ezequiel'
from manager import Manager
import math
from decimal import *

class Bullseye(Manager):

    def main(self):
        for n in range(self.testcases):
            self.output.write("Case #%s: " % (n + 1))
            r, t = [int(x) for x in self.input.readline().strip().split(' ')]


            value = int(Decimal(1-2*r)/4+Decimal.sqrt(Decimal(4*math.pow(r,2)-(4*r)+1+8*t))/4)

            self.output.write(str(value)+"\n")
        self.output.close()

program = Bullseye('/home/ezequiel/Descargas/A-large.in')
program.main()



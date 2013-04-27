__author__ = 'ezequiel'
from manager import Manager
import math
from decimal import *

class ManageYourEnergy(Manager):

    def main(self):
        for n in range(self.testcases):
            self.output.write("Case #%s: " % (n + 1))
            E, R, n = [int(x) for x in self.input.readline().strip().split(' ')]
            values = [int(x) for x in self.input.readline().strip().split(' ')]
            max_value = max(values)
            total = 0
            max_found = False
            for val in values:
                if val == max_value:
                    if not max_found:
                        total += val*E
                        max_found=True
                else:
                    total += val*R
            self.output.write(str(total)+"\n")
        self.output.close()

program = ManageYourEnergy('/home/ezequiel/Descargas/B-small-attempt0.in')
program.main()



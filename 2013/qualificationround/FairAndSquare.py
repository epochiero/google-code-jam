__author__ = 'ezequiel'
from manager import Manager
import math

class FairAndSquare(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            A, B = [int(x) for x in self.input.readline().strip().split(' ')]
            total = 0
            for i in range(A, B+1):
                number = str(i)
                if number == number[::-1]:
                    root = math.sqrt(i)
                    int_root = int(root)
                    if root == int_root:
                        root_str = str(int_root)
                        if root_str == root_str[::-1]:
                            total += 1

            self.output.write(str(total)+"\n")
        self.output.close()

program = FairAndSquare('/home/ezequiel/Descargas/C-small-attempt0.in')
program.main()


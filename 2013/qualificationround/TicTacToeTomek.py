__author__ = 'ezequiel'
from manager import Manager

class TicTacToeTomek(Manager):

    def main(self):

        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            lines = []
            for i in range(4):
                lines.append(self.input.readline().strip())
            for line in ["".join(l[i] for l in lines) for i in range(4)]:
                lines.append(line)
            lines.append("".join([lines[0][0],lines[1][1], lines[2][2], lines[3][3]]))
            lines.append("".join([lines[0][3],lines[1][2], lines[2][1], lines[3][0]]))

            for line in lines:
                found = False
                if self.is_valid(line):
                    self.output.write("{} won".format((set(line) - set('T')).pop()))
                    found = True
                    break
            if not found:
                for line in lines:
                    if '.' in line:
                        self.output.write("Game has not completed")
                        found = True
                        break
            if not found:
                self.output.write("Draw")
            self.output.write("\n")
            self.input.readline()
        self.output.close()

    def is_valid(self, line):
        if 'T' in line and '.' not in line and len(set(line)) == 2:
            return True
        if '.' not in line and len(set(line)) == 1:
            return True
        return False

program = TicTacToeTomek('/home/ezequiel/Descargas/A-small-attempt0.in')
program.main()

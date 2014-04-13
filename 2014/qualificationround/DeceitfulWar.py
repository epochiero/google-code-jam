__author__ = 'ezequiel'
from manager import Manager


class DeceitfulWar(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            blocks_number = int(self.input.readline().strip())
            naomi_blocks = sorted([float(x) for x in self.input.readline().strip().split(' ')])
            ken_blocks = sorted([float(x) for x in self.input.readline().strip().split(' ')])

            naomi_normal_points = blocks_number
            ken_blocks_copy = list(ken_blocks)
            for naomi_block in naomi_blocks:
                possibles = [x for x in ken_blocks_copy if x > naomi_block]
                if len(possibles) > 0:
                    ken_blocks_copy.remove(min(possibles))
                    naomi_normal_points -= 1

            naomi_max_points = blocks_number
            naomi_blocks_copy = list(naomi_blocks)
            naomi_blocks_copy.reverse()
            ken_blocks_copy = list(ken_blocks)
            for naomi_block in naomi_blocks_copy:
                possibles = [x for x in ken_blocks_copy if x < naomi_block]
                if len(possibles) > 0:
                    ken_blocks_copy.remove(max(possibles))
                else:
                    naomi_max_points -= 1

            self.output.write("%s %s" %(str(naomi_max_points), str(naomi_normal_points)) + "\n")
        self.output.close()

program = DeceitfulWar('/home/ezequiel/Descargas/D-large.in')
program.main()

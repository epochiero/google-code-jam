__author__ = 'ezequiel'

class ForegoneSolution:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            digits = [int(x) for x in input()]
            number = int("".join([str(x) for x in digits]))
            to_substract = int("".join(["1" if digit == 4 else "0" for digit in digits]))
            print("Case #{}: {} {}\n".format(t+1, number-to_substract, to_substract))

program = ForegoneSolution()
program.main()

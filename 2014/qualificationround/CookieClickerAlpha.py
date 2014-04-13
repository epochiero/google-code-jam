__author__ = 'ezequiel'
from manager import Manager


class CookieClickerAlpha(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            C, F, X = [float(x) for x in self.input.readline().strip().split(' ')]
            rate = 2
            total_seconds = 0
            no_factory_time = X / rate
            while True:
                #Check if makes sense to buy another farm
                if X / rate < (C / rate + X / (rate + F)):
                    total_seconds += X / rate
                    break
                total_seconds += C / rate
                rate += F
            total_seconds = min(no_factory_time, total_seconds)
            self.output.write("%.8f" % total_seconds + "\n")
        self.output.close()

program = CookieClickerAlpha('/home/ezequiel/Descargas/B-large.in')
program.main()

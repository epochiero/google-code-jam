__author__ = 'ezequiel'

class YouCanGoYourOwnWay:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            maze_size = int(input())
            lydia_moves = [x for x in input()]

            #Mirror path
            my_moves = ["S" if x == "E" else "E" for x in lydia_moves]
            print("Case #{}: {}\n".format(t+1, "".join(my_moves)))

program = YouCanGoYourOwnWay()
program.main()

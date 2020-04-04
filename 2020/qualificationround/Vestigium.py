class Vestigium:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            N = int(input())
            matrix = []
            r = 0
            c = 0
            for nr_rows in range(N):
                row = [int(x) for x in input().split(" ")]
                matrix.append(row)
                if len(list(set(row))) != len(row):
                    r += 1
            transposed_matrix = zip(*matrix)
            for col in transposed_matrix:
                if len(list(set(col))) != len(col):
                    c += 1
            trace = sum(matrix[i][i] for i in range(N))
            print("Case #{}: {} {} {}".format(t+1, trace, r, c))


program = Vestigium()
program.main()

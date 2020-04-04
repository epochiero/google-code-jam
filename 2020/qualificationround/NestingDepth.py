class NestingDepth:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            S = input()
            # The first digit indicates the initial nesting level.
            prev = int(S[0])
            s_ = '(' * prev + str(prev)
            # From there, we look ahead one digit.
            for digit in S[1:]:
                current = int(digit)
                delta = current - prev
                # If the digit increases, add d(x, x+1) opening parentheses.
                if delta > 0:
                    s_ += '(' * delta
                # If it decreases, add d(x, x+1) closing ones.
                elif delta < 0:
                    s_ += ')' * abs(delta)
                # If it remains the same, do nothing.
                s_ += digit
                prev = current
            # At the end of the string, add closing parentheses as necessary.
            s_ += ')' * int(S[-1])
            print("Case #{}: {}".format(t + 1, s_))


program = NestingDepth()
program.main()

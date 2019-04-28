import math
from collections import Counter

class ManhattanCrepeCart:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            nr_people, max_value = [int(x) for x in input().split(" ")]
            next_locations = Counter()
            for p in range(nr_people):
                values = input().split(" ")
                x, y, direction = int(values[0]), int(values[1]), values[2]
                if direction == "N":
                    next_locations[(x, y+1)] += 1
                elif direction == "S":
                    next_locations[(x, y-1)] += 1
                elif direction == "E":
                    next_locations[(x+1, y)] += 1
                elif direction == "W":
                    next_locations[(x-1, y)] += 1
            if nr_people == 1:
                likely = next_locations.most_common()[0][0]
                if direction in ("N", "S"):
                    likely_x, likely_y = 0, likely[1]
                elif direction in ("E", "W"):
                    likely_x, likely_y = likely[0], 0
            else:
                # Find likely corner among most common ones
                all_corners = next_locations.most_common()
                possible = [all_corners[0]]
                count = all_corners[0][1]
                for corner in all_corners[1:]:
                    if corner[1] == count:
                        possible.append(corner)
                    else:
                        break
                if len(possible) == 1:
                    likely_x, likely_y = possible[0][0][0], possible[0][0][1]
                else:
                    if possible[0][0][0] < possible[1][0][0]:
                        likely_x, likely_y = possible[0][0][0], possible[0][0][1]
                    elif possible[0][0][0] > possible[1][0][0]:
                        likely_x, likely_y = possible[1][0][0], possible[1][0][1]
                    elif possible[0][0][1] < possible[1][0][1]:
                        likely_x, likely_y = possible[0][0][0], possible[0][0][1]
                    else:
                        likely_x, likely_y = possible[1][0][0], possible[1][0][1]

            print("Case {}: {} {}\n".format(t+1, likely_x, likely_y))

program = ManhattanCrepeCart()
program.main()

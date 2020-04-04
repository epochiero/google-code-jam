from collections import Counter
from operator import itemgetter


class ParentingPartneringReturns:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            N = int(input())
            counter = Counter()
            all_activities = []

            for i in range(N):
                start, end = [int(x) for x in input().split(" ")]
                for minute in range(start, end):
                    counter[minute] += 1
                all_activities.append((i, start, end))
            # There can't be any minute where there's more than 2 activities taking place
            max_overlap = counter.most_common(1)[0][1]
            if max_overlap > 2:
                print("Case #{}: IMPOSSIBLE".format(t + 1))
                continue
            ordered_activities = sorted(all_activities, key=itemgetter(1))

            # Knowing that, at most, 2 activities will overlap, we can be sure
            # one person will always be free at the start of the next scheduled
            # activity. Once the assigned activity for a person ends, simply wait
            # until the next scheduled one.
            active_person = "C"
            active_person_list = []
            for i in range(len(ordered_activities)-1):
                active_person_list.append([ordered_activities[i][0], active_person])
                if ordered_activities[i + 1][1] < ordered_activities[i][2]:
                    # Need to switch person
                    active_person = "J" if active_person == "C" else "C"
            active_person_list.append([ordered_activities[-1][0], active_person])
            active_person_list.sort(key=itemgetter(0))
            solution = ""
            for activity in active_person_list:
                solution += activity[1]
            print("Case #{}: {}".format(t + 1, solution))


program = ParentingPartneringReturns()
program.main()

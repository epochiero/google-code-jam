__author__ = 'ezequiel'
from manager import Manager


class MinesweeperMaster(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            R, C, M = [int(x) for x in self.input.readline().strip().split(' ')]
            free_cells = (R*C - M - 1)
            if R == 1 or C == 1:
                if (R*C - M) < 1:
                    self.output.write("Impossible\n")
                    continue
                if R == 1:
                    self.output.write("\nc"+ (".")*free_cells + ("*"*M) +"\n")
                    continue
                else:
                    self.output.write("\nc\n" + (".\n")*free_cells + ("*\n"*M))

            elif (R*C - M) < 4:
                self.output.write("Impossible\n")
                continue

            else:
                if M > 0 and R % M == 0:
                    board = []
                    for i in range(R):
                        board.extend(list("." * (C-1) +"*"))
                    board[0] = "c"
                    rendered_board =  "\n".join(["".join(board[C*n:C*(n+1)]) for n in range(R)])
                    self.output.write("\n"+rendered_board+"\n")
                    continue
                elif  M > 0 and C % M == 0:
                    board = list("." * (R*C -M) +"*"*M)
                    board[0] = "c"
                    rendered_board =  "\n".join(["".join(board[C*n:C*(n+1)]) for n in range(R)])
                    self.output.write("\n"+rendered_board+"\n")
                    continue
                else:
                    board = list("*" * (R*C))
                    #Complete as needed
                    current_free_cells = 0
                    iteration = 0
                    row_count = 0
                    col_count = 0
                    while current_free_cells < free_cells:
                        if row_count == 0 and col_count == 0:
                            board[0] = "c"
                            board[1] = "."
                            current_free_cells += 1
                            row_count += 1
                        if row_count < R and col_count == iteration * 2:
                            print "row_count %s" %row_count
                            board[(C* row_count)+col_count] = "."
                            current_free_cells += 1
                            try:
                                board[(C* row_count)+col_count +1] = "."
                                current_free_cells += 1
                            except:
                                pass
                            row_count += 1
                        else:
                            row_count = (iteration * 2)
                            for col_count in range((iteration+1)*2, C):
                                print "col_count %s" %col_count
                                board[col_count + (row_count*C)] = "."
                                current_free_cells += 1
                                try:
                                    board[col_count + ((row_count+1)*C)] = "."
                                    current_free_cells += 1
                                except:
                                    pass
                                if current_free_cells >= free_cells:
                                    break
                            #Start over with remaining cells
                            iteration += 1
                            row_count = iteration * 2
                            col_count = iteration * 2
                    if M % 2 != 0:
                        print current_free_cells
                        if current_free_cells+1 > free_cells:
                            for n in range(-1, C*-1-1, -1):
                                if board[n] != "*":
                                    board[n] = "*"
                                    break

                    rendered_board =  "\n".join(["".join(board[C*n:C*(n+1)]) for n in range(R)])
                    self.output.write("\n"+rendered_board+"\n")

        self.output.close()

program = MinesweeperMaster('/home/ezequiel/Descargas/C-small-attempt1.in')
program.main()

from manager import Manager
        
class SquareTiles(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1) + "\n")
            figura = []
            tieneAzul = False
            filas, columnas = [int(x) for x in self.input.readline().strip().split(" ")]
            for i in range(filas):
                linea = [x for x in self.input.readline().strip()]
                if "#" in linea: tieneAzul = True
                figura.append(linea)
            for i in range(filas-1):
                for j in range(columnas-1):
                    if figura[i][j] == "#" and figura[i+1][j] == "#" and figura[i][j+1] == "#" and figura[i+1][j+1] == "#":
                        figura[i][j] = "/"
                        figura[i+1][j] = "\\"
                        figura[i][j+1] = "\\"
                        figura[i+1][j+1] = "/"
            posible = True
            if tieneAzul:
                for l in figura:
                    if "#" in l: posible = False
            if posible:
                for i in range(filas):
                    for j in range(columnas):
                        self.output.write(figura[i][j])
                    self.output.write("\n")
            else:
                self.output.write("Impossible\n")
           
        self.output.close()
        
program = SquareTiles('/home/ezequiel/Descargas/A-small-attempt0.in')
program.main()
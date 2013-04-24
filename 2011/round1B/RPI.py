from manager import Manager
        
class RPI(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1) + "\n")
            equipos = int(self.input.readline())
            WP = {}
            OWP = {}
            OOWP = {}
            partidos = []
            oponentes = {}
            for equipo in range(equipos):
                resultados = self.input.readline().strip()
                partidos.append([int(x) if x != '.' else x for x in resultados])
                WP[equipo] = sum([int(x) for x in resultados if x=='1'])/float(len([x for x in resultados if x != '.']))
            
            for equipo in range(equipos):
                oponentes[equipo] = []
                for x in range(equipos):
                    if partidos[equipo][x] != '.': oponentes[equipo].append(x)
                
            for equipo in range(equipos):
                owps = []
                for i in oponentes[equipo]:
                    suma = 0
                    cant = 0
                    for j in range(equipos):
                        if j != equipo and partidos[i][j] != '.':
                            suma += partidos[i][j]
                            cant +=1
                    owps.append(float(suma)/cant)
                OWP[equipo] = float(sum([x for x in owps])) / len(owps)
            
            for equipo in range(equipos):
                OOWP[equipo] = float(sum(OWP[x] for x in oponentes[equipo])) / len(oponentes[equipo])               
                rpi = 0.25 * WP[equipo] + 0.50 * OWP[equipo] + 0.25 * OOWP[equipo]
                self.output.write(str(rpi)+"\n")
        self.output.close()
        
program = RPI('/home/ezequiel/Descargas/A-small-attempt0')
program.main()
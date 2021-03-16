import sys
import abc
import argparse
import print_table

class Proceso(object):

    def __init__(self, pid, t_llegada, duracion, prioridad=-1):
        self.pid = pid
        self.t_llegada = t_llegada
        self.duracion = duracion
        self.prioridad = prioridad
        self.t_restante = duracion

    def __repr__(self):
        if (self.pid == -1):
            return " - "
        return "P." + str(self.pid)

    def __str__(self):
        if (self.pid == -1):
            return " - "
        return "P." + str(self.pid)


class PlanificadorDeProcesos(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, fichero_procesos, leer_prioridades):
        self.procesos = self.leer_procesos(fichero_procesos, leer_prioridades)
        self.linea_tiempo = []
        self.procesos.sort(key=lambda p: p.t_llegada)

    @abc.abstractmethod
    def procesar(self, con_log):
        pass

    def leer_procesos(self, nombre_fichero, leer_prioridades):
        lista_procesos = list()
        with open(nombre_fichero, 'r') as f:
            line = f.readline()
            while(line):
                if ("#" in line):
                    line = f.readline()
                    continue
                tokens = line.split(' ')
                tokens = list(map(lambda v: int(v), tokens))
                if (leer_prioridades):
                    p = Proceso(tokens[0], tokens[1], tokens[2], tokens[3])
                else:
                    p = Proceso(tokens[0], tokens[1], tokens[2])
                lista_procesos.append(p)
                line = f.readline()
        return lista_procesos

    def fin_procesar(self):
        for p in self.procesos:
            if (p.t_restante > 0):
                return False
        return True

    def run(self, ancho_celda, con_log):
        self.procesar(con_log)
        self.imprimir(ancho_celda)

    def imprimir(self, espacio=5):
        print_table.print_table(self, espacio)


class RoundRobin(PlanificadorDeProcesos):

    def __init__(self, fichero_procesos):
        super().__init__(fichero_procesos, leer_prioridades=True)
        self.lista_aux = []
        for p in self.procesos:
            for i in range(p.prioridad):
                self.lista_aux.append(p)

    def procesar(self, con_log):
        t = 0
        if (con_log): print("T = {:<3}".format(t), end="|")  # LOG
        while not self.fin_procesar():
            band = False
            for p in self.lista_aux:
                if p.t_llegada <= (t) and p.t_restante > 0:
                    if (con_log): print(" Exe {:<3} , Tiemp. Restante = {:<3}".format(
                            p.__repr__(), p.t_restante))  # LOG
                    self.linea_tiempo.append(p)
                    p.t_restante -= 1
                    if (p.t_restante == 0):
                        if (con_log): print("-------|------------[SALE " + p.__repr__() + "]--------") # LOG
                        p.t_salida = len(self.linea_tiempo)
                    t += 1
                    if (con_log): print("T = {:<3}".format(t), end="|")  # LOG
                    band = True
            if not band:
                self.linea_tiempo.append(Proceso(-1, -1, -1, -1))
                t += 1
                if (con_log):
                    print(" FREE\nT = {:<3}".format(t), end="|")  # LOG
        if (con_log):
            print(" FIN\n")  # LOG


class PrimeroLlegarPrimeroAtender(PlanificadorDeProcesos):

    def __init__(self, fichero_procesos):
        super().__init__(fichero_procesos, leer_prioridades=False)

    def procesar(self, con_log):
        for p in self.procesos:
            self.linea_tiempo += [p] * p.duracion
            p.t_salida = len(self.linea_tiempo)


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.description = "Algoritmos de planificacion de procesos en Sistemas Operativos."
    parser.add_argument("algoritmo", choices=["rr", "rrp", "plpa"],
                        help="escoja el algoritmo: 'rr' para 'Round Robin', 'rrp' para 'Round Robin Prioridades',\
            'plpa' para 'Primero Llegar Primero Atender'")
    parser.add_argument(
        "fichero", type=str, help="fichero de donde se leeran los datos de cada procesos")

    parser.add_argument("-l", "--log", action="store_true",
                        help="imprimir log de la ejecución de los procesos")
    parser.add_argument("-w", "--width", type=int, help="otorge un ancho a las celdas de la linea de tiempo de \
                                                        los procesos (default: %(default)s)", default=5)
    return parser.parse_args()


if __name__ == "__main__":

    parser = get_argparser()

    d = {"rr":"Round Robin", "rrp": "Round Robin con Prioridades", "plpa": "Primero Llegar Primero Atender"}

    print("\n+" + "-"*(len(d[parser.algoritmo])+13) + "+\n| Algoritmo: " + d[parser.algoritmo] + \
            " |\n" + "+" + "-"*(len(d[parser.algoritmo])+13) + "+\n")

    if parser.algoritmo in "rr rrp":
        rr = RoundRobin(parser.fichero)
        rr.run(parser.width, parser.log)

    elif parser.algoritmo in "plpa":
        rr = PrimeroLlegarPrimeroAtender(parser.fichero)
        rr.run(parser.width, parser.log)
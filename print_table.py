import plapro

def print_table(obj: plapro.PlanificadorDeProcesos, espacio=5):
    celda_espacio = espacio
    separador = "+"
    for i in range(celda_espacio):
        separador += "-"

    # procesos que entran:
    for t in range(len(obj.linea_tiempo)+1):
        entran = []
        band = False
        for p in obj.procesos:
            if p.t_llegada == t:
                entran.append(p)
                band = True
        if (band):
            entran_str = ""
            for s in entran[:-1]:
                entran_str += str(s) + ","
            entran_str += str(entran[-1])
            print("{:{w}} ".format(entran_str, w=celda_espacio), end="")
        else:
            print(" {:>{w}}".format(" ", w=celda_espacio), end="")

    print()

    for t in range(len(obj.linea_tiempo)+1):
        band = False
        for p in obj.procesos:
            if p.t_llegada == t:
                print("|{:^{w}}".format(" ", w=celda_espacio), end="")
                band = True
                break
        if not band:
            print(" {:^{w}}".format(" ", w=celda_espacio), end="")

    print()

    for t in range(len(obj.linea_tiempo)+1):
        band = False
        for p in obj.procesos:
            if p.t_llegada == t:
                print("V{:^{w}}".format(" ", w=celda_espacio), end="")
                band = True
                break
        if not band:
            print(" {:^{w}}".format(" ", w=celda_espacio), end="")

    print()

    # linea tiempo:
    for p in obj.linea_tiempo:
        print(separador, end="")
    print("+")
    for p in obj.linea_tiempo:
        print("|{:^{w}}".format(p.__repr__(), w=celda_espacio), end="")
    print("|")
    for p in obj.linea_tiempo:
        print(separador, end="")
    print("+")
    for t in range(len(obj.linea_tiempo)):
        print("|{:^{w}}".format(t, w=celda_espacio), end="")
    print("|")
    for p in obj.linea_tiempo:
        print(separador, end="")
    print("+")

    # procesos que salen:
    for t in range(len(obj.linea_tiempo)+1):
        band = False
        for p in obj.procesos:
            if p.t_salida == t:
                print("|{:^{w}}".format(" ", w=celda_espacio), end="")
                band = True
                break
        if not band:
            print(" {:^{w}}".format(" ", w=celda_espacio), end="")

    print()

    for t in range(len(obj.linea_tiempo)+1):
        band = False
        for p in obj.procesos:
            if p.t_salida == t:
                print("V{:^{w}}".format(" ", w=celda_espacio), end="")
                band = True
                break
        if not band:
            print(" {:^{w}}".format(" ", w=celda_espacio), end="")

    print()

    for t in range(len(obj.linea_tiempo)+1):
        salen = []
        band = False
        for p in obj.procesos:
            if p.t_salida == t:
                salen.append(p)
                band = True
        if (band):
            salen_str = ""
            for s in salen[:-1]:
                salen_str += str(s) + ","
            salen_str += str(salen[-1])
            print("{:{w}} ".format(salen_str, w=celda_espacio), end="")
        else:
            print(" {:>{w}}".format(" ", w=celda_espacio), end="")

    # tabla de resultados
    print("\n")
    procesos_ord_por_pid = obj.procesos
    procesos_ord_por_pid.sort(key=lambda p: p.pid)
    print("+" + "-"*44 + "+")
    print("|" + " "*17 + "Resultados" + " "*17 + "|")
    separador_tabla = "+--------"
    for p in range(5):
        print(separador_tabla, end="")
    print("+")
    for p in ["PID", "T.LLeg.", "Durac.", "Prior.", "T.Perm."]:
        print("|{:^{w}}".format(p, w=len(separador_tabla)-1), end="")
    print("|")
    for p in range(5):
        print(separador_tabla, end="")
    print("+")
    for p in procesos_ord_por_pid:
        vals = [p.pid, p.t_llegada, p.duracion,
                p.prioridad, (p.t_salida - p.t_llegada)]
        if (p.prioridad == -1):
            vals[3] = "X"
        for i in vals:
            print("|{:^{w}}".format(i, w=len(separador_tabla)-1), end="")
        print("|")
    for p in range(5):
        print(separador_tabla, end="")
    print("+")
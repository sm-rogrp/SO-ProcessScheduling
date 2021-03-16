# SO-ProcessScheduling
CLI application for planification of process in operating systems. (Algorithms: Round Robin with/without priority and first come first served)

## Usage
```
usage: plapro.py [-h] [-l] [-w WIDTH] {rr,rrp,plpa} fichero

Algoritmos de planificacion de procesos en Sistemas Operativos.

positional arguments:
  {rr,rrp,plpa}         escoja el algoritmo: 'rr' para 'Round Robin', 'rrp' para 'Round Robin Prioridades', 'plpa'
                        para 'Primero Llegar Primero Atender'
  fichero               fichero de donde se leeran los datos de cada procesos

optional arguments:
  -h, --help            show this help message and exit
  -l, --log             imprimir log de la ejecución de los procesos
  -w WIDTH, --width WIDTH
                        otorge un ancho a las celdas de la linea de tiempo de los procesos (default: 5)
```
More information ➜ [informe.pdf](https://github.com/sm-rogrp/SO-ProcessScheduling/blob/master/informe.pdf)

## Example

1. Input file (in.txt)
```
1 0 5 1
2 3 6 2
3 5 7 1
4 7 5 2
```
2. Run
```
python plapro.py --log --width 3 rrp in1.txt
```
3. Output
```
+----------------------------------------+
| Algoritmo: Round Robin con Prioridades |
+----------------------------------------+

T = 0  | Exe P.1 , Tiemp. Restante = 5
T = 1  | Exe P.1 , Tiemp. Restante = 4
T = 2  | Exe P.1 , Tiemp. Restante = 3
T = 3  | Exe P.2 , Tiemp. Restante = 6
T = 4  | Exe P.2 , Tiemp. Restante = 5
T = 5  | Exe P.3 , Tiemp. Restante = 7
T = 6  | Exe P.1 , Tiemp. Restante = 2
T = 7  | Exe P.2 , Tiemp. Restante = 4
T = 8  | Exe P.2 , Tiemp. Restante = 3
T = 9  | Exe P.3 , Tiemp. Restante = 6
T = 10 | Exe P.4 , Tiemp. Restante = 5
T = 11 | Exe P.4 , Tiemp. Restante = 4
T = 12 | Exe P.1 , Tiemp. Restante = 1
-------|------------[SALE P.1]--------
T = 13 | Exe P.2 , Tiemp. Restante = 2
T = 14 | Exe P.2 , Tiemp. Restante = 1
-------|------------[SALE P.2]--------
T = 15 | Exe P.3 , Tiemp. Restante = 5
T = 16 | Exe P.4 , Tiemp. Restante = 3
T = 17 | Exe P.4 , Tiemp. Restante = 2
T = 18 | Exe P.3 , Tiemp. Restante = 4
T = 19 | Exe P.4 , Tiemp. Restante = 1
-------|------------[SALE P.4]--------
T = 20 | Exe P.3 , Tiemp. Restante = 3
T = 21 | Exe P.3 , Tiemp. Restante = 2
T = 22 | Exe P.3 , Tiemp. Restante = 1
-------|------------[SALE P.3]--------
T = 23 | FIN

P.1         P.2     P.3     P.4
|           |       |       |
V           V       V       V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|P.1|P.1|P.1|P.2|P.2|P.3|P.1|P.2|P.2|P.3|P.4|P.4|P.1|P.2|P.2|P.3|P.4|P.4|P.3|P.4|P.3|P.3|P.3|
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
                                                    |       |                   |           |
                                                    V       V                   V           V
                                                    P.1     P.2                 P.4         P.3

+--------------------------------------------+
|                 Resultados                 |
+--------+--------+--------+--------+--------+
|  PID   |T.LLeg. | Durac. | Prior. |T.Perm. |
+--------+--------+--------+--------+--------+
|   1    |   0    |   5    |   1    |   13   |
|   2    |   3    |   6    |   2    |   12   |
|   3    |   5    |   7    |   1    |   18   |
|   4    |   7    |   5    |   2    |   13   |
+--------+--------+--------+--------+--------+
```

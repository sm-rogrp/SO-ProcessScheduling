@echo off
echo ejecutando: 7 tests
echo ...
python plapro.py --log --width 3  rrp  input/in1.txt > output/out1.txt
python plapro.py --log --width 3  rrp  input/in2.txt > output/out2.txt
python plapro.py --log --width 5  rr   input/in3.txt > output/out3.txt
python plapro.py --log --width 5  rr   input/in4.txt > output/out4.txt
python plapro.py --log --width 3  rrp  input/in5.txt > output/out5.txt
python plapro.py --log --width 8  rrp  input/in6.txt > output/out6.txt
python plapro.py --log --width 5  plpa input/in7.txt > output/out7.txt
echo resultados generados, revise la carpeta 'output'
echo ------------------------------------------------
explorer output
pause
#!/bin/bash

wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesLaboratorio/master/2017-1/lab4_EJ1/red3.txt

awk '{if($2>2000) print $0;}' red3.txt > red3_filtrado.txt

python plots_laser.py

rm red3.txt
rm red3_filtrado.txt


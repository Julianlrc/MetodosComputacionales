#!/bin/bash

mkdir Convection
mv DatosRadioSonda.dat Convection
mv PLOTS_Convection.py Convection
cd Convection
 
awk '{print $2,$3;}' DatosRadioSonda.dat | sed '1,7d' | sed '111d' > TempHeight.txt
 
python PLOTS_Convection.py

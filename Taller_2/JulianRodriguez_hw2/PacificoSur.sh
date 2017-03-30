#!/bin/bash

wget http://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ocean/index/heat_content_index.txt
sed '1,2d' heat_content_index.txt > Heat_content_index.txt
awk '{print $0}' SOI.txt | sed '143d' | sed '1d' > soi.txt
mkdir Dir_PacificoSur
mv Heat_content_index.txt Dir_PacificoSur
mv soi.txt Dir_PacificoSur
rm heat_content_index.txt
mv SOI.txt Dir_PacificoSur
mv PCA_PacificoSur.py Dir_PacificoSur
cd Dir_PacificoSur
python PCA_PacificoSur.py

#!/bin/bash

echo "Punto 1..."
mkdir JuanUseche
cd JuanUseche

echo "Punto 2..."
wget http://www.finiterank.com/saber/2012.csv
wget http://www.finiterank.com/saber/2011.csv

echo "Punto 3..."
awk -F ',' -v OFS=',' '{print $1,$2,$4,$8,$10,$11,$13,$16}' 2011.csv > 2011_Filtro.csv
awk -F ',' -v OFS=','  '{print $1,$2,$23,$3,$5,$6,$10,$16}' 2012.csv > 2012_Filtro.csv

echo "Punto 4..."
cat 2011_Filtro.csv 2012_Filtro.csv > resultadosICFES2011-2012.csv

echo "Punto 5..."
echo "Colegios registrados 2011:"
wc -l 2011_Filtro.csv
echo "Colegios registrados 2012:"
wc -l 2012_Filtro.csv

echo "Punto 6..."
echo "Top 10 2011-2012:"
awk -F ',' -v OFS=',' '($1<=10){print $0}' resultadosICFES2011-2012.csv

echo "Punto 7..."
echo "Total Colegios A:"
awk -F ',' '($1<=10 && $4=="A"){print $0}' resultadosICFES2011-2012.csv | wc -l

echo "Punto 8..."
echo "Total Colegios B:"
awk -F ',' '($1<=10 && $4=="B"){print $0}' resultadosICFES2011-2012.csv | wc -l

echo "Punto 9..."
echo "Colegios Bogotá B:"
awk -F ',' '($3=="Bogotá" && $4=="B"){print $0}' resultadosICFES2011-2012.csv | wc -l

echo "Punto 10..."
echo "Públicos A Pgen>PFisicaMatematicas:"
awk -F ',' '($1<=10 && $4=="A" && $5>(($6+$7)/2.0)){print $1,$2,$4,$5,$6,$7,(($6+$7)/2.0)}' resultadosICFES2011-2012.csv | wc -l

echo "Punto 11..."
cd ../
rm -r JuanUseche

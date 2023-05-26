#!/bin/bash

# Ruta y nombre del archivo CSV
archivo_csv="pdb.csv"
salida="pdb_count.csv"

# Contar filas únicas (sin incluir la cabecera), salta el registro con tail
numero_filas=$(tail -n +2 "$archivo_csv" | sort | uniq -u | wc -l)
filas=$(tail -n +2 "$archivo_csv" | sort | uniq -u)

echo "Número de filas únicas (sin incluir la cabecera): $numero_filas"

i=1
#enlista en un for las filas unicas extraidas del csv
for fila in $filas
do
    #valida si existe archivo de salida
    if [ -f "$salida" ]; then
        echo "$i,$fila" >> $salida
    else
        echo "pdb_count.csv de registros unicos"
        echo "ID,resName1,PDB Classification,Uniprot Acc" > $salida
        echo "$i,$fila" >> $salida
    fi
    #contador en el bucle
    ((i++))
done
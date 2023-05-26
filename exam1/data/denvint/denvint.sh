#!/bin/bash

# Directorio raíz
directorio_raiz="./"

# Lee todos los archivos .csv de un directorio y trae la ruta

archivos=`find "$directorio_raiz" -type f -name "*.csv"`

# archivo de salida
salida="denint.csv"

# for para contar los items y las columnas de una lista de csv
for archivo in $archivos
do
    # Contar el número de filas
    numero_filas=$(wc -l < "$archivo")

    # Leer la primera fila del archivo para contar las columnas
    primera_fila=$(head -n 1 "$archivo")
    numero_columnas=$(echo "$primera_fila" | awk -F ',' '{print NF}')

    # Imprimir los resultados, valida si existe el archivo, si no existe crea la cabecera del .csv
    if [ -f "$salida" ]; then
        echo "$archivo,$numero_columnas,$numero_filas" >> $salida
    else
        echo "name_file,cols,rows" > $salida
        echo "$archivo,$numero_columnas,$numero_filas" >> $salida
    fi
done
#!/bin/bash

# Archivo de origen
archivo="infants_metagenome.txt"

# Imprimir registros que tengan hasta 6 símbolos de tubería en una fila, saltando la cabecera
# -F "|" establece el delimitador de campo como el símbolo de tubería (|).
# NR > 2 indica que se omita las 2 primeras línea (cabecera) del archivo.
# gsub(/\|/, "|") cuenta el número de "|" en cada línea reemplazándolas por sí mismas. La función gsub() devuelve el número de reemplazos realizados.
#<= 6 establece la condición para imprimir solo las líneas que tengan hasta 6 "|".

awk -F "|" 'NR > 2 && gsub(/\|/, "|") <= 6' "$archivo" | wc -l

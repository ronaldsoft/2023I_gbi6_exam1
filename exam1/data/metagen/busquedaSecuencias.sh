#!/bin/bash

# Archivo de origen
archivo="mygenomemap.sam"

# # Array de caracteres a buscar
caracteres=("TATA" "GAGA" "GATA")
columna=10
salida="gata.txt"

# # Construir la expresión regular para buscar cualquier carácter del array
regex=$(printf "[%s]" "$(IFS=""; echo "${caracteres[*]}")")

#limpieza del los datos
# # Empieza a partir de la quinta fila, Reemplazar espacios, tabs y dobles espacios por comas en cada fila del texto
# # Filtrar y mostrar las líneas que contienen los caracteres del array
limpieza=`tail -n +5 "$archivo" | grep -E "$regex" | sed 's/[[:space:]]\{1,\}/,/g'`

for linea in $limpieza
do
    #imprime solo la colunma deseada
    echo $linea|cut -d ',' -f "$columna" >> $salida
done
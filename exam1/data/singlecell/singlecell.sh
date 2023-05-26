#!/bin/bash
# Directorio de raiz 
directorio_raiz="./"

# Archivo de salida 
salida="extensiones.txt"

extensiones=`find "$directorio_raiz" -type f | awk -F. '!a[$NF]++{print $NF}'`

# for para traer el conteo de todas las extenciones
for ext in $extensiones
do
    # buscar y contar la cantidad total de los elementos por extencion
    conteo=`find "$directorio_raiz" -type f -name "*.$ext" | wc -l`
    # Hacer algo con cada elemento
    echo "Extención: .$ext, conteo: $conteo" >> $salida
done
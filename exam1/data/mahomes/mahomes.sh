#!/bin/bash

# Ruta y nombre del archivo CSV de origen
origen="sites.csv"

# Ruta y nombre del archivo CSV de destino
destino="pdb.csv"

# Columnas a extraer (separadas por comas)
columnas="5,18,21"

# Extraer columnas específicas del archivo CSV de origen y guardarlas en el archivo CSV de destino
cut -d',' -f"$columnas" "$origen" > "$destino"

echo "Se han extraído las columnas especificadas y guardado en el archivo $destino."

archivo="miRNA.dat"
salida="elegans.txt"
ocurrenciasNat=$(grep -i -o "Nature." "$archivo" | wc -l)
ocurrenciasPUB=$(grep -i -o "PUBMED" "$archivo" | wc -l)
ocurrenciasELE=$(grep -i -o "C. elegans" "$archivo" | wc -l)
ocurrenciasBP=$(grep -i -o "Sequence 139 BP" "$archivo"| wc -l)
echo "cuantos artículos se tiene a la fecha?: $ocurrenciasPUB"
echo "cuántos estudios de micro RNA se han publicado en la revista Nature?: $ocurrenciasNat"
echo "cuántos de ellos fueron el organismo C. elegans?: $ocurrenciasELE"
echo "cuántos micro RNA estudiados tiene una longitud 139?: $ocurrenciasBP"
echo $ocurrenciasBP > $salida
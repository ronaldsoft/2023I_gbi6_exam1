from Bio import Entrez, SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv

def fetch_sequence_info(term, mail):
    # Conexión al NCBI
    Entrez.email = mail
    handle = Entrez.esearch(db='nucleotide', term=term)
    record = Entrez.read(handle)
    handle.close()

    # Obtención de información de las secuencias
    id_list = record['IdList']
    seq_info = []
    for seq_id in id_list:
        handle = Entrez.efetch(db='nucleotide', id=seq_id, retmode='xml')
        seq_record = Entrez.read(handle)
        handle.close()

        source = seq_record[0]['GBSeq_source']  # Nombre del organismo fuente
        species = seq_record[0]['GBSeq_organism']  # Especie

        seq_info.append((source, species))

    return seq_info

def fetch_file_secuences(input, mail):
    # Conexión al NCBI
    Entrez.email = mail
    with open(input, 'r') as file:
        id_list = file.readlines()

    sequences = []
    for seq_id in id_list:
        handle = Entrez.efetch(db='nucleotide', id=seq_id.strip(), rettype='fasta')
        seq_record = SeqIO.read(handle, 'fasta')
        handle.close()

        sequences.append(seq_record)

    return sequences    

def count_species(seq_info):
    species_count = {}
    for _, species in seq_info:
        if species in species_count:
            species_count[species] += 1
        else:
            species_count[species] = 1
    return species_count

def save_results(seq_info, species_count, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source', 'Species', 'Count'])
        for source, species in seq_info:
            count = species_count[species]
            writer.writerow([source, species, count])

def fetch_sequences(term, mail):
    # Conexión al NCBI
    Entrez.email = mail
    handle = Entrez.esearch(db='nucleotide', term=term)
    record = Entrez.read(handle)
    handle.close()

    # Obtención de las secuencias de ADN
    id_list = record['IdList']
    sequences = []
    for seq_id in id_list:
        handle = Entrez.efetch(db='nucleotide', id=seq_id, rettype='fasta')
        seq_record = SeqIO.read(handle, 'fasta')
        handle.close()

        sequences.append(seq_record)

    return sequences

def translate_sequences(sequences):
    peptides = []
    for seq_record in sequences:
        dna_sequence = seq_record.seq
        protein_sequence = dna_sequence.translate()

        # Verificar si el péptido empieza en metionina y no contiene el símbolo de parada ('*')
        if protein_sequence.startswith('M') and '*' not in protein_sequence:
            peptides.append(protein_sequence)

    return peptides

def calculate_properties(peptides):
    # Cálculo de propiedades de los péptidos
    data = []
    for peptide in peptides:
        analysis = ProteinAnalysis(str(peptide))
        print(analysis)
        molecular_weight = analysis.molecular_weight()
        instability_index = analysis.instability_index()
        data.append((peptide, molecular_weight, instability_index))

    return data

def generate_plot(data, output_file):
    # Generación del jointplot
    df = pd.DataFrame(data, columns=['Peptide', 'Molecular Weight', 'Instability Index'])
    sns.set(style='ticks')
    plot = sns.jointplot(x='Molecular Weight', y='Instability Index', data=df, kind='scatter', color='skyblue', s=40, alpha=0.8)
    plot.set_axis_labels('Molecular Weight', 'Instability Index')
    plot.fig.suptitle('Peptide Molecular Weight vs. Instability Index', y=1.02)
    plt.tight_layout()

    # Guardar el jointplot como imagen
    plot.savefig(output_file)

def save_results_filter(data, output_file):
    # Guardar los resultados en un archivo CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Peptide', 'Molecular Weight', 'Instability Index'])
        writer.writerows(data)
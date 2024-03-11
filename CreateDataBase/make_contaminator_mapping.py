from Bio import Entrez,SeqIO
from ete3 import NCBITaxa
import subprocess
import csv
import gzip

Entrez.email = "n.alexandra.vogel@gmail.com"
Entrez.api_key = "f815551132f17a6be4e57546520bd8b46007"

ncbi = NCBITaxa()

id_list = []
tax_list = []
with gzip.open(f"/home/projects/animalia_mito/benchmarking/db_seqs.fa.gz", "rt") as file:
	sequences = SeqIO.parse(file, "fasta")
			
	for i in sequences:
		temp = []
		id_list.append(i.id)
		try:
			out = subprocess.check_output(f'esearch -db nucleotide -query "{i.id}" | esummary | xtract -pattern TaxId -element TaxId', shell=True)
			ran = out.decode('utf-8')
			ran = int(ran)
			temp.append(ran)
			taxid2name = ncbi.get_taxid_translator(temp)
			
			res = taxid2name[ran]
			#print(res)

		except:
			print(i.id)

		tax_list.append(res)



with open("/home/projects/animalia_mito/benchmarking/db_seqs.mapping", "w") as g:
	writer = csv.writer(g, delimiter = '\t')
	writer.writerows(zip(id_list, tax_list))	








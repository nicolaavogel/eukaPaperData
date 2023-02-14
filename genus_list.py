import pandas as pd

taxa = pd.read_csv("/home/projects/animalia_mito/tools/taxa.tab", sep="\t", header = None, error_bad_lines=False, names=['a', 'b', 'name', 'c', 'rank', 'taxid'])

arthopods_genus = []
for index, row in taxa.iterrows():
    if row['rank'] == 'genus' and '6656' in row['taxid']:
        arthopods_genus.append(row['name'])
        
print(len(arthopods_genus))
artho = open("/home/projects/animalia_mito/scripts/arthro_genus.txt", "w")
for e in arthopods_genus:
    artho.write(e + "\n")
artho.close()




        
tetrapods_genus = []
for index, row in taxa.iterrows():
    if row['rank'] == 'genus' and '32523' in row['taxid']:
        tetrapods_genus.append(row['name'])
        
print(len(tetrapods_genus))
tetra = open("/home/projects/animalia_mito/scripts/tetra_genus.txt", "w")
for e in tetrapods_genus:
    tetra.write(e + "\n")
tetra.close()

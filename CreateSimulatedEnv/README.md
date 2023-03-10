# Construction of simulated metagenomic environmnents

Our simulated metagenomic environments are created with a Snakemake pipeline. 
We provide a list of NCBI accesssion numbers from which we sampled for the contaminants (Bacteria.list, Virus.list, Plants.list, Archaea.list, Fungi.list), the nuclear contaminants (Nuclear_genomes.list) and the endogenous mitochondiral genomes (Mitochondiral_genomes.list). 

Additionally, we provide the damage profiles used to simulate the three levels of damage.
1. High damage rate ("dhigh5.dat and dhigh3.dat for the 5' end and the 3' end deamination done by gargammel") was taken from Günther, Torsten, et al. "Ancient genomes link early farmers from Atapuerca in Spain to modern-day Basques." Proceedings of the National Academy of Sciences 112.38 (2015): 11917-11922.
2. Medium damage rate ("dmid5.dat dmid3.dat for the 5' end and the 3' end deamination done by gargammel") was taken from Olalde, Iñigo, et al. "Derived immune and ancestral pigmentation alleles in a 7,000-year-old Mesolithic European." Nature 507.7491 (2014): 225-228.
3. No damage rate ("none5.dat none3.dat for the 5' end and the 3' end deamination done by gargammel"). 


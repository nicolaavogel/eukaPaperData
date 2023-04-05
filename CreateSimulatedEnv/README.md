# Construction of simulated metagenomic environmnents

Our simulated metagenomic environments are created with a Snakemake pipeline. 
We provide a list of NCBI accesssion numbers from which we sampled for the contaminants (Bacteria.list, Virus.list, Plants.list, Archaea.list, Fungi.list), the nuclear contaminants (Nuclear_genomes.list) and the endogenous mitochondiral genomes (Mitochondiral_genomes.list). 

Additionally, we provide the damage profiles used to simulate the three levels of damage.
1. High damage rate ("dhigh5.dat and dhigh3.dat for the 5' end and the 3' end deamination done by gargammel") was taken from Günther, Torsten, et al. "Ancient genomes link early farmers from Atapuerca in Spain to modern-day Basques." Proceedings of the National Academy of Sciences 112.38 (2015): 11917-11922.
2. Medium damage rate ("dmid5.dat dmid3.dat for the 5' end and the 3' end deamination done by gargammel") was taken from Olalde, Iñigo, et al. "Derived immune and ancestral pigmentation alleles in a 7,000-year-old Mesolithic European." Nature 507.7491 (2014): 225-228.
3. No damage rate ("none5.dat none3.dat for the 5' end and the 3' end deamination done by gargammel"). 

The files used in the simulation experiments can be downloaded via our ftp server:

### For all simulated metagenomic environments with all levels of simulated ancient damage: 
```
wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/*
```

To download the individual files of the cave environment based on Pedersen, Mikkel Winther, et al. "Environmental genomics of Late Pleistocene black bears and giant short-faced bears." Current Biology 31.12 (2021): 2728-2736. and Ardelean, Ciprian F., et al. "Evidence of human occupation in Mexico around the Last Glacial Maximum." Nature 584.7819 (2020): 87-92.
```
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/cave_high_damage.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/cave_mid_damage.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/cave_no_damage.pp.fq.gz
```

To download the individual files of the cave environment with human presence based on Gelabert, Pere, et al. "Genome-scale sequencing and analysis of human, wolf, and bison DNA from 25,000-year-old sediment." Current biology 31.16 (2021): 3564-3574.
```
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/human_cave_high.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/human_cave_mid.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/human_cave_no.pp.fq.gz
```

To download the individual files of the permaforst environment based on Murchie, Tyler J., et al. "Collapse of the mammoth-steppe in central Yukon as revealed by ancient environmental DNA." Nature Communications 12.1 (2021): 7120. and Murchie, Tyler J., et al. "Pleistocene mitogenomes reconstructed from the environmental DNA of permafrost sediments." Current Biology 32.4 (2022): 851-860.
```
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/perma_high_damage.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/perma_mid_damage.pp.fq.gz
 wget ftp://ftp.healthtech.dtu.dk:/public/simulation_data/perma_no_damage.pp.fq.gz
```

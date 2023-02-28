HOME="/home/projects/animalia_mito/scripts/db_construction"

rule all:
    input: "$HOME/final.txt"


rule ava_genera:
    input: "/home/projects/animalia_mito/tools/penv/test_taxa.tab"
    output: " $HOME/arthro_genus.txt", " $HOME/tetra_genus.txt"
    shell: "python genus_list.py" 

rule download_artho_mitogenomes:
    input: " $HOME/arthro_genus.txt"
    output: " $HOME/downloaded_artho_genus.txt"
    shell: """python download_input.py --path {input} --search "Artho" --type "Arthopoda" > artho_down.out"""  

rule download_tetra_mitogenomes:
    input: " $HOME/tetra_genus.txt"                                  
    output:  " $HOME/downloaded_tetra_genus.txt"
    shell: """python download_input.py --path {input} --search "Tetra" --type "Tetrapoda" > tetra_down.out"""

rule combine_lists:
    input: " $HOME/arthro_genus.txt", " $HOME/tetra_genus.txt"
    output: " $HOME/ava_genus.txt" 
    shell: "cat {input} > {output}"

rule clean_up_genera:
    input: " $HOME/ava_genus.txt"
    output:
    shell: "python clean_up_genera.py {input}"

rule get_all_fasta:
    input: " $HOME/ava_genus.txt"
    output: " $HOME/complete.fa.gz"
    shell: "./fasta_sum.sh"

rule make_mapping_file:
    input: " $HOME/db_seqs.fa.gz"
    output: " $HOME/db_seqs.mapping"
    shell: "python make_contaminator_mapping.py"

rule check_for_contamination:
    input: " $HOME/db_seqs.mapping"
    output: 
    shell: "/home/ctools/conterminator/conterminator dna db_seqs.fa.gz {input} db_seqs tmp"

rule gen_to_fam:
    input: " $HOME/ava_genus.txt"
    output: " $HOME/ava_family.txt"
    shell: "python gen_to_fam.py {input}"

rule check_families:
    input: " $HOME/ava_family.txt"
    output:
    shell: "python merge_dir.py -f {input} -n 10 -c 0"

rule merge_families:
    input: " $HOME/ava_family.txt"
    output:
    shell: "python merge_dir.py -f {input} -n 10 -c 1"

rule check_families2:
    input: " $HOME/ava_family.txt"
    output:
    shell: "python merge_dir.py -f {input} -n 5 -c 0"

rule get_all_new_taxa:
    input: " $HOME/ava_familiy.txt"
    output: " $HOME/ava_taxa.txt"
    shell: "ls /home/projects/animalia_mito/data > ava_taxa.txt"

rule rotation:
    input: " $HOME/ava_taxa.txt"
    output:
    shell: "./clean_and_rotate.sh"

rule pairwise_alignment:
    input: " $HOME/ava_taxa.txt"
    output: 
    shell: "./pairwise_alignment_clean.sh"

rule run_prank: 
     input: " $HOME/ava_taxa.txt"
     output:
     shell: "./run_prank_ancestral.sh"

rule construct_and_circ_vg:
     input: " $HOME/ava_taxa.txt"
     output: " $HOME/final.txt"
     shell: "./vg_const_circ.sh"

# this rule needs to be exectued only if the taxonomic groups for the database change.
# The resulting output file "new_all_clades will print out the list of all taxa to use as input for the next two rules."
#rule combine_vg:
#     input: " $HOME/ava_taxa.txt"
#     output: " $HOME/new_combo.txt"
#     shell: "./vg_combine.sh"


rule manipulate_vg_ids:
    input: 
    output:
    shell: "./vg_manipulate_ids.sh"

# create additional files used for euka:
rule make_look_up_dic:
    input: " $HOME/ava_taxa.txt"
    output: " $HOME/look_up.pk"
    shell: "python create_look_up_dic.py {input}"
rule get_group_info:
    input: " $HOME/ava_taxa.txt"
    output: "/home/projects/animalia_mito/vgan_dev/share/euka_dir/clade_information.csv"
    shell: "python assign_fam_name_to_graph.py {input} > {output}"
rule get_bins:
    input: " $HOME/ava_taxa.txt"
    output: "/home/projects/animalia_mito/vgan_dev/share/euka_dir/euka_db.bin"
    shell: "python get_bins.py {input}"

rule combine_vg:
    input: 
    output: " $HOME/euka_db.vg"
    shell: "./vg_combine_all.sh"  


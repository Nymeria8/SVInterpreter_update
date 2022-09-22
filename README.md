# SVInterpreter database update

## MGI BD update

1. Download the "MGI_PhenoGenoMP.rpt" file from http://www.informatics.jax.org/downloads/reports/index.html

2. Download the "mp.owl" file from https://www.ebi.ac.uk/ols/ontologies/mp

3. Run:
   
   <pre><code>python3 make_mgi_bd.py MGI_PhenoGenoMP.rpt mp.owl > mgi_formated_bd
   </code></pre>

## Pannel list

1. Go to the panelapp website [Genes and Genomic Entities](https://panelapp.genomicsengland.co.uk/panels/entities/) and download all the genes from the table

2. Transform those genes into a txt file, list of genes, one per line (gene_list.txt)

3. Run:
   
   ```
   python3 panelapp.py genes_list.txt > panel_list
   ```

## Rat Genome Database

1. Download the file GENES.RAT.txt from [Index of /data_release](https://download.rgd.mcw.edu/data_release/)

2. Run:
   
   ```
   python3 make_rat_bd.py GENES.RAT.txt > rat_formated_bd
   ```

## Wormbase Database

1. Download disease_association.WS285.daf.txt.c_elegans [Index of /species/c_elegans/annotation/disease_association](https://downloads.wormbase.org/species/c_elegans/annotation/disease_association/) 

2. Download the DOID.owl annotation file from https://www.ebi.ac.uk/ols/ontologies/doid

3. Run:

```
python3 make_wormbase_bd.py disease_association.WS285.daf.txt.c_elegans doid.owl > wormbase_formated_bd
```

## Zfin Database

1. Download https://zfin.org/downloads/gene2DiseaseViaOrthology.txt

2. Download the DOID.owl annotation file from https://www.ebi.ac.uk/ols/ontologies/doid

3. Run:

```
python3 zfin_create.py gene2DiseaseViaOrthology.txt  doid.owl > zfin_formated_bd
```





























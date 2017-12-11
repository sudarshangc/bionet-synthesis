## FOR GIT REPOSITORY -- Sorting Sequencing files
## Read in a sequencing data and copy the files to the gene directory that they are associated with

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import json
import os
import glob
import re

import shutil

from Bio import pairwise2
from Bio import AlignIO
from Bio import Align
from Bio import Seq
from Bio import SeqRecord
from Bio.Alphabet import generic_dna

for file in glob.glob("./gene_id_dict.json"):
        print(file)
        with open(file,"r") as json_file:
            print(json_file)
            dictionary = json.load(json_file)

#State the primers
forward_primer = "M13-Forward---20-"
reverse_primer = "M13-Reverse"

for seqfile in glob.glob("../Sequencing files/*/*.ab1"):
    print(seqfile)
    print(seqfile[55])

    if seqfile[55] == "-":
        initials, order_number, plate_number, well_number, hyphen, sample_name, primer_name, well_address = re.match(
            r'.*/([A-Z]+)_([0-9]+)-([0-9])([0-9]+)_(-)([A-Za-z0-9_-]+)_([A-Za-z0-9-]+)_([A-H][0-9]{2}).ab1',
            seqfile).groups()
        revfile = "{}/{}_{}-{}{}_{}{}_{}_{}.ab1".format(os.path.dirname(seqfile), initials, order_number, (int(plate_number)+1), well_number, hyphen, sample_name, reverse_primer, well_address)
    else:
        initials, order_number, plate_number, well_number, sample_name, primer_name, well_address = re.match(
            r'.*/([A-Z]+)_([0-9]+)-([0-9])([0-9]+)_([A-Za-z0-9_-]+)_([A-Za-z0-9-]+)_([A-H][0-9]{2}).ab1',
            seqfile).groups()
        revfile = "{}/{}_{}-{}{}_{}_{}_{}.ab1".format(os.path.dirname(seqfile), initials, order_number, (int(plate_number)+1), well_number, sample_name, reverse_primer, well_address)

    print(sample_name)
    split = sample_name.rsplit('_')
    gene = split[0] + "_" + split[1]

    if 'link' in gene:
        print('link')
        gene = gene[:11]

    if gene not in dictionary:
        continue

    print(gene)

    name = dictionary[gene]
    print(name)

    shutil.copy(seqfile, '../Data/{}'.format(name))
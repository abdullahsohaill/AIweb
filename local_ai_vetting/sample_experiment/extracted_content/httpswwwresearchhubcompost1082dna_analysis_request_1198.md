# https://www.researchhub.com/post/1082/dna-analysis-request-mexico-uap-genomics-data/bounties
**URL:** https://www.researchhub.com/post/1082/dna-analysis-request-mexico-uap-genomics-data/bounties
**Page Title:** [DNA Analysis Request] Mexico UAP Genomics Data - Bounties | ResearchHub
--------------------


## Question

## Question

[LINK: Issues](https://github.com/ResearchHub/issues/issues/new/choose)
[LINK: Docs](https://docs.researchhub.com/)

## [DNA Analysis Request] Mexico UAP Genomics Data

## Earning Opportunity

5. Assemble the DNA reads into contigs and scaffolds using de novo assembly methods
Open-ended here
Hi. I was able to finish assembly for one the samples (SRR20458000). I used Megahit to assemble the contigs. ( https://www.researchhub.com/paper/1282014/megahit-an-ultra-fast-single-node-solution-for-large-and-complex-metagenomics-assembly-via-succinct-de-bruijn-graph ). The contig itself is a very small file ( 80Mb ), so when compared to actual datasets, this was very surprising. Most of this sample consists of Proteobacteria species, along with other metagenome species.
What's even more interesting is that this sample produces a 80G SAM file, which is significantly bigger than the said contig file. To put this in perspective, I have recently finished processing multiple soil and aqua samples (each have size around 100G for paired-end files). These environmental samples produce contigs much larger and of better quality than this said sample. Another thing to note, when I did a word count of all the contigs in this  sample and compared to my environmental samples, I found that my environm ...
Another question I had was, do we have to finish processing all 3 samples to be eligble for the bounty? As I mentioned in one my my previous posts, I am new to RH and this my first bounty hunt. Was wondering how the system works!!
Also, if anyone wanted access to my results,  I can surely have them sent. For some reason, I was not being able to upload files to my post. I also have other results which my pipeline can generate, such as EC and GO number mapping with the contigs, and protein level mapping.

## Earning Opportunity

4. Align the reads to the human reference genome (hg38) to compare the reads against the human genome
e.g. bowtie2 or other aligner
[Comment removed]

## Earning Opportunity

3. Run a microbial contaminant subtraction method
It is typical to see microbial contaminants added in the process or sample itself

## Earning Opportunity

Piggybacking off of this bounty for read QC: pre-register a robust statistical plan with references and controls for how you'll test whether the reads are simulated or otherwise manipulated.

## Earning Opportunity

2. Conduct Basic Local Alignment Search Tool (BLAST) to search for the sequences in the reads against a large genomic database
Check for matches against known species
[Comment removed]
Hi @Amir hamza khan ,
You can surely find the data sets at https://www.ncbi.nlm.nih.gov/ under the project numbers mentioned in the original post. Here are the links to the same:
1: https://www.ncbi.nlm.nih.gov/sra/PRJNA861322
2: https://www.ncbi.nlm.nih.gov/sra/PRJNA869134
3: https://www.ncbi.nlm.nih.gov/sra/PRJNA865375
You can go to these pages to look for the SRA ID (generally it goes like SRRxxxxx). I used fastq to get the datasets.
fastq-dump --split-files SRR20458000
fastq-dump --split-files SRR20755928
fastq-dump --split-files SRR21031366
WARNING: These are pretty large datasets. So my suggestion would be make sure you have enough memory. Each of these files are roughly around 300Gb. So there is that!!
Also, as far as your question regarding BlastP/BlastN, I would assume it's BlastN, since the bounty says "to search for the sequences in the reads against a large genomic database". Nevertheless, I think BlastP would also be a good try, especially to see how the proteins line up when compare ...
[Comment removed]
NCBI provides an analysis of the taxonomy of the reads in the archive if that is what you are after. It hints to what is in the data set, but it is not comprehensive since it only includes comparisons to Refseq genomes (for example, no woolly monkey Refseq genome exists and so it would not be identifiable with this method). Follow the link for each project. In the bottom table under Run, there is a link to the SRR#. The default tab is metadata and the second tab is the taxonomy.  I did no work for this, so not seeking any bounty. The analysis is not BLAST based. Here is a link to how the analysis was done: https://www.ncbi.nlm.nih.gov/sra/docs/sra-taxonomy-analysis-tool/
[LINK: https://www.ncbi.nlm.nih.gov/sra/docs/sra-taxonomy-analysis-tool/](https://www.ncbi.nlm.nih.gov/sra/docs/sra-taxonomy-analysis-tool)
Hopefully someone can do better and claim the bounty. Here are partial screenshots of the analyses:

## Earning Opportunity

- Check the quality of the reads
Checking with something like fastqc and other tools to check the quality and whether the reads were simulated or legitimate.
I was able to complete quality control with the help of FastQC similar to ﻿@Kiran Arshad﻿post pre-processing using BBTools. (https://www.researchhub.com/post/1082/dna-analysis-request-mexico-uap-genomics-data/conversation#threadId=39783)Looking at the results, most of the data looks highly contaminated. Basically, these said 'mummies' have been exposed to so much environmental contamination, that finding actual genome belonging to these 'aliens' would be a tough ask. I have worked with Ancient DNA before (Wolly Mammoth), and even though the GC % was low, there were still significant traces of WM DNA along with loads of microbial communities. Another arguement would be, that any one can create a 300G file just by taking 2-3 sequences from each sample in NCBI and compiling them together. But we cannot be sure.The issue is, just because we cannot disprove something doesn't also mean we can prove that these data sets were simulated. However, based on experience, it is easy to say that most ...
Did you do some sort of trimming of the low-quality reads?
[Comment removed]

## More

[LINK: Issues](https://github.com/ResearchHub/issues/issues/new/choose)
[LINK: Docs](https://docs.researchhub.com/)

--------------------
# DeepMind's AlphaFold
**URL:** https://alphafold.ebi.ac.uk
**Page Title:** AlphaFold Protein Structure Database
--------------------


## AlphaFold Protein Structure Database

## AlphaFold Protein Structure Database

## AlphaFold Protein Structure Database

Developed by Google DeepMind and EMBL-EBI

### Background

AlphaFold is an AI system developed by Google DeepMind that predicts a protein’s 3D structure from its amino acid sequence. It regularly achieves accuracy competitive with experiment.
Google DeepMind and EMBL’s European Bioinformatics Institute ( EMBL-EBI ) have partnered to create AlphaFold DB to make these predictions freely available to the scientific community. The latest database release contains over 200 million entries, providing broad coverage of UniProt (the standard repository of protein sequences and annotations). We provide individual downloads for the human proteome and for the proteomes of 47 other key organisms important in research and global health. We also provide a download for the manually curated subset of UniProt ( Swiss-Prot ).
Q8I3H7: May protect the malaria parasite against attack by the immune system. Mean pLDDT 85.57.
View protein
In CASP14 , AlphaFold was the top-ranked protein structure prediction method by a large margin, producing predictions with high accuracy . While the system still has some limitations , the CASP results suggest AlphaFold has immediate potential to help us understand the structure of proteins and advance biological research.
Let us know how the AlphaFold Protein Structure Database has been useful in your research, or if you have questions not answered in the FAQs, at alphafold@deepmind.com .
If your use case isn't covered by the database, you can generate your own AlphaFold predictions using this open source code , which also supports multimer prediction.
[LINK: open source code](https://github.com/deepmind/alphafold/)
Q8W3K0: A potential plant disease resistance protein. Mean pLDDT 82.24.
View protein

### Find out more

### What’s new?

Custom annotations - November 2025
We introduce a new functionality that enables users to integrate and visualise custom sequence annotations. This is made possible through the integration a protein feature web visualisation component.
The new feature, located on the "Annotations" tab, allows researchers to input single-residue annotations and region annotations. Custom annotations are visible on the 2D and 3D tracks, and alongside the predicted Local Distance Difference Test (pLDDT) score track.
Read full article on EMBL-EBI site
AF-P42684-F1: Tyrosine-protein kinase ABL2
View protein

### What’s next?

We plan to continue updating the database with structures for newly discovered protein sequences, and to improve features and functionality in response to user feedback. Please follow Google DeepMind 's and EMBL-EBI ’s social channels for updates.

### Licence and attributions

Data is available for academic and commercial use, under a CC-BY-4.0 licence.
EMBL-EBI expects attribution (e.g., in publications, services, or products) for any of its online services, databases, or software in accordance with good scientific practice.
If you use this resource, please cite the following papers:
Fleming J. et al. AlphaFold Protein Structure Database and 3D-Beacons: New Data and Capabilities. Journal of Molecular Biology, (2025)
If you use data from AlphaMissense in your work, please cite the following paper:
Cheng, J et al. Accurate proteome-wide missense variant effect prediction with AlphaMissense. Science (2023).
AlphaFold Data Provided by GDM:
AlphaFold Data Copyright (2022) DeepMind Technologies Limited.
AlphaMissense Copyright (2023) DeepMind Technologies Limited.

### FAQs

### How does AlphaFold work?

DeepMind’s 2021 methods paper is the best reference for this. It gives an overview of the most important ideas, and there is a detailed description of all aspects of the system in the Supplementary Information. Note that the architecture of the system used at CASP14 differs significantly from the version used at CASP13, making it important to refer to the 2021 publication. Visit our online training course to learn more about AlphaFold.
DeepMind’s 2021 methods paper is the best reference for this. It gives an overview of the most important ideas, and there is a detailed description of all aspects of the system in the Supplementary Information. Note that the architecture of the system used at CASP14 differs significantly from the version used at CASP13, making it important to refer to the 2021 publication.
Visit our online training course to learn more about AlphaFold.

### What is AlphaMissense?

AlphaMissense is an AI model that builds on Google DeepMind’s AlphaFold2 to categorise ‘missense’ mutations in different proteins as either ‘likely pathogenic’, ‘likely benign’ or ‘uncertain’, producing a score that estimates the likelihood of a variant being pathogenic. AlphaMissense leverages AlphaFold2’s capability to model protein structure, and its capacity to learn evolutionary constraints from related sequences. The implementation is closely aligned with AlphaFold2, with some architectural differences. AlphaMissense was used to classify the effects of all possible 216 million single amino acid sequence substitutions across the 19,233 canonical human proteins. Using an amino acid sequence as an input, AlphaMissense: Gives an indication of which mutations are more likely to underlie human diseases - such as rare genetic disorders or developmental diseases - by categorising missense mutations into likely pathogenic or likely benign. Combined with other types of information, it can help to decipher what mutations may be causing a disease. Helps to highlight potential functionally important regions of the protein. Note that AlphaMissense does not predict the change in protein structure, or biophysical properties such as stability, upon mutation. Instead, it uses related protein sequences and protein structure as contextual information to estimate pathogenicity. For more information about AlphaMissense, please refer to the paper: Accurate proteome-wide missense variant effect prediction with AlphaMissense. Science (2023). AlphaMissense scores for all human missense variants are available on the Google Cloud Public Dataset .
AlphaMissense is an AI model that builds on Google DeepMind’s AlphaFold2 to categorise ‘missense’ mutations in different proteins as either ‘likely pathogenic’, ‘likely benign’ or ‘uncertain’, producing a score that estimates the likelihood of a variant being pathogenic. AlphaMissense leverages AlphaFold2’s capability to model protein structure, and its capacity to learn evolutionary constraints from related sequences. The implementation is closely aligned with AlphaFold2, with some architectural differences.
AlphaMissense was used to classify the effects of all possible 216 million single amino acid sequence substitutions across the 19,233 canonical human proteins.
Using an amino acid sequence as an input, AlphaMissense:
- Gives an indication of which mutations are more likely to underlie human diseases - such as rare genetic disorders or developmental diseases - by categorising missense mutations into likely pathogenic or likely benign. Combined with other types of information, it can help to decipher what mutations may be causing a disease.
- Helps to highlight potential functionally important regions of the protein.
Note that AlphaMissense does not predict the change in protein structure, or biophysical properties such as stability, upon mutation. Instead, it uses related protein sequences and protein structure as contextual information to estimate pathogenicity.
For more information about AlphaMissense, please refer to the paper: Accurate proteome-wide missense variant effect prediction with AlphaMissense. Science (2023).
AlphaMissense scores for all human missense variants are available on the Google Cloud Public Dataset .

### What if I can’t find the protein I’m interested in?

If you can’t find the structure you’re looking for, here are some suggestions to improve your search results: Try searching by protein or gene name rather than specific UniProt accession. If running a sequence search, the input query should contain at least 20 amino acids, and only standard amino acids are accepted. Check that the protein isn’t excluded by any of the criteria covered in a previous FAQ . The AlphaFold source code can be used to predict the structures of proteins not in the AlphaFold DB, which supports predicting multimer structures. If you experience any issues with search, please contact afdbhelp@ebi.ac.uk .
If you can’t find the structure you’re looking for, here are some suggestions to improve your search results:
- Try searching by protein or gene name rather than specific UniProt accession.
- If running a sequence search, the input query should contain at least 20 amino acids, and only standard amino acids are accepted.
- Check that the protein isn’t excluded by any of the criteria covered in a previous FAQ .
[LINK: source code](https://github.com/google-deepmind/alphafold)

### How can I download and use the Predicted Aligned Error (PAE) file?

The PAE is displayed as an interactive plot for each of the structure predictions. If you need the raw data with PAE for all residue pairs, you can download the PAE as a JSON file using the button at the top of the structure page. This file is in a custom format and it isn't supported by any existing software – you will have to use Python or another programming language to analyse or plot the information that is contained in it. For a protein of length num_res , the JSON file has the following structure of arrays format: [ { "predicted_aligned_error": [[0, 1, 4, 7, 9, ...], ...],  # Shape: (num_res, num_res). "max_predicted_aligned_error": 31.75 } ] The fields in the JSON file are: predicted_aligned_error : The PAE value of the residue pair, rounded to the closest integer. For the PAE value at position (i, j), i is the residue on which the structure is aligned, j is the residue on which the error is predicted. max_predicted_aligned_error : A number that denotes the maximum possible value of PAE. The smallest possible value of PAE is 0. We updated the PAE JSON file format on 28th July 2022 to reduce file size by 4x. Please ensure you read the 2D matrix of PAE values from the predicted_aligned_error field instead of the removed 1D "distances" field and avoid using the old "residue1" and "residue2" fields. If you are using a script or third party tool to read the PAE JSON file programmatically and you are seeing errors (e.g. missing field "distance"), check with the author of the program whether the latest PAE JSON format is supported.
The PAE is displayed as an interactive plot for each of the structure predictions. If you need the raw data with PAE for all residue pairs, you can download the PAE as a JSON file using the button at the top of the structure page.
This file is in a custom format and it isn't supported by any existing software – you will have to use Python or another programming language to analyse or plot the information that is contained in it.
The fields in the JSON file are:
- predicted_aligned_error : The PAE value of the residue pair, rounded to the closest integer. For the PAE value at position (i, j), i is the residue on which the structure is aligned, j is the residue on which the error is predicted.
- max_predicted_aligned_error : A number that denotes the maximum possible value of PAE. The smallest possible value of PAE is 0.
We updated the PAE JSON file format on 28th July 2022 to reduce file size by 4x. Please ensure you read the 2D matrix of PAE values from the predicted_aligned_error field instead of the removed 1D "distances" field and avoid using the old "residue1" and "residue2" fields.
If you are using a script or third party tool to read the PAE JSON file programmatically and you are seeing errors (e.g. missing field "distance"), check with the author of the program whether the latest PAE JSON format is supported.

### Who should I contact with enquiries?

For sharing feedback on structure predictions, please use the feedback buttons on each structure page. For other questions about AlphaFold not directly related to the database, please contact the AlphaFold team at alphafold@deepmind.com .  Please do not share anything confidential with Google DeepMind. For questions and feedback about the AlphaFold DB website, please contact afdbhelp@ebi.ac.uk . For press enquiries, please contact press@deepmind.com or comms@ebi.ac.uk .
For sharing feedback on structure predictions, please use the feedback buttons on each structure page.
For other questions about AlphaFold not directly related to the database, please contact the AlphaFold team at alphafold@deepmind.com .  Please do not share anything confidential with Google DeepMind.
For questions and feedback about the AlphaFold DB website, please contact afdbhelp@ebi.ac.uk .
For press enquiries, please contact press@deepmind.com or comms@ebi.ac.uk .
View all frequently asked questions

### EMBL-EBI training

Recorded webinar

### Accessing and interpreting predicted protein structures from AlphaFold database

Online tutorial

### AlphaFold


--------------------
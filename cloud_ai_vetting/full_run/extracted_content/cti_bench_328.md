# CTI-Bench
**URL:** https://huggingface.co/datasets/AI4Sec/cti-bench
**Page Title:** AI4Sec/cti-bench · Datasets at Hugging Face
--------------------


## Dataset Card for CTIBench

A set of benchmark tasks designed to evaluate large language models (LLMs) on cyber threat intelligence (CTI) tasks.

## Dataset Details

### Dataset Description

CTIBench is a comprehensive suite of benchmark tasks and datasets designed to evaluate LLMs in the field of CTI.
Components:
- CTI-MCQ: A knowledge evaluation dataset with multiple-choice questions to assess the LLMs' understanding of CTI standards, threats, detection strategies, mitigation plans, and best practices. This dataset is built using authoritative sources and standards within the CTI domain, including NIST, MITRE, and GDPR.
CTI-MCQ: A knowledge evaluation dataset with multiple-choice questions to assess the LLMs' understanding of CTI standards, threats, detection strategies, mitigation plans, and best practices. This dataset is built using authoritative sources and standards within the CTI domain, including NIST, MITRE, and GDPR.
- CTI-RCM: A practical task that involves mapping Common Vulnerabilities and Exposures (CVE) descriptions to Common Weakness Enumeration (CWE) categories. This task evaluates the LLMs' ability to understand and classify cyber threats.
CTI-RCM: A practical task that involves mapping Common Vulnerabilities and Exposures (CVE) descriptions to Common Weakness Enumeration (CWE) categories. This task evaluates the LLMs' ability to understand and classify cyber threats.
- CTI-VSP: Another practical task that requires calculating the Common Vulnerability Scoring System (CVSS) scores. This task assesses the LLMs' ability to evaluate the severity of cyber vulnerabilities.
CTI-VSP: Another practical task that requires calculating the Common Vulnerability Scoring System (CVSS) scores. This task assesses the LLMs' ability to evaluate the severity of cyber vulnerabilities.
- CTI-TAA: A task that involves analyzing publicly available threat reports and attributing them to specific threat actors or malware families. This task tests the LLMs' capability to understand historical cyber threat behavior and identify meaningful correlations.
CTI-TAA: A task that involves analyzing publicly available threat reports and attributing them to specific threat actors or malware families. This task tests the LLMs' capability to understand historical cyber threat behavior and identify meaningful correlations.
- Curated by: Md Tanvirul Alam & Dipkamal Bhusal (RIT)
Curated by: Md Tanvirul Alam & Dipkamal Bhusal (RIT)

### Dataset Sources

Repository: https://github.com/xashru/cti-bench
[LINK: https://github.com/xashru/cti-bench](https://github.com/xashru/cti-bench)

## Uses

CTIBench is designed to provide a comprehensive evaluation framework for large language models (LLMs) within the domain of cyber threat intelligence (CTI). 
Dataset designed in CTIBench assess the understanding of CTI standards, threats, detection strategies, mitigation plans, and best practices by LLMs, 
and evaluates the LLMs' ability to understand, and analyze about cyber threats and vulnerabilities.

## Dataset Structure

The dataset consists of 5 TSV files, each corresponding to a different task. Each TSV file contains a "Prompt" column used to pose questions to the LLM. 
Most files also include a "GT" column that contains the ground truth for the questions, except for "cti-taa.tsv". 
The evaluation scripts for the different tasks are available in the associated GitHub repository.

## Dataset Creation

### Curation Rationale

This dataset was curated to evaluate the ability of LLMs to understand and analyze various aspects of open-source CTI.

### Source Data

The dataset includes URLs indicating the sources from which the data was collected.
The dataset does not contain any personal or sensitive information.

## Citation

The paper can be found at: https://arxiv.org/abs/2406.07599
BibTeX:

## Dataset Card Contact

Md Tanvirul Alam (ma8235 @ rit . edu)

## Paper for AI4Sec/cti-bench


--------------------
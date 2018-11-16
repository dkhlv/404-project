# Searchable encryption based on fuzzy matching

This project demonstrates searchable encryption method based on fuzzy keyword search. 

Workflow is based on 2010 paper "Fuzzy Keyword Search over Encrypted Data in Cloud Computing" by Jin Li et al. Paper can be found here: https://ieeexplore.ieee.org/document/5462196


### Prerequisites
- Python 3.6
- Cryptography package for Python can be installed by running
`pip install cryptography`


### Running steps
`python3 fuzzy_keyword_search.py`

### Explanation
When prompted for a query enter some keyword, for example "machine". The results should return all paper titles that match given keyword with edit distance = 1. For example, "machine" and "machinee" will both resolve to "machine" or "machines", but not "machinery". 

### Sample interaction
```
Enter your query:  machine

A set of fuzzy keywords: 
['*machine', '*achine', 'm*chine', 'ma*hine', 'mac*ine', 'mach*ne', 'machi*e', 'machin*', 'machine*']

Searching for results...

Server returned these encrypted file identifiers:

[b'gAAAAABa0-U_UQNFmppLRRC6boMQoGCcHr1msj6G4GA_58ENzbmjcvtycgAdZe4-TwoWyKfaSmgcZd3ezee7PHrXtSVINH7SmA==', b'gAAAAABa0-U_PtyyK76JcP0M6myjqimUwYrhJIBVe0_djTaSjuPh_fo8s395OiqXE_7q2jeCyagbIA68U5bp44N1YXGzqXJBPQ==', b'gAAAAABa0-VAfc1GWnWwVJtkQfOyu8T0OqrKAGXLRROOwQWHts1cxLzYRGTL-LsvjLRbcplZUespI0yXO2MiWIxg7A7i2hzz7Q==', b'gAAAAABa0-VAyIetzvw1l8SwruO_flA9hIocl2DABArptml3dn3YH9vtOnSlMAFB-CGQqtAVUYlx_RNpInhn-c6MOaBwq-xF6w==', b'gAAAAABa0-VBOcWt9yJcswq4cK_7tfzRvPXn0WlbzupAGAvU186FP_ANA_sGOSFbcnfUuSP9--uslGfy9ecF1nve2GSoLK6amQ==', b'gAAAAABa0-VB6fLa7icczH-jywTy9_L7RDVLFCITKhP7VJGmLKg0gIBRiiRgOVy5gc2LxveMRUnF7GgzkKJ51-ZtIby3-G4CWQ==', b'gAAAAABa0-VCQpXnthrp8fpS8oZDKxBaGiPlGFVsjlYYGehsEh7RWnFs-v9boabWkaW6B1vcpvjbxCskRdgFE8vDSbb7hGDejA==', b'gAAAAABa0-VCG0PzUit4XW9r6KZUlGhOoL0akKd-9WRR56XHUmSTcQbQJZE7gwZ5aZS0Kb0RuEm9cbvYjdGs7YA5oQQH2YJ5hQ==', b'gAAAAABa0-VCkhQ3aCf8R3t032Ru9r9VcmLhnqk8IiBDGIQ07Spi9Pm3I8mKi9QZykQr3-1OxRyhYlJfmQsJ7bhZlfdcHctVFg==']

Decrypted file identifiers:

[b'machine,6', b'machine,47', b'machine,88', b'machines,150', b'machine,228', b'machine,246', b'machine,297', b'machine,297', b'machine,305']


Here are the results that match your query "machine":

Discovering Better AAAI Keywords via Clustering with Crowd-sourced Constraints
Active Learning with Model Selection via Nested Cross-Validation
A Machine Learning Approach to Musically Meaningful Homogeneous Style Classification
Learning with Augmented Class by Exploiting Unlabeled Data
Efficient codes for inverse dynamics during walking
GenEth: A General Ethical Dilemma Analyzer
Machine Translation with Real-time Web Search
Partial Multi-View Clustering

```

### About dataset
There are two datasets available for examination. 

1. unencrypted_data.csv is an 
AAAI 2014 Accepted Papers Data Set downloaded from https://archive.ics.uci.edu/ml/datasets/AAAI+2014+Accepted+Papers. 

2. index.csv is an encrypted index table containing all encrypted fuzzy keywords as keys and matching encrypted file identifiers as values. Construction of the index is described in the algorithm.

Users may want to examine both datasets for a comparison.
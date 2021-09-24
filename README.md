# PatientFORUM

**>> see [Website](https://sap218.github.io/patientFORUM) for more information about the project**

- **PatientFORUM (+ClinicalBERT) `patientforum+clinical.model`**: retrained ClinicalBERT embedding model with patient forum conversation 

- **PatientFORUM `patientforum.model`**: trained model from same forum conversations using same method/parameters as ClinicalBERT

---

## Brief Overview

1a. extracted patient forum conversations from [Patient.info](https://patient.info/forums) using inflammatory conditions, via Python package `BeautifulSoup` [1]

1b. downloaded [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) Word2Vec model - ClinicalBERT [2] is based on MIMIC-III [3] clinical letters of patients of intesive care

2a. trained model PatientFORUM **`patientforum.model`** from forum conversations using same method/parameters as ClinicalBERT, via Python package `Gensim` [4]

2b. retraining ClincalBERT with same forum conversations to create PatientFORUM (+ClinicalBERT) **`patientforum+clinical.model`**

3a. created a basic applicaiton ontology, Combined Ontology for Inflammatory Diseases ([COID](https://github.com/sap218/coid/)) [5] and expanded with the same tf-idf methods as Pendleton et al. (2021) [6] in addition to further expansion from the PatientFORUM (+ClinicalBERT) word embeddings

3b. manuscript analysis: Pearson/Wilcoxon comparisons of all three models, clustering, and synonym analysis via ROC AUC

---

### 1. Forum extraction script (`forum_extraction_scripts/` directory)
- includes the forum extraction instructions, examples provided with inflammatory topics used for embeddings in `forum_extraction_scripts/inflammation_topics/` directory (includes the date of extraction of the inflammatory terms of interest used in the Word2Vec models)

**Question: am I allowed to do this? Answer: yes**

"*As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users.*" - Patient team from [Patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private/remove scripts. Please respect the Patient team and the users' privacy. 

**version 10/02/2020** - works as of this date, in future website may change and so the script might not work!

### 2. Training Word2Vec models (`embedding_model/` directory)
- PatientFORUM: `patientforum.model`
- PatientFORUM (+ClinicalBERT): `patientforum+clinical.model`
- there will be another directory here `data_processing/` to show how to train/retrain the models so anyone can perform this method of a forum of their choice, recreate our experiments, or expand upon our models and create a pull-request

**version 23/09/2021**

---

## References

[1] Richardson L. Beautiful Soup Documentation. 2007. `http://mde.tw/wcm2021/downloads/2019_beautifulsoup_document.pdf`.

[2] Huang K, Altosaar J, Ranganath R. Clinicalbert: Modeling clinical notes and predicting hospital readmission. arXiv preprint arXiv:1904.05342. 2019.

[3] Johnson AE, Pollard TJ, Shen L, Li-Wei HL, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, Mark RG. MIMIC-III, a freely accessible critical care database. Scientific data. 2016 3(1):1-9.

[4] Rehurek R, Sojka P. Gensim--python framework for vector space modelling. NLP Centre, Faculty of Informatics, Masaryk University, Brno, Czech Republic. 2011 3(2).

[5] Pendleton SC. Combined Ontology for Inflammatory Diseases COID. Zenodo. 2021. `https://doi.org/10.5281/zenodo.5524650`.

[6] Pendleton SC, Slater LT, Karwath A, Gilbert RM, Davis N, Pesudovs K, Liu X, Denniston AK, Gkoutos GV, Braithwaite T. Development and application of the ocular immune-mediated inflammatory diseases ontology enhanced with synonyms from online patient support forum conversation. Computers in biology and medicine. 2021 135:104542.


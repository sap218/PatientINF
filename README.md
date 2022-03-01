# PatientFORUM

**>> see [Website](https://sap218.github.io/patientFORUM) for more information about the project**

| Abbrev. | Full name | Source |
| --- | --- | --- |
| PI | PatientINF | [Patient.info](https://patient.info/forums) forum board |
| CB | ClinicalBERT | [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) [1] |
| mBR | (modified) BioReddit | [COMETA corpus](https://github.com/cambridgeltl/cometa) [2] |

---

## Brief Overview

1a. extracted patient forum conversations from [Patient.info](https://patient.info/forums) using inflammatory conditions, via Python package `BeautifulSoup` [3].

2a. downloaded [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) model - ClinicalBERT [1] is based on MIMIC-III [4] clinical letters of patients of intesive care.

2b. trained model **PatientINF** from forum conversations using same method/parameters as ClinicalBERT, via Python package `Gensim` [5].

2c. retraining ClincalBERT with same forum conversations to create **ClinicalBERT + PatientINF**.

3a. downloaded [COMETA](https://github.com/cambridgeltl/cometa) corpus - COMETA [2] is a subset of the BioReddit [6] corpus of 68 medical subreddits.

3b. trained model **mPatientINF** using same method/parameters as ClinicalBERT, via Python package `Gensim` [5].

3c. trained model **PatientINF** using same method/parameters as ClinicalBERT, via Python package `Gensim` [5].

analysis: Pearson/Wilcoxon comparisons of all three models, clustering, and synonym analysis via ROC AUC

**Additional**

- Created a basic applicaiton ontology, Combined Ontology for Inflammatory Diseases ([COID](https://github.com/sap218/coid/)) [7] and expanded with the same tf-idf methods as Pendleton et al. (2021) [8] in addition to further expansion from the PatientFORUM (+ClinicalBERT) word embeddings

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
- there will be another directory here `data_processing/` to show how to train/retrain the models so anyone can perform this method of a forum of their choice, recreate our experiments, or expand upon our models and create a pull-request.

**Note**: we used the CaStLeS Bear services at University of Birmingham [9] to extract forum, and perform majority of analysis.

*The computations described in this paper were performed using the University of Birmingham's BlueBEAR HPC service, which provides a High Performance Computing service to the University's research community. See `http://www.birmingham.ac.uk/bear` for more details.*

**version 23/09/2021**

---

## References



[1] Huang K, Altosaar J, Ranganath R. Clinicalbert: Modeling clinical notes and predicting hospital readmission. arXiv preprint arXiv:1904.05342. 2019.

[2] Basaldella, Marco, et al. "COMETA: A corpus for medical entity linking in the social media." arXiv preprint arXiv:2010.03295 (2020).

[3] Richardson L. Beautiful Soup Documentation. 2007. `http://mde.tw/wcm2021/downloads/2019_beautifulsoup_document.pdf`.

[4] Johnson AE, Pollard TJ, Shen L, Li-Wei HL, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, Mark RG. MIMIC-III, a freely accessible critical care database. Scientific data. 2016 3(1):1-9.

[5] Rehurek R, Sojka P. Gensim--python framework for vector space modelling. NLP Centre, Faculty of Informatics, Masaryk University, Brno, Czech Republic. 2011 3(2).

[6] Basaldella, Marco, and Nigel Collier. "BioReddit: Word embeddings for user-generated biomedical NLP." Proceedings of the Tenth International Workshop on Health Text Mining and Information Analysis (LOUHI 2019). 2019.

[7] Pendleton SC. Combined Ontology for Inflammatory Diseases COID. Zenodo. 2021. `https://doi.org/10.5281/zenodo.5524650`.

[8] Pendleton SC, Slater LT, Karwath A, Gilbert RM, Davis N, Pesudovs K, Liu X, Denniston AK, Gkoutos GV, Braithwaite T. Development and application of the ocular immune-mediated inflammatory diseases ontology enhanced with synonyms from online patient support forum conversation. Computers in biology and medicine. 2021 135:104542.

[9] Thompson SJ, Thompson SE, Cazier JB. CaStLeS (Compute and Storage for the Life Sciences): a collection of compute and storage resources for supporting research at the University of Birmingham. Zenodo. 2019 Jun 20.



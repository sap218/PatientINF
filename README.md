# PatientINF

**>> see [Website](https://sap218.github.io/patientFORUM) for more information about the project**

| Abbrev. | Full name | Source |
| --- | --- | --- |
| `PI` | PatientINF | [Patient.info](https://patient.info/forums) forum board |
| `CB` | ClinicalBERT | [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) [1] |
| `mBR` | (modified) BioReddit | [COMETA](https://github.com/cambridgeltl/cometa) corpus [2] |

**>> see HuggingFace for the [PatientINF](https://huggingface.co/sap218/PatientINF) CB+PI model**

## Brief Overview

1a. extracted patient forum conversations from [Patient.info](https://patient.info/forums) using inflammatory conditions, via Python package `BeautifulSoup` [3].

2a. downloaded `CB` model, which is based on MIMIC-III [4] clinical letters of patients of intesive care.

2b. trained model `PI` from forum conversations using same method/parameters as `CB` via Python package `Gensim` [5].

2c. retraining `CB` with same forum conversations to create `CB + PI`.

3a. downloaded COMETA corpus, which is a subset of the BioReddit [6] data of 68 medical subreddits.

3b. trained model `mBR` using same method/parameters as `CB`.

3c. trained model `PI` using same method/parameters as `CB`.

3d. retraining `mBR` with same forum conversations to create `mBR + PI`.

4a. analysis: t-SNE clustering, Pearson correlation with physician, Wilcoxon comparisons, and synonym analysis via ROC AUC.

**Additional**

- Created a basic applicaiton ontology, [Combined Ontology for Inflammatory Diseases](https://github.com/sap218/coid/) (`COID`) [7] and expanded with the same tf-idf methods as Pendleton et al. (2021) [8], using 14 inflammatory topics of interest. In addition to further expanding `COID` from the `CB + PI` word embeddings.

**Note**: we used the CaStLeS Bear services at University of Birmingham [9] to extract forum, and perform majority of analysis.

*The computations described in this paper were performed using the University of Birmingham's [BlueBEAR HPC](http://www.birmingham.ac.uk/bear) service, which provides a High Performance Computing service to the University's research community.*

---

### 1. Forum extraction script (`forum_extraction_scripts/` directory)
- includes the forum extraction instructions, examples provided with inflammatory topics used for embeddings in `forum_extraction_scripts/inflammation_topics/` directory (includes the date of extraction of the inflammatory terms of interest used in the Word2Vec models)

**Question: am I allowed to do this? Answer: yes**

"*As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users.*" - Patient team from [Patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private/remove scripts. Please respect the Patient team and the users' privacy. 

**version 10/02/2020** - works as of this date, in future website may change and so the script might not work!

### 2. Training fastText models (`embedding_models/` directory)
- ...

**Question: why not Word2Vec? Answer: n-grams**

The ability to retain n-gram informtion in the embedding model is important, specifically for the Pearson correlation experiment.

**version 01/03/2022**

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


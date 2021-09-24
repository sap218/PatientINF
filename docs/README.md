**>> see [SCENARIO](SCENARIO.md) for the working inflammatory project from the manuscript**

**>> see [GitHub](https://github.com/sap218/patientFORUM) for the PatientFORUM repository**

## About

- **PatientFORUM (+ClinicalBERT)**: retrained ClinicalBERT embedding model with patient forum conversation 

- **PatientFORUM**: trained model from same forum conversations using same method/parameters as ClinicalBERT

---

### Overview

In this project, we presented two novel Word2Vec embedding models dervived from the Patient Voice via patient forum conversations. We used [Patient.info](https://patient.info/forums) and extracted [1]  inflammatory topics of interest as many health conditions have an inflammatory response/properties. 

We downloaded [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) Word2Vec model [2], which is an embedding model based on MIMIC-III [3] clinical letters (patients in intesive care) and used their training parameters to train [4] the patient forum conversations into the PatientFORUM embedding model.

We then also created a second model, PatientFORUM (+ClinicalBERT) by retraining ClinicalBERT with the same patient forum conversations. 

Using all three models, ClinicalBERT, PatientFORUM, and PatientFORUM (+ClinicalBERT); we did some analysis and observed differences in clinical, layman, and mixed models. Additionally, using the Combined Ontology for Inflammatory Diseases ([COID](https://github.com/sap218/coid/)) [5] we expanded with the same tf-idf methods as Pendleton et al. (2021) [6] plus further expansion from the PatientFORUM (+ClinicalBERT) word embeddings.

To read more about the manuscript and our findings, see [inflammation](SCENARIO.md) page.

**version 23/09/2021**

### How you can get involved...

Community guidelines...

We provide instsuctions how to download your own forum topics of interest and to train/retrain models, how to recreate our experiments, or expand upon our models and create a pull-request.

---

### A note from the forum guidelines

**Question: am I allowed to do this? Answer: yes**

"*As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users.*" - Patient team from [Patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private/remove scripts. Please respect the Patient team and the users' privacy. 

**version 10/02/2020** - works as of this date, in future website may change and so the script might not work!

---

### References

[1] Richardson L. Beautiful Soup Documentation. 2007. `http://mde.tw/wcm2021/downloads/2019_beautifulsoup_document.pdf`.

[2] Huang K, Altosaar J, Ranganath R. Clinicalbert: Modeling clinical notes and predicting hospital readmission. arXiv preprint arXiv:1904.05342. 2019.

[3] Johnson AE, Pollard TJ, Shen L, Li-Wei HL, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, Mark RG. MIMIC-III, a freely accessible critical care database. Scientific data. 2016 3(1):1-9.

[4] Rehurek R, Sojka P. Gensim--python framework for vector space modelling. NLP Centre, Faculty of Informatics, Masaryk University, Brno, Czech Republic. 2011 3(2).

[5] Pendleton SC. Combined Ontology for Inflammatory Diseases COID. Zenodo. 2021. `https://doi.org/10.5281/zenodo.5524650`.

[6] Pendleton SC, Slater LT, Karwath A, Gilbert RM, Davis N, Pesudovs K, Liu X, Denniston AK, Gkoutos GV, Braithwaite T. Development and application of the ocular immune-mediated inflammatory diseases ontology enhanced with synonyms from online patient support forum conversation. Computers in biology and medicine. 2021 135:104542.

[7] Thompson SJ, Thompson SE, Cazier JB. CaStLeS (Compute and Storage for the Life Sciences): a collection of compute and storage resources for supporting research at the University of Birmingham. Zenodo. 2019 Jun 20.


# PatientFORUM

## Project

1. extracted patient forum conversations from [Patient.info](https://patient.info/forums) using inflammatory conditions
1b. downloaded [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) Word2Vec model - ClinicalBERT is based on MIMIC-III clinical letters (ICU)
2a. trained model PatientFORUM `patientforum.model` from forum conversations using same method/parameters as ClinicalBERT
2b. retraining ClincalBERT with same forum conversations to create PatientFORUM (+ClinicalBERT) `patientforum+clinical.model`
3. manuscript analysis: Pearson/Wilcoxon comparisons of all three models, clustering, and synonym analysis via ROC AUC (using the tf-idf method from Pendleton et al. (2021) we extract patient-preferred/layman terms and add to the [**COID**](https://github.com/sap218/coid/) ontology)

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

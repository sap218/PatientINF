# PatientFORUM

### Project
- extraction of forum [Patient.info](https://patient.info/forums) using inflammatory conditions, to create embedding model `PatientFORUM`
- creation of `PatientFORUM (+ClinicalBERT)` which is retrained [`ClinicalBERT`](https://github.com/kexinhuang12345/clinicalBERT) with the same patient forum conversations - `ClinicalBERT` is based on MIMIC-III clinical letters
- using the tf-idf method from Pendleton et al. (2021) we extract patient-preferred/layman terms and add to the [**COID**](https://github.com/sap218/coid/) ontology
- observed differences in all three models: Pearson correlation, ROC AUC, and clustering

### Word2Vec models (`embedding_model/` directory)
- `PatientFORUM.model` - dated: XXX
- `PatientFORUM-CLINICAL.model` - dated: XXX
- there will be another directory here `data_processing/` to show how to create `PatientFORUM` and retrain `ClinicalBERT` to create `PatientFORUM (+ClinicalBERT)` - so anyone can perform this method of a forum of their choice or recreate our experiments

### Inflammatory conditions of interest (`inflammation_topics/` directory)
- includes the date of extraction of the inflammatory terms of interest used in the Word2Vec models

### Forum extraction script (`forum_extraction_scripts/` directory)
- includes the forum extraction instructions

**am I allowed to do this? answer: yes**

"*As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users.*" - Patient team from [Patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private/remove scripts. Please respect the Patient team and the users' privacy. 

**version 10/02/2020** - works as of this date, in future website may change and so the script might not work!

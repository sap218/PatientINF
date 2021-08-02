# PatientBERT

### project

- extraction of forum from [patient.info](https://patient.info/forums) and using the tf-idf method from Pendleton et al. (2021) we extract patient-preferred/layman terms and add to the [**COID**](https://github.com/sap218/coid/) ontology

- application: using the [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) model on MIMIC-III clinical letters, we use to pretrain on inflammatory forum to observe differences in clinical and patient text

### word2vec model

- in the `embedding_model/` directory: `patientbert.bin` - dated: 28/01/2020
- there will be another directory here `data_processing/` to show how to pretrain ClinicalBERT with the forum - so anyone can perform this method of a forum of their choice

### inflammation of interest

- in the `inflammation_topics/` directory includes the date of extraction of the inflammatory terms of interest used in the word2vec model

### forum extraction script

- in the `forum_extraction_scripts/` directory includes the forum extraction instructions

**am I allowed to do this? answer: yes**

"*As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users.*" - Patient team from [patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private. Please respect the Patient team and the users' privacy. 

**version 10/02/2020** - works as of this date, in future website may change and so the script might not work!

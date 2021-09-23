## how to use

**version 23/09/2021**

- provided are scripts to train your own model, just like PatientFORUM
- or retrain a pre-existing model, e.g. ClinicalBERT to create PatientFORUM (+ ClinicalBERT)

### scripts

1. if you extracted your own forum using the scripts provided in `/patientFORUM/forum_extraction_scripts/`, then you need to use the output `patients-info_forums.json` with step 01a, you will get the output `forum_sentences_pretrain.txt` - this output file is important: you need this unformatted file for training your model

2a. **retraining ClinicalBERT to make PatientFORUM (+ ClinicalBERT)** use `forum_sentences_pretrain.txt` for Python script step02a, editing script will be needed in order to correct file inputs, you will get the output `patientforum+clinical.model`

2b. **training PatientFORUM** use `forum_sentences_pretrain.txt` for Python script step02b, editing script will be needed in order to correct file inputs, you will get the output `patientforum.model` - important to note that if you don't wish to involve ClinicalBERT at these steps, you will need to edit the script to avoid using same parameters as ClinicalBERT

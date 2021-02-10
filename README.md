# forum-patientinfo
extraction of [patient.info](https://patient.info/forums) forum discussions

- used for the **ufo** ontology (looking into inflammatory conditions)

## how to use

1. edit "chosen_topics.tsv" with the inflammatory topics and links you want to extract
2. run "top-level.py", which will export "chosen_topics_links.json" - these will include all the links for the threads from your desired topics
3. run "patients.py", which will export "patients-info_forums.json" - these will include all the threads (including title, posts, replies, users, dates, etc.) for all the thread links and topics you have chosen

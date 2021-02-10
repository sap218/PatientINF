# forum-patientinfo
extraction of [patient.info](https://patient.info/forums) forum discussions

- used for the **ufo** ontology (looking into inflammatory conditions)

## how to use

1. edit "chosen_topics.tsv" with the inflammatory topics and links you want to extract
2. run "top-level.py", which will export "chosen_topics_links.json" - these will include all the links for the threads from your desired topics
3. run "patients.py", which will export "patients-info_forums.json" - these will include all the threads (including title, posts, replies, users, dates, etc.) for all the thread links and topics you have chosen

## am I allowed to do this?

**answer: yes**

"As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users." - Patient team

## version

**10/02/2020** - works as of this date, in future website may change and so the script might not work

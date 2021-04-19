# forum-patientinfo

[patient.info](https://patient.info/forums)

- used for the [**UFO**](https://github.com/sap218/ufo/) ontology (looking into inflammatory conditions)

---

## Forum extraction Script

- in the `scripts/` directory

**how to use**

1. edit `chosen_topics.tsv` with the inflammatory topics and links you want to extract, two forum examples already provided
2. run `top-level.py`, which will export `chosen_topics_links.json` - these will include all the links for the threads from your desired topics/forums
3. run `patients.py`, this uses `chosen_topics_links.json` for all the thread links, it will export `patients-info_forums.json` - these will include all the threads (including title, posts, replies, users, dates, etc.) for all the thread links from the forum topics you have chosen

**am I allowed to do this? answer: yes**

*"As the forum discussions are openly accessible then it is is fine if you are just analysing posts. However, please note we do not allow posting of surveys, research requests etc so please do not post direct questions to any users."* - Patient team from [patient.info](https://patient.info/forums)

If I find out this is being abused, I will make repository private. Please respect the Patient team and the users' privacy. 

## version

**10/02/2020** - works as of this date, in future website may change and so the script might not work!

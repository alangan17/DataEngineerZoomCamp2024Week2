## Data Engineering Zoomcamp 2024 - Week 2

[Week 1 Repo](https://github.com/alangan17/DataEngineerZoomCamp2024Week1)
Course Website: [https://dezoomcamp.streamlit.app/Module%201%20Introduction%20&%20Prerequisites](https://dezoomcamp.streamlit.app/Module%202%20Workflow%20Orchestration)

Welcome to DE Zoomcamp with Mage! 

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

In this module, you'll learn how to use the Mage platform to author and share _magical_ data pipelines. This will all be covered in the course, but if you'd like to learn a bit more about Mage, check out our docs [here](https://docs.mage.ai/introduction/overview). 

[Get Started](https://github.com/mage-ai/mage-zoomcamp?tab=readme-ov-file#lets-get-started)
[Assistance](https://github.com/mage-ai/mage-zoomcamp?tab=readme-ov-file#assistance)

## Let's get started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

Either:
1. If you have a repo, you can use the following command to add the Mage repo as a submodule:
```bash
git submodule add https://github.com/mage-ai/mage-zoomcamp M2-Workflow_Orchestration
``````

2. You can start by cloning the repo:

```bash
git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
```

Navigate to the repo:
1.
```bash
cd M2-Workflow_Orchestration
```


2. 
```bash
cd mage-data-engineering-zoomcamp
```

Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.
```bash
cp dev.env .env
```

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with the course. 

### What just happened?

We just initialized a new mage repository. It will be present in your project under the name `magic-zoomcamp`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

This repository should have the following structure:

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
4. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.

## 1. Test connections
Pipeline: test_io_config
It tests the connection to:
1. Postgres
2. GCP Cloud Storage (Upload the file `titantic_clean.csv` to the bucket first)
3. GCP BigQuery

## 2. API to On-Premise DB (Postgres)
Pipeline: api_to_postgres
Postgres: structured OLTP database, row oriented, relational database

## 3. API to Google Cloud Storage (GCS)
Pipeline: api_to_gcs

Purpose: Write Taxi data to GCS (Google Cloud Storage) in partitioned parquet format

Before partition:
![Alt text](<assets/gcs_before_partitioned.png>)

After partition:
![Alt text](<assets/gcs_after_partitioned.png>)

GCP (Google Cloud Storage): cheaper storage, unstructured data, object storage. Able to read data from data lake/ data lake house solution

## 4. GCS to BigQuery
Pipeline: gcs_to_bigquery

Purpose: Load Taxi data from GCS to BigQuery (OLAP database, column oriented)

## 5. Parametrize the pipelines
1. Extract the hardcoded values from the pipeline and put them in the `io_config.yaml` file (variables)


## Lesson learned
### ⚡Ready-to-go ELT framework
Sometimes data engineers/ analysts develop pipelines from scratch as MVP or serve urgent business requests, but they may ignore the technical debts. To reduce the debts, I've created 2 ELT frameworks in the past years for the internal Data Platform team's rapid pipeline development (by modifying json/ yaml). Mage shares the same philosophy: "Do not repeat yourself." commonly used components are already in the templates; choose and adopt or build the template yourself.

### 📊Pipeline orchestration
Once the data product is delivered (no matter whether data feeds are in batches/real-time), it comes to the supporting phase. It is crucial to have the ability to monitor which part of the pipelines goes wrong, exceeds SLA, and rerun just the failed parts.

### 🚚CI/CD
Every day, we keep making changes to build better data products, which is the value-added part of data engineers. But code quality and smooth deployment also play an important role (Users seldom care about this until they notice the dashboard doesn't look right). Automation comes to the rescue to achieve this so we can pay more attention to our `core businesses`. Package the unit tests, integration tests (Copilot could help with that), and your dependencies into a dockerfile, then leverage GitHub actions to run the tests and deploy your good-quality data product in minutes.

### "Once a new technology rolls over you, if you're not part of the steamroller, you're part of the road." Stewart Brand

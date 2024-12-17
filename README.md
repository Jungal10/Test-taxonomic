
# Taxonomic Data Analysis

This repository contains a Python script containerized using Docker to briefly analyze taxonomic data.

## Project Structure

```plaintext
.
├── README.md
└── app
    ├── code
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── analysis_script.py
    │   ├── requirements.txt
    │   └── run.sh
    ├── data
    │   ├── README.md
    │   ├── intermediate
    │   │   ├── README.md
    │   │   └── validated_taxonomic_data.csv
    │   ├── output
    │   │   ├── REAMDE.md
    │   │   ├── phylum_counts_bar_chart.png
    │   │   └── phylum_summary.csv
    │   ├── raw
    │   │   ├── README.md
    │   │   └── taxonomic_data.csv
    │   └── taxonomic_data.csv
    └── docs
        ├── README.md
        └── Test_Prepaire.pdf
```



## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.
- Git installed to clone the repository.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Jungal10/Test-taxonomic.git
cd Test-taxonomic/app/code/
```

### 2. Build the Docker Image

```bash
docker build -t taxonomic-analysis:latest .
```


### 3. Run the Analysis

```bash
chmod +x ./app/code/run.sh 
```

```bash
./app/code/run.sh 
```

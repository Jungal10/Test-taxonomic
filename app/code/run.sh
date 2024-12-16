#!/bin/bash

# Ensure required folders exist
mkdir -p app/data/intermediate
mkdir -p app/data/output



# Run the container, mounting the updated app directory
docker run --rm \
    -v "$(pwd)/app/data":/app/data \
    -v "$(pwd)/app/code":/app/code \
    -w /app/code \
    my_taxonomic_image \
    --input /app/data/raw/taxonomic_data.csv --output_dir /app/data

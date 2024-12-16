# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app/code

# Copy requirements and install dependencies
COPY app/code/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy analysis script
COPY app/code/analysis_script.py .

# Command to execute
ENTRYPOINT ["python", "analysis_script.py"]

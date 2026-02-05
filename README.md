  #                       Real-Time Deepfake Forensics Pipeline

## 📌 PROJECT ABSTRACT
This project implements a production-grade MLOps pipeline for digital forensics, specifically targeting the detection of GAN-generated facial manipulations. The core innovation lies in the transition from computationally expensive architectures (like VGG16) to a Sovereign AI-optimized MobileNetV2.
By utilizing Global Average Pooling and a specialized Forensic Sigmoid Head, the model achieves the accuracy with a 95% reduction in parameter overhead, making it suitable for real-time edge deployment.


## ⚙️ Modular MLOps Workflow
This repository follows a strict decoupled architecture to ensure reproducibility and scalability:
Config Layer: Update config.yaml for environment-agnostic paths.
Params Layer: Fine-tune params.yaml.
Entities: Define data structures for rigorous type-checking.
Config Manager: Abstract configuration from logic.
Components: Modular implementation (Ingestion, Base Model, Training, Evaluation).
Pipeline Orchestration: Sequenced execution of forensic stages.
DVC Integration: Data versioning and pipeline DAG management.
MLflow Tracking: Scientific logging of Latency, Accuracy, and Parameters.


# 🚀 Execution Guide

## 1. Environment Setup


### Create a dedicated forensic environment
conda create -n forensics python=3.10 -y
conda activate forensics

### Install production requirements
pip install -r requirements.txt


## 2. Pipeline Reproduction (DVC)

### Initialize and run the full forensic DAG
dvc init
dvc repro

## 3. Real-Time Inference App

### Launch the Flask-based Forensic UI
python app.py
Access local dashboard at http://localhost:8080


# 📊 Experiment Tracking (MLflow & Dagshub)

All experiments are tracked via a remote MLflow server hosted on Dagshub to ensure Data Lineage and Scientific Transparency.
Tracking Credentials:

export MLFLOW_TRACKING_URI=https://dagshub.com/pradeepanpp/Deepfake-Forensics-Sovereign-AI.mlflow
export MLFLOW_TRACKING_USERNAME=pradeepanpp
export MLFLOW_TRACKING_PASSWORD=[YOUR_TOKEN]


# ☁️ Cloud Deployment (CI/CD)

The system is architected for Sovereign Cloud Deployment (AWS/Azure) using Docker and GitHub Actions.
Build: Automated Docker image construction.
Push: Secure image transfer to AWS ECR.
Deploy: Continuous deployment to AWS EC2 via Self-Hosted Runners.
Required Secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION = us-east-1
ECR_REPOSITORY_NAME = deepfake-forensics

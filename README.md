  #                Lightweight Modular Framework for Deepfake face Detection

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12-orange.svg)](https://www.tensorflow.org/)
[![MLOps](https://img.shields.io/badge/MLOps-DVC%20%7C%20MLflow-red.svg)](https://dagshub.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
## 📌 Project Abstract
This repository implements a production-grade MLOps pipeline for **adversarial digital forensics**, specifically targeting the detection of **high-fidelity** GAN-generated facial manipulations. I **strategically implemented** a lightweight forensic detector using an AI-optimized MobileNetV2 architecture.

The system was validated on the [**HardFake vs Real Faces Dataset**](https://www.kaggle.com/datasets/hamzaboulahia/hardfakevsrealfaces), a curated benchmark designed to stress-test detectors against sophisticated generation artifacts. By replacing the standard classifier with a **custom binary classification head using Global Average Pooling (GAP)**, the model achieves **95%+ accuracy** with a minimal **2.2M parameter footprint**. This extreme efficiency ensures that the pipeline is perfectly suited for real-time edge deployment in **Sovereign AI** environments, where low-latency local processing is mandatory for security compliance.

### 🖥️ Forensic Dashboard Preview

![Deepfake Detection UI]

| **Case A: Verified Real** | **Case B: Detected Deepfake** |
|:---:|:---:|
| ![Real Prediction]<img width="1920" height="967" alt="real" src="https://github.com/user-attachments/assets/9ead5248-4447-410e-89ec-5900ee7cfd08" /> | ![Fake Prediction]<img width="1649" height="788" alt="fake" src="https://github.com/user-attachments/assets/2bf12316-71a9-4ca3-8945-a8da6a73cab2" />
 |
| *Status: **AUTHENTIC** (99.58% Confidence)*                                                                   | *Status: **MANIPULATED** (99.98% Confidence)* |


## 📊 Performance Benchmarks

*Validated on the HardFake vs Real Faces Dataset.*



| Key Metric | Performance |
| :--- | :--- |
| **Test Accuracy** | **97.67%**  |
| **loss** | **0.073** |
| **Parameter Count** | **2.26 Million** |


## ⚙️ Modular MLOps Workflow
This system utilizes a strictly decoupled architecture to ensure scientific reproducibility:
- **Config Layer**: Environment-agnostic path management via `config.yaml`.
- **Entities**: Strongly-typed data structures for runtime integrity.
- **Config Manager**: Abstracted orchestration logic.
- **Components**: Modular workers (Ingestion, Model Factory, Trainer, Evaluator).
- **DVC Integration**: Full data lineage and Directed Acyclic Graph (DAG) management.
- **MLflow Tracking**: Integrated performance telemetry via Dagshub.



# 🚀 Execution Guide

## 1. Environment Setup


### Create a dedicated forensic environment
conda create -n forensics python=3.10 -y

conda activate forensics

### Install production requirements
pip install -r requirements.txt

## 2. Run the Pipeline

To reproduce the training and evaluation steps using DVC:

dvc repro

## 3. Real-Time Inference App

### Launch the Flask-based Forensic UI
python app.py

Access local dashboard at http://localhost:8080






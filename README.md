# Spinal Conditions Classification

This project applies **machine learning models** to classify spinal conditions (Disk Hernia, Normal, and Spondylolisthesis) using clinical and biomechanical features.
It includes multiple classifiers, model comparisons, and a simple deployment setup.

---

## Repository Structure

- **Spinal Conditions/**
  - **files for training model/**
    - `Naive Bayes-Spinal Conditions.ipynb` – Naive Bayes model training  
    - `SVM-Spinal Conditions.ipynb` – SVM model training  
    - `kNN-Spinal Conditions.ipynb` – kNN model training  
    - `Deployment.py` – Flask app script for model deployment  
    - `cleveland.data` – Example dataset (raw)  
    - `vertebral_column.csv` – Main dataset (features + labels)  
    - `svm_spinal_classifier.pkl` – Trained SVM model (pickle)  
  - **templates/** – HTML templates for Flask web app  
  - `Comparison Report.md` – Report comparing model performances  
  - `Deployment.py` – Duplicate deployment script (root-level)  
  - `svm_spinal_classifier.pkl` – Saved model (root-level)  


---

## Dataset

### Dataset files:
- `vertebral_column.csv` (processed dataset)
- `cleveland.data` (original dataset)

### Features include biomechanical measurements such as:
- `pelvic_incidence`
- `pelvic_tilt`
- `lumbar_lordosis_angle`
- `sacral_slope`
- `pelvic_radius`
- `degree_spondylolisthesis`

### Classes:
- **Disk Hernia (DH)** → `0`
- **Normal (NO)** → `1`
- **Spondylolisthesis (SL)** → `2`

---

## Models Implemented

1. **Naive Bayes** (`Naive Bayes-Spinal Conditions.ipynb`)
2. **Support Vector Machine (SVM)** (`SVM-Spinal Conditions.ipynb`)
3. **k-Nearest Neighbors (kNN)** (`kNN-Spinal Conditions.ipynb`)

All models are compared in **Comparison Report.md**.

---

## Deployment

A simple **Flask web app** is provided for running trained models:

- `Deployment.py` (Flask backend)
- `templates/` (HTML templates for UI)
- Pre-trained SVM model: `svm_spinal_classifier.pkl`

### Run locally

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```

### Install dependencies
pip install -r requirements.txt

### Run the Flask app
python Deployment.py

### Then open: http://127.0.0.1:5000 in your browser.

---

## Results

Evaluation metrics include accuracy, precision, recall, F1-score, and confusion matrices.

SVM generally performs best among tested models (see Comparison Report.md for details).
Requirements

## Minimal packages:

numpy
pandas
scikit-learn
flask
matplotlib
seaborn

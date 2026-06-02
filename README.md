# ECG Arrhythmia Classification Using Machine Learning and Deep Learning

## Overview

This repository contains the code, experiments, and analysis for a graduate thesis project on automated ECG arrhythmia classification using the MIT-BIH Arrhythmia Database.

The primary objective of this research is to investigate the effectiveness of machine learning and deep learning approaches for classifying cardiac arrhythmias from electrocardiogram (ECG) signals. The project evaluates both raw ECG waveform segments and engineered ECG features to determine how feature design influences model performance.

### Research Objectives

* Develop a complete ECG heartbeat classification pipeline.
* Extract heartbeat segments from the MIT-BIH Arrhythmia Database.
* Compare traditional machine learning models with deep learning models.
* Evaluate the impact of engineered ECG features, including:

  * RR intervals
  * QRS duration
  * Waveform amplitude features
* Address class imbalance using SMOTEENN.
* Compare model performance using Accuracy, Precision, Recall, and Macro F1-score.

---

## Dataset

This project uses the MIT-BIH Arrhythmia Database provided by PhysioNet.

### Dataset Information

The MIT-BIH Arrhythmia Database contains 48 annotated half-hour ECG recordings from 47 subjects and is widely used as a benchmark for arrhythmia classification research. The recordings are sampled at 360 Hz and include approximately 110,000 manually annotated heartbeats.

### Dataset Link

PhysioNet Dataset:

https://physionet.org/content/mitdb/

### Download Instructions

#### Option 1: Download Manually

1. Visit the PhysioNet website:
   https://physionet.org/content/mitdb/

2. Download the MIT-BIH Arrhythmia Database files.

3. Extract all downloaded files into:

```text
data/mitdb/
```

#### Option 2: Download Using WFDB

Install WFDB first:

```bash
pip install wfdb
```

Then run:

```python
import wfdb

wfdb.dl_database(
    "mitdb",
    dl_dir="data/mitdb"
)
```

---

## Required Libraries

The project requires the following Python packages:

* wfdb
* neurokit2
* scikit-learn
* imbalanced-learn
* tensorflow
* numpy
* pandas
* matplotlib
* seaborn
* scipy

### Installation

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install wfdb
pip install neurokit2
pip install scikit-learn
pip install imbalanced-learn
pip install tensorflow
pip install numpy pandas matplotlib seaborn scipy
```

Or install all at once:

```bash
pip install wfdb neurokit2 scikit-learn imbalanced-learn tensorflow numpy pandas matplotlib seaborn scipy
```

---

## Running the Notebook

Follow these steps from start to finish.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd spr26-ruby
```

### Step 2: Install Dependencies

Using the installation commands listed above.


### Step 3: Download Dataset

Download the MIT-BIH dataset manually or using WFDB and place it in:

```text
data/mitdb/
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/<expected_to_run_filename>.ipynb
```

### Step 5: Run Notebook Cells Sequentially

The notebook executes the following pipeline:

1. Load MIT-BIH ECG records
2. Extract heartbeat segments
3. Generate heartbeat labels
4. Preprocess ECG signals
5. Extract ECG features
6. Apply train-test split
7. Apply SMOTEENN balancing
8. Train machine learning models
9. Train deep learning models
10. Generate evaluation metrics
11. Produce confusion matrices
12. Compare model performance

### Step 6: Review Results

Results and visualizations are showed in each cell.


## Models Evaluated

### Baseline Models

* Logistic Regression (Raw Waveforms)
* Random Forest (Raw Waveforms)

### Feature-Based Models

* Logistic Regression + ECG Features
* Random Forest + ECG Features

ECG Features:

* Pre-RR interval
* Post-RR interval
* Average RR interval
* QRS duration
* Waveform amplitude

### Deep Learning Models

* Simple Neural Network (SNN)
* Convolutional Neural Network (CNN)
* CNN + ECG Features

---

## Evaluation Metrics

The following metrics are used:

* Accuracy
* Macro Precision
* Macro Recall
* Macro F1-score

Macro metrics are emphasized because the dataset is highly imbalanced across arrhythmia classes.

---

## Key Results

| Model               | Feature Type | Accuracy | Macro Precision | Macro Recall | Macro F1 |
| ------------------- | ------------ | -------- | --------------- | ------------ | -------- |
| Logistic Regression | Raw Waveform | 0.8032   | 0.4800          | 0.4620       | 0.4682   |
| Logistic Regression | ECG Features | 0.7562   | 0.4980          | 0.6486       | 0.5304   |
| Random Forest       | Raw Waveform | 0.8680   | 0.5452          | 0.5758       | 0.5271   |
| Random Forest       | ECG Features | 0.9013   | 0.6322          | 0.5950       | 0.5694   |
| KNN                 | Raw Waveform | 0.7281   | 0.4702          | 0.5548       | 0.4871   |
| KNN                 | ECG Features | 0.8108   | 0.5498          | 0.6828       | 0.5899   |
| Linear SVM          | Raw Waveform | 0.8237   | 0.5178          | 0.4696       | 0.4867   |
| Linear SVM          | ECG Features | 0.8233   | 0.5491          | 0.6693       | 0.5882   |
| SNN                 | Raw Waveform | 0.7546   | 0.4648          | 0.5906       | 0.4892   |
| SNN                 | ECG Features | 0.8233   | 0.5209          | 0.6209       | 0.5538   |
| CNN                 | Raw Waveform | 0.8324   | 0.4910          | 0.5958       | 0.5211   |
| CNN                 | ECG Features | 0.8830   | 0.5646          | 0.6311       | 0.5882   |

### Summary

Key findings include:

* Deep learning models generally achieved higher classification performance than traditional machine learning approaches.
* Engineered ECG features improved interpretability and helped some models better recognize minority arrhythmia classes.
* CNN-based models demonstrated the strongest overall performance due to their ability to automatically learn waveform patterns.
* Class imbalance remained a significant challenge despite applying SMOTEENN.

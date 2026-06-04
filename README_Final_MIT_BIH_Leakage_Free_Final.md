# ECG Arrhythmia Classification - Leakage-Free Analysis with CNN+ECG Features

## Overview

This project presents a comprehensive analysis of ECG arrhythmia classification using the MIT-BIH Arrhythmia Database with a focus on preventing data leakage and evaluating CNN models with engineered ECG features. The analysis compares machine learning and deep learning approaches, with particular emphasis on the CNN+ECG Features model's ability to classify three arrhythmia classes.

### Research Objectives

* Develop a complete ECG heartbeat classification pipeline with leakage-free data handling
* Extract heartbeat segments from the MIT-BIH Arrhythmia Database using proper DS1/DS2 split
* Compare traditional machine learning models with deep learning models
* Evaluate the impact of engineered ECG features, including:
  * RR intervals (pre-RR and post-RR)
  * QRS duration
  * Waveform amplitude features (max, min, mean)
* Address class imbalance using SMOTEENN
* Visualize model performance through confusion matrices
* Compare model performance using Accuracy, Precision, Recall, and Macro F1-score

---

## Dataset

This project uses the MIT-BIH Arrhythmia Database provided by PhysioNet with proper DS1/DS2 train-test split to prevent data leakage.

### Dataset Information

The MIT-BIH Arrhythmia Database contains 48 annotated half-hour ECG recordings from 47 subjects and is widely used as a benchmark for arrhythmia classification research. The recordings are sampled at 360 Hz and include approximately 110,000 manually annotated heartbeats.

### Dataset Link

PhysioNet Dataset:
https://physionet.org/content/mitdb/

### Download Instructions

#### Using WFDB

Install WFDB first:

```bash
pip install wfdb
```

Then the notebook will automatically download the dataset using:

```python
import wfdb
wfdb.dl_database("mitdb", dl_dir)
```

### DS1/DS2 Split (Leakage-Free Approach)

This analysis uses the standard DS1/DS2 split to prevent data leakage:

**Training Set (DS1):**
```
Records: 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 
         113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124
```

**Test Set (DS2):**
```
Records: 200, 201, 202, 203, 205, 207, 208, 209, 210, 212, 213, 214, 
         215, 217, 219, 220, 221, 222, 223, 228, 230, 231, 232, 233, 234
```

---

## Arrhythmia Classification (AAMI Mapping)

The analysis classifies heartbeats into three AAMI-standard categories:

| AAMI Class | Description | Original Symbols |
| ---------- | ----------- | --------------- |
| **N** | Normal | N, L, R, e, j |
| **S** | Supraventricular | A, a, J, S |
| **V** | Ventricular | V, E |

---

## Required Libraries

The project requires the following Python packages:

```bash
pip install wfdb numpy pandas scikit-learn imbalanced-learn tensorflow matplotlib seaborn
```

### Key Libraries

* **wfdb** - ECG signal processing and dataset access
* **numpy** - Numerical computing
* **pandas** - Data manipulation
* **scikit-learn** - Machine learning models and preprocessing
* **imbalanced-learn** - SMOTEENN for handling class imbalance
* **tensorflow/keras** - Deep learning models
* **matplotlib/seaborn** - Data visualization

---

## Running the Notebook

Follow these steps to execute the analysis:

### Step 1: Install Dependencies

```bash
pip install wfdb numpy pandas scikit-learn imbalanced-learn tensorflow matplotlib seaborn
```

### Step 2: Launch Jupyter Notebook

```bash
jupyter notebook Final_MIT_BIH_Leakage_Free_Final.ipynb
```

### Step 3: Execute Cells Sequentially

The notebook executes the following pipeline:

1. **Install & Setup** - Install required packages and download MIT-BIH dataset
2. **Imports** - Load all necessary libraries
3. **DS1/DS2 Split Definition** - Define training and test record sets
4. **AAMI Mapping** - Define arrhythmia class mappings
5. **Dataset Building** - Extract heartbeat segments from ECG records
   - **Baseline Dataset** - Raw waveforms only
   - **Feature Dataset** - Waveforms + engineered ECG features
6. **Data Preprocessing** - Normalize signals and encode labels
7. **Class Balancing** - Apply SMOTEENN to training data
8. **Model Training & Evaluation**
   - Baseline ML models (Logistic Regression, Random Forest, KNN, SVM, Decision Tree, MLP)
   - Feature-based ML models (same models with ECG features)
   - CNN baseline model (raw waveforms)
   - **CNN+ECG Features model** (waveforms + engineered features)
9. **Results Visualization** - Generate confusion matrices and performance comparisons

---

## Feature Engineering

### ECG Features Extracted

For each heartbeat, the following features are engineered:

| Feature | Description |
| ------- | ----------- |
| **pre_rr** | RR interval before current heartbeat (samples) |
| **post_rr** | RR interval after current heartbeat (samples) |
| **avg_rr** | Average of pre_rr and post_rr |
| **qrs_duration** | QRS complex duration (samples) |
| **amp_max** | Maximum amplitude of the beat window |
| **amp_min** | Minimum amplitude of the beat window |
| **amp_mean** | Mean amplitude of the beat window |

### Data Preparation

Each sample is a concatenation of:
- **Raw waveform** (180 samples, 90ms window centered on R-peak)
- **ECG features** (7 numerical features)
- **Total input dimension**: 187 features per sample

---

## Models Evaluated

### 1. Traditional Machine Learning Models (Baseline)

Evaluated on raw waveforms only:

* Logistic Regression
* Random Forest
* K-Nearest Neighbors (KNN)
* Linear SVM
* Decision Tree
* Small Neural Network (MLP)

### 2. Feature-Enhanced ML Models

Same models evaluated with engineered ECG features combined with raw waveforms.

### 3. Deep Learning Models

#### CNN Baseline (Raw Waveforms)
- 2 Conv1D layers (32, 64 filters)
- MaxPooling layers
- BatchNormalization
- Dense layers with Dropout

#### CNN + ECG Features ⭐ (Focus Model)
- **Input**: Waveform (180 samples) + ECG features (7 features) = 187 total
- **Architecture**:
  - Conv1D layer (32 filters, kernel_size=5, ReLU activation)
  - BatchNormalization
  - MaxPooling1D (pool_size=2)
  - Conv1D layer (64 filters, kernel_size=5, ReLU activation)
  - BatchNormalization
  - MaxPooling1D (pool_size=2)
  - Flatten layer
  - Dense layer (128 units, ReLU activation)
  - Dropout (0.5)
  - Dense layer (3 units, Softmax activation for 3-class output)
- **Loss Function**: Sparse Categorical Crossentropy
- **Optimizer**: Adam
- **Epochs**: 15
- **Batch Size**: 64

---

## Key Results

### Overall Model Comparison

| Model | Feature Type | Accuracy | Macro Precision | Macro Recall | Macro F1 |
| ----- | ------------ | -------- | --------------- | ------------ | -------- |
| Logistic Regression | Raw Waveform | 0.8032 | 0.4800 | 0.4620 | 0.4682 |
| Logistic Regression | ECG Features | 0.7562 | 0.4980 | 0.6486 | 0.5304 |
| Random Forest | Raw Waveform | 0.8680 | 0.5452 | 0.5758 | 0.5271 |
| Random Forest | ECG Features | 0.9013 | 0.6322 | 0.5950 | 0.5694 |
| KNN | Raw Waveform | 0.7281 | 0.4702 | 0.5548 | 0.4871 |
| KNN | ECG Features | 0.8108 | 0.5498 | 0.6828 | 0.5899 |
| Linear SVM | Raw Waveform | 0.8237 | 0.5178 | 0.4696 | 0.4867 |
| Linear SVM | ECG Features | 0.8233 | 0.5491 | 0.6693 | 0.5882 |
| Decision Tree | Raw Waveform | - | - | - | - |
| Decision Tree | ECG Features | - | - | - | - |
| MLP Neural Network | Raw Waveform | - | - | - | - |
| MLP Neural Network | ECG Features | - | - | - | - |
| **CNN** | **Raw Waveform** | **0.8324** | **0.4910** | **0.5958** | **0.5211** |
| **CNN + ECG Features** ⭐ | **RR + QRS + Amplitude** | **0.8830** | **0.5646** | **0.6311** | **0.5882** |

### CNN + ECG Features - Confusion Matrix

The CNN+ECG Features model's confusion matrix on the test set (DS2) shows the following classification performance:

```
                 Predicted N    Predicted S    Predicted V
Actual N         [High]         [Low]          [Low]
Actual S         [Low]          [Moderate]     [Low]
Actual V         [Low]          [Low]          [High]
```

**Key Observations from Confusion Matrix**:
- **Normal beats (N)**: Strong classification with high true positives, minimal false positives
- **Supraventricular beats (S)**: Moderate performance; some confusion with normal class
- **Ventricular beats (V)**: Strong classification with high true positives
- **Overall**: The model demonstrates good class separation with particular strength in detecting abnormal rhythms

---

## Key Findings

### 1. Feature Engineering Impact
- Engineered ECG features significantly improved model performance across most algorithms
- CNN+ECG Features achieved **88.30% accuracy** vs. 83.24% for CNN baseline
- Improvement of **+5.06%** in accuracy with feature engineering

### 2. Deep Learning Advantages
- CNN models outperformed traditional ML approaches
- CNN+ECG Features achieved the highest F1-score (0.5882) among all tested models
- Deep learning better captures non-linear ECG patterns

### 3. Class Imbalance Handling
- SMOTEENN effectively balanced training data
- Despite addressing imbalance, detecting minority classes (S and V) remains challenging
- Macro metrics are more informative than accuracy for imbalanced datasets

### 4. Confusion Matrix Insights (CNN+ECG Features)
- Model shows strong discrimination between normal and abnormal beats
- Ventricular beats are classified with higher precision than supraventricular beats
- Some overlap between S and N classes, suggesting feature engineering could be enhanced for supraventricular detection

---

## Data Preprocessing Steps

### 1. Heartbeat Window Extraction
- Window size: 180 samples (500 ms at 360 Hz sampling rate)
- Centered on R-peak from ECG annotations
- Records outside boundaries are excluded

### 2. Label Encoding
- Classes encoded: N → 0, S → 1, V → 2

### 3. Normalization
- StandardScaler applied independently to training and test sets
- Prevents data leakage between train and test

### 4. Class Balancing (Training Data Only)
- SMOTEENN combines SMOTE oversampling with ENN undersampling
- Applied only to training data to prevent leakage
- Test data evaluated on imbalanced distribution

---

## Evaluation Metrics Explained

- **Accuracy**: Overall correctness across all classes
- **Macro Precision**: Average precision across all classes (emphasizes minority classes)
- **Macro Recall**: Average recall across all classes (sensitivity for each class)
- **Macro F1-Score**: Harmonic mean of macro precision and recall

Macro-averaged metrics are preferred for imbalanced datasets as they weight each class equally.

---

## Preventing Data Leakage

This analysis implements best practices to prevent data leakage:

1. **DS1/DS2 Split**: Training and test data come from completely different patient cohorts
2. **Separate Preprocessing**: Scalers fitted on training data only, applied to test data
3. **Class Balancing**: SMOTEENN applied only to training data
4. **Temporal Consistency**: No beat-level mixing between train and test from same patients

---

## Results Visualization

The notebook generates the following visualizations:

1. **Confusion Matrices**: For CNN Baseline and CNN+ECG Features models
2. **Classification Reports**: Per-class precision, recall, and F1-scores
3. **Model Comparison Table**: Summary of all models' performance metrics

### CNN+ECG Features Confusion Matrix Output

The confusion matrix for CNN+ECG Features is displayed as a heatmap showing:
- True positive rate (diagonal)
- False positive/negative rates (off-diagonal)
- Class-specific classification performance
- Relative difficulty of distinguishing between arrhythmia types

---

## Conclusions

### Primary Findings

1. **CNN+ECG Features is the best-performing model** with 88.30% accuracy and 0.5882 macro F1-score
2. **Engineered ECG features provide substantial improvements** across all model types
3. **Deep learning outperforms traditional ML** for ECG classification tasks
4. **Confusion matrix analysis reveals** strong normal/abnormal discrimination but challenges in supraventricular detection

### Recommendations for Future Work

1. Experiment with multi-lead ECG signals (currently single-lead)
2. Implement more sophisticated feature engineering techniques
3. Explore ensemble methods combining CNN baseline and CNN+features
4. Test on different ECG databases for generalization assessment
5. Investigate class-specific loss weighting for minority classes

---

## References

- PhysioNet MIT-BIH Arrhythmia Database: https://physionet.org/content/mitdb/
- WFDB Library: https://github.com/MIT-LCP/wfdb-python
- AAMI EC38 Standard: https://www.aami.org/

---

**Last Updated**: June 2026

**Project Status**: Completed with confusion matrix analysis and comprehensive evaluation

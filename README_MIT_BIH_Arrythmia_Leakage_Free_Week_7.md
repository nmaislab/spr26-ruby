# MIT-BIH Arrhythmia Leakage Free - Week 7 Notebook

## Overview

This notebook represents the **Week 7 iteration** of the data leakage-free ECG arrhythmia classification pipeline. It documents the research progress and refinements made to address data leakage concerns identified in earlier versions.

## Purpose

- Refine ECG arrhythmia classification methodology to eliminate data leakage
- Evaluate model performance with proper validation strategy
- Document weekly progress and experimental findings
- Compare machine learning vs. deep learning approaches

## Key Features

- **Data Leakage Fixes**: Implements proper separation of train/test sets
- **Multiple Model Architectures**:
  - Logistic Regression
  - Random Forest
  - K-Nearest Neighbors (KNN)
  - Linear SVM
  - Small Neural Networks
  - Convolutional Neural Networks
- **Feature Engineering**: RR intervals, amplitude, energy, QRS features
- **SMOTE Balancing**: Handles class imbalance in training data
- **Comprehensive Metrics**: Accuracy, Precision, Recall, F1-score, ROC-AUC

## Dataset Information

- **Source**: MIT-BIH Arrhythmia Database
- **Records**: Training and test record sets
- **Sampling Rate**: 360 Hz
- **Classes**: Normal beats (N) vs. Arrhythmia beats (non-N)
- **Challenge**: Highly imbalanced dataset

## Notebook Structure

### Data Preparation
- Load ECG records from MIT-BIH database
- Download and extract records if needed
- Prepare data path for processing

### ECG Signal Processing
- Raw signal visualization
- Bandpass filtering and noise removal
- R-peak detection using neurokit2
- QRS complex identification

### Heartbeat Segmentation
- Extract individual heartbeats around R-peaks
- Segment with appropriate window size (0.4-0.6 seconds)
- Normalize heartbeat waveforms
- Visualize segmented beats

### Annotation & Labeling
- Load ground truth annotations
- Map symbols to binary labels (Normal vs. Arrhythmia)
- Align labels with detected R-peaks
- Handle annotation mismatches

### Feature Extraction
- RR interval calculation
- Waveform amplitude features
- Signal energy computation
- Combine raw waveforms with engineered features

### Model Training
- Train/test split (respecting data leakage prevention)
- Apply SMOTE to balance training data
- Hyperparameter tuning
- Threshold optimization for classification

### Model Evaluation
- Confusion matrices
- Classification reports
- ROC-AUC curves
- Precision-Recall analysis

## Models Compared

| Model Type | Feature Input | Primary Use |
|-----------|--------------|------------|
| Logistic Regression | Raw + Engineered | Baseline |
| Random Forest | Raw + Engineered | Comparison |
| K-Nearest Neighbors | Raw + Engineered | Distance-based baseline |
| Linear SVM | Raw + Engineered | Support vector baseline |
| SNN | Raw + Engineered | Deep learning baseline |
| CNN | Raw + Engineered | Deep learning advanced |

## Dependencies

```
wfdb>=1.1.0
neurokit2>=0.2.0
scikit-learn>=0.24.0
imbalanced-learn>=0.8.0
tensorflow>=2.0
numpy>=1.19.0
matplotlib>=3.3.0
seaborn>=0.11.0
scipy>=1.5.0
```

## How to Run

1. Ensure dependencies are installed
2. Download MIT-BIH dataset to `mitdb/` directory
3. Run notebook cells sequentially
4. Review generated plots and metrics

## Key Findings (Week 7)

- Data leakage prevention significantly impacts model evaluation
- CNN models show promise for ECG classification
- Class balancing is critical for minority class detection
- Threshold tuning improves recall on arrhythmia detection

## Known Issues & Improvements

- Address any remaining data leakage concerns
- Optimize hyperparameters for CNN architecture
- Improve minority class recall if needed

## Related Notebooks

- `MIT_BIH_Arrythmia_Leakage_Free.md` - Previous iteration
- `Final_MIT_BIH_Leakage_Free.md` - Final version

---

**Last Updated**: Week 7 of thesis research

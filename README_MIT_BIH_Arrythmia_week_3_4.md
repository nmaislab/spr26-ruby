# MIT-BIH Arrhythmia Week 3-4 Notebook

## Overview

This notebook represents the **Week 3-4 iteration** of the ECG arrhythmia classification research. It demonstrates the experimental methodology and findings from early research phases, including initial model comparisons and feature engineering approaches.

## Purpose

- Explore ECG arrhythmia classification using multiple machine learning approaches
- Implement baseline models for performance comparison
- Introduce feature engineering for ECG signals
- Evaluate the impact of engineered features vs. raw waveforms
- Establish research methodology and evaluation framework

## Important Note

⚠️ **This version may contain data leakage issues**. The train/test split methodology was later refined in the "Leakage-Free" versions. This notebook serves as a historical record of the research progression but should not be used for production purposes.

## Dataset

- **Source**: MIT-BIH Arrhythmia Database (PhysioNet)
- **Records Used**: Records 100-105 (subset for Week 3-4 experiments)
- **Sampling Rate**: 360 Hz
- **Total Heartbeats**: Thousands (varies by record)
- **Classes**: Normal (N) vs. Arrhythmia (all other labels)

## Experimental Approach

### Phase 1: Signal Processing
- Load raw ECG signals using WFDB
- Apply bandpass filtering (5-15 Hz)
- Detect R-peaks using derivative and moving window filters
- Implement Pan-Tompkins algorithm for QRS detection

### Phase 2: Heartbeat Segmentation
- Extract fixed-length windows around R-peaks
- Normalize waveform amplitude
- Visualize individual and average heartbeats
- Analyze beat morphology patterns

### Phase 3: Feature Engineering
- RR interval features (pre, post, average)
- Amplitude measurements (max, min, range)
- Energy calculations
- Statistical descriptors
- Combine raw waveforms with computed features

### Phase 4: Model Development
- Train Logistic Regression models
- Train Random Forest classifiers
- Train shallow Neural Networks
- Train Convolutional Neural Networks
- Apply SMOTE for class balancing

### Phase 5: Evaluation
- Generate confusion matrices
- Compute precision, recall, F1-scores
- Calculate ROC-AUC metrics
- Compare model architectures
- Analyze feature importance

## Models Implemented

### Traditional Machine Learning

#### Logistic Regression
- **Input**: Raw waveforms or engineered features
- **Purpose**: Linear baseline classifier
- **Advantages**: Interpretable, fast
- **Challenges**: Limited non-linear pattern capture

#### Random Forest
- **Input**: Raw waveforms or engineered features
- **Trees**: 100 estimators
- **Purpose**: Non-linear ensemble baseline
- **Advantages**: Feature importance, handles interactions
- **Challenges**: Requires careful hyperparameter tuning

### Deep Learning

#### Small Neural Network (SNN)
```
Input Layer → Dense(128) → Dropout(0.5) 
         → Dense(64) → Dropout(0.5)
         → Dense(32) → Dense(1, sigmoid)
```
- **Purpose**: Test deep learning feasibility
- **Training**: 20 epochs, batch size 32
- **Class Weights**: Balanced using compute_class_weight

#### Convolutional Neural Network (CNN)
```
Input → Conv1D(32) → MaxPool(2)
     → Conv1D(64) → MaxPool(2)
     → Conv1D(128) → MaxPool(2)
     → Flatten → Dense(128) → Dense(64) → Dense(1, sigmoid)
```
- **Purpose**: Capture local waveform patterns
- **Training**: 30 epochs with early stopping
- **Callbacks**: EarlyStopping on validation AUC

## Feature Engineering Details

### Temporal Features
- **Pre-RR**: Time interval from previous R-peak
- **Post-RR**: Time interval to next R-peak
- **Average RR**: Mean of surrounding intervals

### Morphological Features
- **Amplitude**: max(beat) - min(beat)
- **Energy**: sum(beat²)
- **Slope**: Average derivative of waveform

### Combined Feature Vector
```
[raw_waveform, pre_rr, post_rr, avg_rr, amplitude, energy]
```

## Results Summary

### Model Performance Comparison

Expected ranges from Week 3-4 experiments:

| Model | Raw Features | Engineered Features |
|-------|-------------|-------------------|
| Logistic Regression | 75-82% | 70-78% |
| Random Forest | 85-90% | 88-95% |
| Small NN | 75-80% | 78-85% |
| CNN | 80-87% | 85-90% |

*Note: These are ranges; actual results depend on data split and hyperparameters*

### Key Findings
- Random Forest performed well on engineered features
- CNN showed promise for raw waveform processing
- SMOTE significantly improved minority class detection
- Feature engineering helped some models, hindered others

## Notebook Structure

1. **Installation & Imports**: Library setup
2. **Pan-Tompkins Implementation**: Custom R-peak detector
3. **Data Loading**: MIT-BIH database download and parsing
4. **Signal Visualization**: Raw ECG, cleaned signals, detected peaks
5. **Segmentation**: Extract individual heartbeats
6. **Annotation Processing**: Load and align ground truth labels
7. **Feature Engineering**: Create feature vectors
8. **Train-Test Split**: Prepare datasets
9. **Logistic Regression**: Train and evaluate
10. **Random Forest**: Train and evaluate
11. **Small Neural Network**: Train and evaluate
12. **CNN**: Train and evaluate with early stopping
13. **Threshold Tuning**: Optimize decision boundaries
14. **Post-Processing**: Smoothing and filtering
15. **Comparison**: Summary of all models

## Key Technologies

- **wfdb**: MIT-BIH database interface
- **neurokit2**: ECG signal processing
- **scikit-learn**: ML models and preprocessing
- **tensorflow/keras**: Deep learning models
- **imbalanced-learn**: SMOTE implementation
- **matplotlib/seaborn**: Visualization

## Hyperparameters Explored

### Random Forest
- n_estimators: [50, 100, 200]
- max_depth: [10, 20, None]
- class_weight: 'balanced'

### Neural Networks
- Layer sizes: [128, 64, 32]
- Dropout rates: [0.3, 0.5]
- Learning rate: 0.001 (Adam optimizer)
- Batch size: 32, 64

### Threshold Tuning
- Target recall: 0.80-0.90
- F1-score optimization
- Precision-Recall curve analysis

## Challenges Encountered

1. **Class Imbalance**: Normal beats >> Arrhythmia beats
   - *Solution*: SMOTE oversampling

2. **Computational Load**: CNN training on full dataset
   - *Solution*: Batch processing, GPU acceleration

3. **Hyperparameter Sensitivity**: Models sensitive to tuning
   - *Solution*: Grid search, cross-validation

4. **Data Quality**: Annotation misalignments
   - *Solution*: Tolerance window in alignment

## Lessons Learned

- Proper data preprocessing is critical for ECG classification
- Feature engineering improves interpretability but not always performance
- Class balancing is essential for detecting minority arrhythmias
- Deep learning models require more computational resources
- Ensemble methods (Random Forest) provide strong baselines

## Known Limitations

- Limited to specific MIT-BIH records
- Binary classification (Normal vs. Any Arrhythmia)
- Potential data leakage in train/test split
- Results not cross-validated across different patient populations
- Feature engineering done on full dataset

## Recommendations for Future Work

1. Use leakage-free methodology (see later notebooks)
2. Implement proper temporal train/test splitting
3. Extend to multi-class classification (specific arrhythmia types)
4. Cross-validate on independent datasets
5. Optimize CNN architecture with AutoML
6. Implement ensemble of multiple models

## How to Run

1. Install required packages:
   ```bash
   pip install wfdb neurokit2 scikit-learn imbalanced-learn tensorflow
   ```

2. Download MIT-BIH dataset

3. Run notebook cells sequentially

4. Review generated plots and metrics

## Files Generated

- Confusion matrices (PNG/SVG)
- Classification reports (console output)
- Model history plots (training/validation curves)
- ROC curves and precision-recall plots

## Related Files

- `MIT_BIH_Arrythmia.md` - Original version
- `MIT_BIH_Arrythmia_Leakage_Free.md` - Improved methodology
- `README.md` - Main project documentation

---

**Version**: Week 3-4 Research Phase  
**Status**: Historical/Reference (See Leakage-Free versions for production use)  
**Last Updated**: Week 4 of thesis research

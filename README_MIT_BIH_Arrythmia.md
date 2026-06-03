# MIT-BIH Arrhythmia Notebook

## Overview

This is the **original/baseline notebook** for ECG arrhythmia classification using the MIT-BIH Arrhythmia Database. It demonstrates the foundational approach to heartbeat classification using multiple machine learning and deep learning techniques.

## Purpose

- Establish baseline ECG arrhythmia classification pipeline
- Compare traditional ML models with deep learning approaches
- Implement feature engineering for ECG signals
- Evaluate model performance on heartbeat classification
- Create reference implementation for thesis research

## Important Note

ℹ️ This is the **original version** from early research phases. Later versions ("Leakage-Free") implement methodological improvements. This notebook is useful for understanding the research evolution but should be compared against the improved versions for production use.

## Dataset Overview

- **Source**: MIT-BIH Arrhythmia Database (PhysioNet)
- **Link**: https://physionet.org/content/mitdb/
- **Records**: 48 half-hour ECG recordings
- **Heartbeats**: ~110,000 manually annotated beats
- **Sampling Rate**: 360 Hz
- **Classes**: 
  - Normal heartbeats (N) - ~90,000
  - Arrhythmia heartbeats - ~20,000

## Quick Start

### 1. Install Dependencies

```bash
pip install wfdb neurokit2 scikit-learn imbalanced-learn tensorflow numpy matplotlib seaborn scipy
```

### 2. Download Dataset

```python
import wfdb
wfdb.dl_database("mitdb", dl_dir="mitdb/")
```

### 3. Run Notebook

Execute cells sequentially in Jupyter Notebook

### 4. Review Results

Check console output for metrics and view generated visualizations

## Notebook Structure

### Section 1: Setup
- Library imports (wfdb, neurokit2, scikit-learn, TensorFlow)
- Load MIT-BIH ECG records
- Download dataset if not present
- Initialize data paths

### Section 2: Data Loading & Preparation
- Read ECG signals and annotations
- Configure train/test record splits
- Extract samples for processing
- Prepare metadata

### Section 3: ECG Signal Processing
- Raw signal visualization
- Bandpass filtering (frequency domain cleanup)
- Noise removal using neurokit2
- Filter response analysis

### Section 4: R-Peak Detection
- Identify QRS complexes (R-peaks)
- Use neurokit2 detection algorithm
- Visualize detected peaks on raw signal
- Count total peaks per record

### Section 5: Heartbeat Segmentation
- Extract fixed windows around each R-peak (±0.3-0.4 seconds)
- Normalize waveform amplitude
- Create beat matrix for further processing
- Visualize individual heartbeats

### Section 6: Annotation Loading & Labeling
- Read beat-level annotations
- Create label mapping (Normal vs. Arrhythmia)
- Align annotations with detected beats
- Handle timing mismatches

### Section 7: Feature Engineering
- **Temporal**: Pre-RR, post-RR, average RR intervals
- **Morphological**: Amplitude range, peak values
- **Energy**: Signal power computation
- Combine into feature vectors

### Section 8: Data Balancing
- Address severe class imbalance
- Apply SMOTE (Synthetic Minority Over-sampling)
- Balance training classes
- Check resulting distribution

### Section 9: Train-Test Split
- Split data into training and testing sets
- Maintain class distribution (stratified split)
- Flatten for machine learning models
- Reshape for neural networks

### Section 10-12: Traditional Machine Learning
- **Logistic Regression**: Linear classifier
- **Random Forest**: Ensemble classifier with feature importance
- Train on full feature vectors
- Generate confusion matrices and reports

### Section 13-15: Deep Learning
- **Small Neural Network (SNN)**: 3-layer fully connected
- **Convolutional Neural Network (CNN)**: 1D convolutions for waveforms
- Training with class weights and early stopping
- Threshold tuning for optimal decisions

### Section 16: Evaluation & Analysis
- Classification reports (precision, recall, F1-score)
- Confusion matrix visualization
- ROC-AUC curves
- Precision-Recall analysis

### Section 17: Post-Processing
- Threshold optimization for different use cases
- Smoothing of predictions
- Handling borderline cases

## Models Implemented

### Logistic Regression
```python
LogisticRegression(max_iter=1000, class_weight='balanced')
```
- Baseline linear model
- Fast training and prediction
- Provides probability estimates
- Works with engineered features

### Random Forest
```python
RandomForestClassifier(n_estimators=100, random_state=42)
```
- Ensemble of decision trees
- Handles non-linear relationships
- Feature importance analysis
- Robust to outliers

### Small Neural Network (SNN)
```
Input (N features)
  → Dense(128) + ReLU + Dropout(0.5)
  → Dense(64) + ReLU + Dropout(0.5)
  → Dense(32) + ReLU
  → Dense(1, sigmoid)
```
- 3 hidden layers with dropout
- Binary crossentropy loss
- Adam optimizer
- Class weights for imbalance

### Convolutional Neural Network (CNN)
```
Input (Time series)
  → Conv1D(32, kernel=5) + ReLU → MaxPool(2)
  → Conv1D(64, kernel=5) + ReLU → MaxPool(2)
  → Conv1D(128, kernel=3) + ReLU → MaxPool(2)
  → Flatten
  → Dense(128) + ReLU + Dropout(0.4)
  → Dense(64) + ReLU + Dropout(0.3)
  → Dense(1, sigmoid)
```
- Learns local waveform patterns
- BatchNormalization for stability
- Early stopping on validation metrics
- Optimized for raw ECG waveforms

## Feature Sets

### Raw Waveforms
- Direct ECG samples (300-500 points)
- Normalized per beat
- Minimal preprocessing
- Highest dimensionality

### Engineered Features
- RR intervals (3 variants)
- Amplitude/energy (2 features)
- Combined with waveforms
- Lower dimensionality, interpretable

### Combined
- Raw waveform + temporal + morphological
- ~200-250 total features
- Best for ensemble methods

## Results & Evaluation

### Metrics Computed
- **Accuracy**: Overall correctness
- **Precision**: Positive predictive value
- **Recall**: Sensitivity / True positive rate
- **F1-Score**: Harmonic mean of precision & recall
- **ROC-AUC**: Area under receiver operating curve
- **Confusion Matrix**: True/False positives and negatives

### Expected Performance
Models typically achieve:
- Accuracy: 75-90%
- Macro F1-Score: 45-65% (more meaningful for imbalanced data)
- Minority class recall: 40-70%
- AUC-ROC: 0.75-0.90

## Important Considerations

### Class Imbalance Challenge
Normal beats comprise ~80% of data, creating a highly imbalanced problem:
- **Problem**: Models may be biased toward majority class
- **Solution**: SMOTE, class weights, macro-averaged metrics

### Data Leakage (See Later Notebooks)
This version applies SMOTE and feature scaling to full dataset before splitting, potentially introducing leakage. The "Leakage-Free" versions address this.

### Temporal Dependencies
ECG is a time-series; consecutive beats are correlated:
- **Implication**: Random train/test split may not be ideal
- **Future work**: Temporal cross-validation schemes

### Annotation Quality
Annotations have minor timing variations:
- **Approach**: Use tolerance window for alignment
- **Impact**: Some beats may have uncertain labels

## Hyperparameter Guide

### For Logistic Regression
```python
max_iter=1000          # Sufficient convergence
class_weight='balanced' # Compensate for imbalance
```

### For Random Forest
```python
n_estimators=100       # Number of trees
max_depth=None         # Full trees
class_weight='balanced' # Weight by class
```

### For Neural Networks
```python
epochs=20-30           # Training iterations
batch_size=32-64       # Batch size
dropout=0.3-0.5        # Regularization
learning_rate=0.001    # Adam default
```

## Troubleshooting

### Issue: Dataset Download Fails
**Solution**: Download manually from PhysioNet and extract to `mitdb/` directory

### Issue: Memory Errors
**Solution**: Reduce number of records or use smaller window sizes

### Issue: Low Minority Class Recall
**Solution**: 
- Increase SMOTE ratio
- Adjust class weights
- Lower decision threshold

### Issue: Model Overfitting
**Solution**:
- Increase dropout
- Reduce model complexity
- Use cross-validation

## Comparison with Later Versions

| Aspect | Original | Leakage-Free |
|--------|----------|------------|
| SMOTE Timing | Before split | After split (training only) |
| Scaler Fitting | All data | Training only |
| Data Leakage | Possible | Eliminated |
| Methodology Status | Exploratory | Production-ready |

## Citation & References

- MIT-BIH Database: https://physionet.org/content/mitdb/
- NeuroKit2: https://neurokit2.readthedocs.io/
- scikit-learn: https://scikit-learn.org/
- TensorFlow: https://www.tensorflow.org/

## Related Notebooks

- `MIT_BIH_Arrythmia_week_3_4.ipynb` - Week 3-4 iteration
- `MIT_BIH_Arrythmia_Leakage_Free.ipynb` - Methodologically improved
- `Final_MIT_BIH_Leakage_Free.ipynb` - Final refined version

## Author Notes

This notebook served as the foundation for the thesis research. It establishes the basic pipeline that was refined through subsequent iterations addressing data leakage, methodological concerns, and performance optimization.

---

**Version**: Original Baseline  
**Status**: Reference/Educational  
**Successor**: MIT_BIH_Arrythmia_Leakage_Free.ipynb

# MIT-BIH Arrhythmia Leakage Free Notebook

## Overview

This notebook presents the **data leakage-free version** of the ECG arrhythmia classification pipeline. It addresses critical methodological issues identified in earlier iterations where data leakage compromised the validity of model evaluation.

## Purpose

- Implement ECG arrhythmia classification without data leakage
- Establish proper train/test validation methodology
- Evaluate multiple machine learning and deep learning models fairly
- Serve as a reference for proper experimental design in time-series classification

## What is Data Leakage?

Data leakage occurs when information from the test set inadvertently influences model training or validation. In ECG analysis, this can happen through:
- Using overlapping time windows between train and test sets
- Applying feature extraction across entire dataset before splitting
- Using statistics (mean, std) calculated from all data
- Not respecting temporal ordering of heartbeats

## Key Improvements from Earlier Versions

- ✓ Proper train/test split before any feature engineering
- ✓ Separate statistics (scaler parameters) fitted on training data only
- ✓ Test data processed with training statistics
- ✓ No mixing of records between train and test sets
- ✓ Temporal coherence respected during splitting

## Dataset Details

- **Source**: MIT-BIH Arrhythmia Database (PhysioNet)
- **Size**: 48 half-hour ECG recordings, ~110,000 annotated beats
- **Sampling Rate**: 360 Hz
- **Classes**: 
  - Normal (N): ~90,000 beats
  - Arrhythmia (non-N): ~20,000 beats (includes SVEB, VEB, F, /Q)
- **Challenge**: Highly imbalanced classification problem

## Notebook Components

### 1. Data Loading & Preprocessing
- Load ECG signals from MIT-BIH database
- Read annotation files (ground truth labels)
- Clean and filter raw ECG signals
- Detect R-peaks (QRS complexes)

### 2. Heartbeat Extraction
- Segment ECG signals around R-peaks
- Extract fixed-length windows (0.4-0.6 seconds)
- Normalize individual heartbeat waveforms
- Visualize segmented beats

### 3. Label Alignment
- Map beat locations to annotations
- Convert symbol codes to binary labels (Normal/Arrhythmia)
- Handle annotation mismatches
- Create balanced train/test splits

### 4. Feature Engineering
- **Temporal Features**: Pre-RR, post-RR, average RR intervals
- **Morphological Features**: Amplitude, energy, slope
- **QRS Features**: Duration, area
- Applied separately to train and test sets

### 5. Model Training Pipeline
- **Train/Test Split**: 70/30 or similar (respecting data boundaries)
- **Preprocessing**: StandardScaler fitted on training data only
- **Class Balancing**: SMOTE applied to training set only
- **Model Training**: Multiple algorithms tested

### 6. Models Evaluated
- **Logistic Regression**: Linear baseline
- **Random Forest**: Ensemble baseline
- **Small Neural Network (SNN)**: Simple deep learning
- **Convolutional Neural Network (CNN)**: Waveform-focused

### 7. Evaluation Metrics
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC-AUC Score
- Macro-averaged metrics (for imbalanced data)
- Threshold tuning for optimal decision boundaries

## Pipeline Execution

```
Load Raw ECG
    ↓
Filter & Clean Signals
    ↓
Detect R-Peaks
    ↓
Extract Heartbeats
    ↓
Align with Annotations
    ↓
Train/Test Split (BEFORE feature engineering)
    ↓
Extract Features (separately on each set)
    ↓
Apply SMOTE (training set only)
    ↓
Train Models
    ↓
Evaluate on Test Set
    ↓
Generate Results
```

## Key Features

- **Proper Methodology**: No data leakage
- **Reproducible**: Random seeds set for reproducibility
- **Comprehensive**: Multiple model types and evaluation metrics
- **Well-documented**: Comments explaining each step
- **Visualization**: Plots of signals, beats, confusion matrices

## Dependencies

```
wfdb>=1.1.0          # Read MIT-BIH database
neurokit2>=0.2.0     # ECG signal processing
scikit-learn>=0.24   # Machine learning models
imbalanced-learn     # SMOTE for class balancing
tensorflow>=2.0      # Deep learning models
numpy, pandas        # Data manipulation
matplotlib, seaborn  # Visualization
scipy                # Signal processing
```

## Installation

```bash
pip install wfdb neurokit2 scikit-learn imbalanced-learn tensorflow
```

## Usage Instructions

1. **Download Dataset**:
   ```python
   import wfdb
   wfdb.dl_database("mitdb", dl_dir="mitdb/")
   ```

2. **Run Notebook**:
   - Open in Jupyter Notebook
   - Execute cells sequentially from top to bottom

3. **Review Results**:
   - Check confusion matrices
   - Compare model performance
   - Analyze precision-recall curves

## Expected Results

Models should achieve:
- **Accuracy**: 70-90% depending on model and features
- **Macro F1-Score**: 50-65% (more meaningful for imbalanced data)
- **AUC-ROC**: 0.75-0.90
- **Minority Class Recall**: 40-70% (arrhythmia detection)

## Comparison with Original Version

| Aspect | Original | Leakage-Free |
|--------|----------|--------------|
| Data Split Timing | After feature engineering | Before features |
| Scaler Fitting | All data | Training only |
| SMOTE Application | All data | Training only |
| Test Data Contamination | Possible | None |
| Result Validity | Questionable | Reliable |

## Important Notes

- This is the corrected, methodologically sound version
- Results may differ from original due to leakage elimination
- Lower performance may be expected (reflects true model capability)
- Use this as reference for proper ECG classification methodology

## Troubleshooting

**Issue**: Dataset download fails
- **Solution**: Download manually from https://physionet.org/content/mitdb/

**Issue**: Memory errors with large datasets
- **Solution**: Reduce batch size or use subset of records

**Issue**: Low minority class recall
- **Solution**: Adjust SMOTE ratio or class weights in models

## Related Files

- `README.md` - Main project documentation
- `Final_MIT_BIH_Leakage_Free.md` - Final refined version
- `MIT_BIH_Arrythmia_week_3_4.md` - Early iteration (with leakage)

## References

- [MIT-BIH Database](https://physionet.org/content/mitdb/)
- [NeuroKit2 Documentation](https://neurokit2.readthedocs.io/)
- [scikit-learn Leakage Guide](https://scikit-learn.org/stable/)

---

**Version**: Data Leakage-Free Implementation  
**Status**: Production-ready for research

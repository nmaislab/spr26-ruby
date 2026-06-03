# Documentation Index

This directory contains comprehensive documentation for each file in the ECG Arrhythmia Classification project. Use this index to navigate the available documentation.

## Quick Links

### Main Documentation
- **[README.md](README.md)** - Main project overview, setup instructions, and results summary

### Notebook Documentation

#### Final/Production Version
- **[README_Final_MIT_BIH_Leakage_Free.md](README_Final_MIT_BIH_Leakage_Free.md)** - Final, production-ready version with all improvements

#### Development Versions (Timeline)
1. **[README_MIT_BIH_Arrythmia.md](README_MIT_BIH_Arrythmia.md)** - Original baseline notebook
2. **[README_MIT_BIH_Arrythmia_week_3_4.md](README_MIT_BIH_Arrythmia_week_3_4.md)** - Week 3-4 research iteration
3. **[README_MIT_BIH_Arrythmia_Leakage_Free.md](README_MIT_BIH_Arrythmia_Leakage_Free.md)** - First leakage-free version with proper methodology
4. **[README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md](README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md)** - Week 7 refinement and optimization

### Hardware/Script Documentation
- **[README_read_pulse.md](README_read_pulse.md)** - Hardware integration script for real-time ECG sensor data acquisition

---

## Documentation Organization

### By Use Case

**For Quick Start:**
→ Read [README.md](README.md) first

**For Understanding the Research:**
→ Follow the development timeline in order

**For Running Production Code:**
→ Use [README_Final_MIT_BIH_Leakage_Free.md](README_Final_MIT_BIH_Leakage_Free.md)

**For Hardware Integration:**
→ See [README_read_pulse.md](README_read_pulse.md)

### By Notebook

| Notebook | README | Purpose | Status |
|----------|--------|---------|--------|
| MIT_BIH_Arrythmia.ipynb | [Link](README_MIT_BIH_Arrythmia.md) | Original baseline | Reference |
| MIT_BIH_Arrythmia_week_3_4.ipynb | [Link](README_MIT_BIH_Arrythmia_week_3_4.md) | Week 3-4 research | Historical |
| MIT_BIH_Arrythmia_Leakage_Free.ipynb | [Link](README_MIT_BIH_Arrythmia_Leakage_Free.md) | Improved methodology | Production |
| MIT_BIH_Arrythmia_Leakage_Free_Week_7.ipynb | [Link](README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md) | Week 7 refinement | Production |
| Final_MIT_BIH_Leakage_Free.ipynb | [Link](README_Final_MIT_BIH_Leakage_Free.md) | Final version | **Use This** |

### By Script

| Script | README | Purpose |
|--------|--------|---------|
| read_pulse.py | [Link](README_read_pulse.md) | Hardware data acquisition |

---

## Key Concepts Across Documentation

### Data Leakage
Learn about this critical issue in:
- [README_MIT_BIH_Arrythmia_Leakage_Free.md](README_MIT_BIH_Arrythmia_Leakage_Free.md) - Detailed explanation
- [README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md](README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md) - Week 7 refinements and prevention strategies
- [README_Final_MIT_BIH_Leakage_Free.md](README_Final_MIT_BIH_Leakage_Free.md) - How it's prevented

### Models & Architectures
Explained in all notebook READMEs:
- Logistic Regression
- Random Forest
- K-Nearest Neighbors (KNN)
- Linear SVM
- Small Neural Network (SNN)
- Convolutional Neural Network (CNN)

### ECG Processing
Technical details in:
- [README_MIT_BIH_Arrythmia.md](README_MIT_BIH_Arrythmia.md) - Complete signal processing pipeline
- [README_read_pulse.md](README_read_pulse.md) - Hardware acquisition methods

### Evaluation Metrics
Detailed in:
- [README.md](README.md) - Results summary table
- All notebook READMEs - Per-model evaluation

---

## Research Timeline

```
Original Baseline (Week 1-2)
    ↓
[README_MIT_BIH_Arrythmia.md]
    ↓
Week 3-4 Experiments
    ↓
[README_MIT_BIH_Arrythmia_week_3_4.md]
    ↓
Leakage Identified & Fixed
    ↓
[README_MIT_BIH_Arrythmia_Leakage_Free.md]
    ↓
Week 7 Refinements
    ↓
[README_MIT_BIH_Arrythmia_Leakage_Free_Week_7.md]
    ↓
Final Production Version
    ↓
[README_Final_MIT_BIH_Leakage_Free.md]
```

---

## Common Questions

**Q: Which notebook should I use?**
A: Use [Final_MIT_BIH_Leakage_Free.ipynb](README_Final_MIT_BIH_Leakage_Free.md) for current work.

**Q: What's the difference between notebooks?**
A: See the timeline above. Each iteration improves upon previous versions.

**Q: Where do I start?**
A: Read [README.md](README.md) for project overview, then choose a notebook based on your needs.

**Q: How do I run the hardware script?**
A: See [README_read_pulse.md](README_read_pulse.md) for setup and usage instructions.

**Q: What is data leakage and why does it matter?**
A: Detailed explanation in [README_MIT_BIH_Arrythmia_Leakage_Free.md](README_MIT_BIH_Arrythmia_Leakage_Free.md#what-is-data-leakage).

---

## Dependencies Overview

All notebooks require:
```
wfdb              # MIT-BIH database interface
neurokit2         # ECG signal processing
scikit-learn      # Machine learning models
imbalanced-learn  # SMOTE for class balancing
tensorflow        # Deep learning models
numpy, pandas     # Data manipulation
matplotlib        # Visualization
seaborn           # Enhanced plotting
scipy             # Signal processing
```

Hardware script requires:
```
spidev            # SPI interface
paho-mqtt         # MQTT client
```

See [README.md](README.md) for installation instructions.

---

**Last Updated**: Current research phase  
**Total Documentation Files**: 6 READMEs + 1 Index  
**Total Project Files Documented**: 6 (5 notebooks + 1 script)

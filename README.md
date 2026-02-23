# Software Quality and Complexity Analysis Using Machine Learning

## Overview
This repository contains research code and experiments focused on understanding how code complexity and evolving requirements impact software quality in real-world automation projects. The project mines open-source GitHub repositories, extracts software metrics, and applies machine learning models to analyze quality patterns.

---

## Key Contributions
- Built a dataset by mining open-source automation projects from GitHub  
- Extracted code complexity metrics (LOC, cyclomatic complexity, inheritance depth, function calls)  
- Used closed GitHub issues as a proxy for evolving requirements (bugs, features, refactors)  
- Applied dimensionality reduction using autoencoder-based models to capture latent structure in software metrics  
- Analyzed relationships between complexity, requirement volatility, and software quality indicators  

---

## Data Sources
- Open-source automation projects (e.g., Robot Framework)
- GitHub issues and code repositories

---

## Methodology
1. Mine repositories and extract software metrics  
2. Parse issue histories to model requirement evolution  
3. Build a unified dataset linking code metrics and requirements data  
4. Train machine learning models to study software quality patterns  

---

## Results & Insights
- Demonstrated how evolving requirements and increasing complexity influence maintainability and reliability  
- Highlighted challenges of noisy and evolving engineering data in ML-based software quality prediction  

---

## Notes
This repository contains research prototypes and exploratory analysis developed during a research internship at IAS.

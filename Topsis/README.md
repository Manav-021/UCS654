# TOPSIS Implementation – Topsis-Manavjot-102317270

A Python package and web service implementation of the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**.

This project was developed as part of an academic assignment to demonstrate:

- command line execution  
- packaging and publishing on PyPI  
- deployment as a web service  

---

## What is TOPSIS?

TOPSIS is a multi-criteria decision-making technique used to rank alternatives by comparing their geometric distance from an ideal best and an ideal worst solution.

The alternative closest to the ideal best and farthest from the ideal worst receives the highest preference.

---

## Methodology

The implementation follows the standard TOPSIS procedure:

1. Normalize the decision matrix  
2. Apply weights to the normalized matrix  
3. Determine the ideal best and ideal worst values  
4. Calculate the distance of each alternative from the best and worst  
5. Compute the TOPSIS score  
6. Rank alternatives based on descending score  

---

## Installation (from PyPI)

```bash
pip install Topsis-Manavjot-102317270

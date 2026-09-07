# Genetic Cross Calculator
   **Live app:** https://genetic-crosscalculator-ccqmhtmyvhvvzzdbeendek.streamlit.app

A Streamlit app that calculates and visualizes Mendelian genetic cross outcomes for any two parents, 
across any number of traits.

## Features

- Input any two parent genotypes, for any number of traits
- Generates and displays the full Punnett square
- Calculates genotypic and phenotypic ratios
- Interactive buttons to reveal each result (Punnett square, ratios, etc.) on demand
- In progress: a forked diagram showing branching probabilities across traits

## How to run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Why I built this

I wanted a tool that could handle Mendelian crosses generally with any number of traits, not just 
single-trait textbook examples, as a way to build hands-on intuition for genetics while practicing 
building a usable software.

## Status

Actively being extended — currently working on the forked probability diagram as the next feature.

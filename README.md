# Economic Stress & Behaviour Change Model

## Overview

This project investigates how economic stress — measured through unemployment, inflation, and GDP contraction — influences collective behaviour and social mood across European countries.

Using data from the IMF, Eurostat, ACLED (Armed Conflict Location & Event Data), and Google Trends, the study examines whether economic downturns predict increases in protest activity and social anxiety.

The project applies time series analysis and event correlation methods grounded in computational social science and behavioural economics.

## Research Question

To what extent do economic shocks predict changes in protest activity and public anxiety across European countries?

## Hypotheses

- H1: Rising unemployment is associated with increased protest activity
- H2: Inflation spikes correlate with heightened social anxiety (Google Trends)
- H3: GDP contraction precedes peaks in protest frequency
- H4: The 2020 COVID-19 economic shock produced measurable behavioural responses distinct from other recessions

## Data Sources

| Variable | Source |
|---|---|
| Unemployment rate | Eurostat |
| Inflation rate | IMF / World Bank |
| GDP growth | World Bank |
| Protest events | ACLED |
| Social anxiety (search volume) | Google Trends (via pytrends) |

## Countries Included (initial scope)

Portugal, Spain, France, Germany, Italy, Netherlands, Greece

**Time period:** 2010–2024

## Methodology

1. Data collection — automated extraction from Eurostat API, ACLED API, and Google Trends
2. Time series construction — monthly panel of economic indicators, protest counts, and search indices
3. Event correlation — identifying peaks in protest activity relative to economic shocks
4. Granger causality testing — assessing whether economic variables predict protest frequency
5. Visualization — time series overlays, heatmaps, correlation matrices

## Tools

- Python (pandas, numpy, matplotlib, seaborn)
- Statsmodels (time series analysis, Granger causality)
- Pytrends (Google Trends API)
- Streamlit (interactive dashboard)

## Project Structure

The repository is organized as follows:

- `data/raw/` — Original datasets from Eurostat, IMF, ACLED, and Google Trends
- `data/processed/` — Cleaned and merged time series datasets
- `notebooks/` — Jupyter notebooks for data collection, EDA, and modeling
- `src/` — Reusable Python functions for data processing and analysis
- `figures/` — Saved plots and visualizations
- `dashboard/` — Streamlit dashboard application
- `README.md` — Project documentation
- `requirements.txt` — Python dependencies

## Key Findings

### Economic Stress Index (2010–2023)

A composite economic stress index was constructed from unemployment, inflation, and GDP growth. The 2020 COVID-19 shock produced the highest stress levels across all countries, with Spain (2.86) and Greece (2.31) most affected. The 2011–2013 Eurozone crisis hit Greece (peak stress: 3.91 in 2011), Portugal (2.56 in 2012), and Spain (2.48 in 2012) hardest.

### Correlation Analysis

| Relationship | Correlation |
|---|---|
| Economic Stress Index ↔ "Economic crisis" searches | +0.700 |
| Unemployment ↔ "Economic crisis" searches | +0.650 |
| Economic Stress Index ↔ Protest events | +0.248 |
| Unemployment ↔ Protest events | +0.273 |
| Economic Stress Index ↔ Anxiety | +0.141 |

### Within-Country: Stress vs Protests

| Country | Correlation |
|---|---|
| Greece | +0.728 |
| Spain | +0.585 |
| Portugal | +0.428 |
| Germany | +0.076 |
| France | −0.228 |
| Italy | −0.221 |
| Netherlands | −0.159 |

Southern European countries show the strongest positive associations between economic stress and protest activity. France and Italy show weak or negative correlations, suggesting institutional factors mediate the translation of economic grievances into street mobilization.

### Granger Causality Test (Portugal)

Unemployment does not Granger-cause anxiety at conventional significance levels (p > 0.05), suggesting that economic stress and mental health indicators follow independent long-term trends rather than short-term causal relationships.

### Key Insight

Economic stress strongly predicts information-seeking behaviour ("economic crisis" Google searches) and correlates moderately with protest activity in Southern Europe. However, the relationship is heterogeneous across countries, reinforcing the importance of country-level institutional analysis.

## Current Status

- [x] Data collection — Eurostat, World Bank, Google Trends
- [x] Economic stress index construction
- [x] Correlation analysis — pooled and within-country
- [x] Granger causality testing
- [x] Visualizations
- [ ] ACLED API integration (currently using curated sample)
- [ ] Dashboard deployment

## Limitations

- ACLED protest data used in this version are curated approximations based on public summaries. Full ACLED access requires registration.
- Google Trends data are relative indices (0–100), not absolute search volumes.
- Correlation does not imply causation. Observed relationships may reflect confounding variables.
- National-level data masks regional and city-level variation.
- Granger causality tests with 14 annual observations have limited statistical power.

## Future Work

- Register with ACLED and replace curated sample with exact event data
- Expand to monthly frequency for more robust time series analysis
- Incorporate social media sentiment (Twitter/X API)
- Apply machine learning for protest prediction
- Deploy interactive Streamlit dashboard
- Build an "Early Warning Index" for social instability

## Limitations

- Protest data coverage varies by country and source
- Google Trends data is relative, not absolute
- Correlation does not imply causation
- Economic shocks may have delayed behavioural effects not captured by contemporaneous analysis

## Future Work

- Expand to Latin American and Asian countries
- Incorporate social media sentiment (Twitter/X API)
- Apply machine learning for protest prediction
- Deploy interactive Streamlit dashboard
- Build an "Early Warning Index" for social instability

## Author

Undergraduate research project in Sociology, with a focus on computational social science, quantitative methods, and policy analytics.

*Part of a portfolio developed for MSc applications in Social Data Science.*

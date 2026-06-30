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

## Current Status

- [ ] Data collection
- [ ] Exploratory data analysis
- [ ] Time series modeling
- [ ] Granger causality testing
- [ ] Dashboard deployment

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

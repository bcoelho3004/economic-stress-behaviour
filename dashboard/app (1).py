"""
Streamlit Dashboard — Economic Stress & Behaviour Change
=========================================================
Interactive exploration of economic stress, protest activity,
and social anxiety across 7 European countries (2010–2023).
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Economic Stress & Behaviour", page_icon="📉", layout="wide")

st.title("Economic Stress & Behaviour Change in Europe")
st.markdown("Portugal · Spain · France · Germany · Italy · Netherlands · Greece (2010–2023)")

@st.cache_data
def load_data():
    return pd.read_csv("economic_stress_full_dataset.csv")

df = load_data()

st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select countries",
    options=sorted(df["country"].unique()),
    default=["Portugal", "Spain", "Greece"]
)
selected_years = st.sidebar.slider(
    "Select year range",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=(2010, 2023)
)

filtered = df[(df["country"].isin(selected_countries)) & (df["year"] >= selected_years[0]) & (df["year"] <= selected_years[1])]

st.subheader("Summary Statistics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Avg Stress Index", f"{filtered['stress_index'].mean():.2f}")
with col2:
    st.metric("Avg Protest Events", f"{filtered['protest_events'].mean():.0f}")
with col3:
    st.metric("Avg Anxiety Index", f"{filtered['anxiety'].mean():.1f}")
with col4:
    st.metric("Avg Unemployment (%)", f"{filtered['unemployment'].mean():.1f}")

st.subheader("Economic Stress Index Over Time")
fig1, ax1 = plt.subplots(figsize=(10, 5))
for country in selected_countries:
    data = filtered[filtered["country"] == country].sort_values("year")
    if not data.empty:
        ax1.plot(data["year"], data["stress_index"], marker="o", label=country, linewidth=2)
ax1.set_xlabel("Year")
ax1.set_ylabel("Stress Index")
ax1.axhline(y=0, color="black", linestyle="--", alpha=0.3)
ax1.legend()
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

st.subheader("Economic Stress vs Protest Events")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered, x="stress_index", y="protest_events", hue="country", s=100, ax=ax2)
sns.regplot(data=filtered, x="stress_index", y="protest_events", scatter=False, ax=ax2, color="red")
ax2.set_xlabel("Economic Stress Index")
ax2.set_ylabel("Protest Events")
ax2.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

st.subheader("Economic Stress vs Mental Health")
fig3, axes3 = plt.subplots(1, 2, figsize=(14, 5))
for country in selected_countries:
    data = filtered[filtered["country"] == country]
    axes3[0].scatter(data["stress_index"], data["anxiety"], s=80, label=country)
axes3[0].set_xlabel("Stress Index")
axes3[0].set_ylabel("Anxiety (Google Trends)")
axes3[0].set_title("Stress vs Anxiety")
axes3[0].legend(fontsize=7)
axes3[0].grid(True, alpha=0.3)
for country in selected_countries:
    data = filtered[filtered["country"] == country]
    axes3[1].scatter(data["stress_index"], data["depression"], s=80, label=country)
axes3[1].set_xlabel("Stress Index")
axes3[1].set_ylabel("Depression (Google Trends)")
axes3[1].set_title("Stress vs Depression Searches")
axes3[1].legend(fontsize=7)
axes3[1].grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig3)

st.subheader("Correlation Matrix")
vars_to_check = ["stress_index", "unemployment", "inflation", "gdp_growth", "protest_events", "anxiety", "economic crisis", "depression"]
corr = filtered[vars_to_check].corr()
fig4, ax4 = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".3f", square=True, ax=ax4)
ax4.set_title("Full Correlation Matrix")
st.pyplot(fig4)

st.subheader("Country Deep Dive")
deep_country = st.selectbox("Select a country:", sorted(filtered["country"].unique()))
country_data = filtered[filtered["country"] == deep_country].sort_values("year")
fig5, ax5_left = plt.subplots(figsize=(12, 5))
ax5_left.plot(country_data["year"], country_data["stress_index"], "darkred", marker="o", linewidth=2, label="Stress Index")
ax5_left.set_ylabel("Stress Index", color="darkred")
ax5_left.tick_params(axis="y", labelcolor="darkred")
ax5_right = ax5_left.twinx()
ax5_right.plot(country_data["year"], country_data["protest_events"], "navy", marker="s", linewidth=2, linestyle="--", label="Protest Events")
ax5_right.set_ylabel("Protest Events", color="navy")
ax5_right.tick_params(axis="y", labelcolor="navy")
ax5_left.set_title(f"{deep_country}: Economic Stress vs Protest Events (2010-2023)", fontsize=14)
ax5_left.set_xlabel("Year")
ax5_left.grid(True, alpha=0.3)
lines1, labels1 = ax5_left.get_legend_handles_labels()
lines2, labels2 = ax5_right.get_legend_handles_labels()
ax5_left.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.tight_layout()
st.pyplot(fig5)
corr_country = country_data["stress_index"].corr(country_data["protest_events"])
st.metric(f"Stress-Protest Correlation ({deep_country})", f"{corr_country:.3f}")

st.subheader("Full Dataset")
st.dataframe(filtered.sort_values(["country", "year"]), use_container_width=True)
st.markdown("---")
st.markdown("*Data sources: Eurostat, World Bank, Google Trends · Undergraduate project in Computational Social Science*")

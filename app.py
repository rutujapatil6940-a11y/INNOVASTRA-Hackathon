import streamlit as st
import pandas as pd

st.title("INNOVASTRA Talent Scout")

# Metrics row
col1, col2, col3 = st.columns(3)
col1.metric("TOTAL CANDIDATES", "5")
col2.metric("HIGH SCORERS", "2")
col3.metric("AVG. SKILL MATCH", "88%")

# Ranking table
st.subheader("Top Candidates Rankings")
df = pd.read_csv("final_rankings.csv") # Aapki validated file
st.table(df.head(5))

# Sidebar for Criteria
st.sidebar.header("Ranking Criteria")
st.sidebar.write("Scoring Algorithm: rank_candidates.py")
st.sidebar.checkbox("Python")
st.sidebar.checkbox("SQL")
st.sidebar.checkbox("Spark")
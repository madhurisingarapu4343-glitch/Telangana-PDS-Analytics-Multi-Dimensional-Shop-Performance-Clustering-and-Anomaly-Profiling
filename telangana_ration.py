import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# TITLE
st.title("Telangana PDS Analytics Dashboard")

# LOAD DATA
df = pd.read_csv("final_dataset.csv")

# LOAD PCA DATA
pca_data = pd.read_csv("pca_data.csv")

# SIDEBAR FILTERS
district = st.sidebar.selectbox(
    "Select District",
    df['distName'].unique()
)

year = st.sidebar.selectbox(
    "Select Year",
    df['year'].unique()
)

# FILTER DATA
filtered_df = df[
    (df['distName'] == district) &
    (df['year'] == year)
]

# SHOW FILTERED DATA
st.subheader("Filtered Dataset")
st.dataframe(filtered_df.head())

# CLUSTER DISTRIBUTION
st.subheader("Cluster Distribution")

st.bar_chart(
    filtered_df['cluster'].value_counts()
)

# PCA VISUALIZATION
st.subheader("PCA Cluster Visualization")

fig, ax = plt.subplots(figsize=(8,5))

scatter = ax.scatter(
    pca_data['PCA1'],
    pca_data['PCA2'],
    c=pca_data['cluster']
)

st.pyplot(fig)

# MAP VISUALIZATION
st.subheader("Shop Locations Map")

map_data = filtered_df[
    ['latitude', 'longitude']
].dropna()

st.map(map_data)

# SHOP SEARCH
st.subheader("Shop Search")

shop_input = st.text_input(
    "Enter Shop Number"
)

if shop_input:

    shop_data = df[
        df['shopNo'].astype(str) == shop_input
    ]

    st.dataframe(shop_data)

# ANOMALY SHOPS
st.subheader("Anomaly Shops")

anomalies = filtered_df[
    filtered_df['dbscan_cluster'] == -1
]

st.dataframe(anomalies)

# PROJECT INSIGHTS
st.subheader("Project Insights")

st.write("""
- Cluster 1 represents high portability shops.
- Cluster 3 represents low utilization shops.
- DBSCAN identified anomaly shops.
- PCA visualized shop behavior patterns.
""")
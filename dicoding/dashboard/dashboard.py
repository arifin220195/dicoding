import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
day_df = pd.read_csv("C:\\Users\\userxyz\\dicoding\\dashboard\\cleaned_day.csv")
hour_df = pd.read_csv("C:\\Users\\userxyz\\dicoding\\dashboard\\cleaned_hour.csv")

# Convert date column to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Sidebar filters
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ['All', 'Spring', 'Summer', 'Fall', 'Winter'])

# Map season to numerical values
season_mapping = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
if selected_season != 'All':
    day_df = day_df[day_df['season'] == season_mapping[selected_season]]

# Main Dashboard Title
st.title("📊 Dashboard Peminjaman Sepeda")

# Display Metrics
col1, col2 = st.columns(2)
col1.metric("Total Peminjaman", f"{day_df['cnt'].sum():,}")
col2.metric("Rata-rata Peminjaman Per Hari", f"{day_df['cnt'].mean():,.2f}")

# Line Chart: Tren Peminjaman Sepeda
st.subheader("Tren Peminjaman Sepeda Per Hari")
fig = px.line(day_df, x='dteday', y='cnt', title="Tren Peminjaman Sepeda Harian")
st.plotly_chart(fig)

# Bar Chart: Pengaruh Cuaca
st.subheader("Pengaruh Cuaca Terhadap Peminjaman Sepeda")
fig2 = px.box(day_df, x='weathersit', y='cnt', title="Distribusi Peminjaman Berdasarkan Cuaca")
st.plotly_chart(fig2)

# Conclusion
st.subheader("📌 Insight & Kesimpulan")
st.write("- Peminjaman sepeda meningkat pada musim panas.")
st.write("- Cuaca buruk mengurangi jumlah peminjaman.")
st.write("- Pola peminjaman harian menunjukkan tren naik selama akhir pekan.")

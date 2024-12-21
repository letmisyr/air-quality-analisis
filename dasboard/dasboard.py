import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
df = pd.read_csv('all_data.csv')

# Create dashboard title
st.title("Dashboard Analisis Kualitas Udara")
st.write("Dashboard ini menampilkan analisis kualitas udara dari beberapa station.")

# Group data by year and station, calculate mean AQI
station_avg_aqi_year = df.groupby(['year', 'station'])['AQI'].mean().reset_index()

# Function to plot AQI over time
def plot_aqi_over_time(station_avg_aqi, x_label, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    for station in station_avg_aqi['station'].unique():
        station_data = station_avg_aqi[station_avg_aqi['station'] == station]
        ax.plot(station_data[x_label], station_data['AQI'], label=f"Station: {station}")
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel('AQI')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(True)
    return fig

# Plot AQI over time by year
st.title("Analisis Kualitas Udara tahunan")
fig = plot_aqi_over_time(station_avg_aqi_year, 'year', 'AQI Over Time by Station')
st.pyplot(fig)

# Group data by month and station, calculate mean AQI
station_avg_aqi_month = df.groupby(['month', 'station'])['AQI'].mean().reset_index()

# Plot AQI over time by month
st.title("Analisis Kualitas Udara bulanan")
fig = plot_aqi_over_time(station_avg_aqi_month, 'month', 'AQI Over Time by Station')
st.pyplot(fig)

# Group data by day and station, calculate mean AQI
station_avg_aqi_day = df.groupby(['day', 'station'])['AQI'].mean().reset_index()

# Plot AQI over time by day
st.title("Analisis Kualitas Udara harian")
fig = plot_aqi_over_time(station_avg_aqi_day, 'day', 'AQI Over Time by Station')
st.pyplot(fig)

# Calculate correlation matrix
correlation_matrix = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()

# Function to plot correlation matrix
def plot_correlation_matrix(correlation_matrix):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    ax.set_title("Correlation Matrix of Variables")
    return fig

# Plot correlation matrix
st.title("Matriks Korelasi Kualitas Udara")
fig = plot_correlation_matrix(correlation_matrix)
st.pyplot(fig)

# Define pollutants and their colors
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
pollutant_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FF6666', '#FF7F0E']

# Calculate sum of pollutant concentrations
total_concentrations = df[pollutants].sum()

# Create DataFrame for concentrations
concentration_data = pd.DataFrame({
    "Pollutant": pollutants,
    "Concentration": total_concentrations
})

# Function to plot donut chart
def plot_donut_chart(concentration_data, pollutant_colors):
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(concentration_data['Concentration'], labels=concentration_data['Pollutant'],
                                      autopct='%1.1f%%', startangle=90, colors=pollutant_colors,
                                      wedgeprops=dict(width=0.4))
    ax.set_title("Pollutant Concentrations at All Stations")
    ax.legend(wedges, concentration_data['Pollutant'], title="Pollutants", loc="upper left")
    return fig

# Plot donut chart
st.title("Konsentrasi Polutan")
fig = plot_donut_chart(concentration_data, pollutant_colors)
st.pyplot(fig)
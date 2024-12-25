import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st



# Create dashboard title
st.title("Dashboard Analisis Kualitas Udara")
st.write("Dashboard ini menampilkan analisis kualitas udara dari beberapa station.")

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

try:
    file = 'all_data.csv'
    df = load_data()
    st.header("Original DataFrame")
    st.write(df.head(100))
    

    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

    with tab1:
        st.header("Analisis 1")
        station_avg_aqi = df.groupby(['year', 'station'])['AQI'].mean().reset_index()

        # Function to plot AQI over time
        def plot_aqi_over_time(station_avg_aqi, x_label='year'):
            unique_stations = station_avg_aqi['station'].unique()

            # Divide the station into 3 groups
            num_groups = 3
            group_stations = np.array_split(unique_stations, num_groups)

            fig, axes = plt.subplots(num_groups, 1, figsize=(12, 6 * num_groups))

            for i, group_stations in enumerate(group_stations):
                group_data = station_avg_aqi[station_avg_aqi['station'].isin(group_stations)]
                
                for station in group_stations:
                    station_data = group_data[group_data['station'] == station]
                    axes[i].plot(station_data[x_label], station_data['AQI'], label=f"Station: {station}")

                axes[i].set_title(f'Group {i} - AQI setiap tahun')
                axes[i].set_xlabel(x_label)
                axes[i].set_ylabel('AQI')
                axes[i].legend(loc='upper left', bbox_to_anchor=(1, 1))
                axes[i].grid(True)
            
            fig.tight_layout()
            return fig

        # Plot AQI over time by year
        fig = plot_aqi_over_time(station_avg_aqi)
        st.pyplot(fig)

        with st.expander("See explanation"):
            st.write("""Dari grafik yang ditampilkan, dapat dilihat perubahan kualitas udara (AQI) setiap tahunnya di setiap kota.\
                - Aotizhongxin: 2013 hingga 2017 AQI cenderung stabil dengan sedikit fluktuasi, menunjukkan kualitas udara yang relatif konsisten di wilayah ini.\
                - Changping: Terdapat peningkatan yang signifikan dalam AQI antara tahun 2014 dan 2015, yang mengindikasikan adanya waktu dengan kualitas udara yang buruk, tapi membaik setelahnya.\
                - Dingling: Tidak ada perubahan yang terlalu signifikan, cenderung stabil dengan sedikit fluktuasi.\
                - Dongsi: Cenderung fluktuatif tetapi masih lebih rendah dari AQI nya di bandingkan station lain.\
                - Guanyuan: terus mengalami peningkatan hingga 2017.\
                - Gucheng: Mengalami peningkatan signifikan di 2013-2014, kemudian stabil, dan terus menurun hingga 2017.\
                - Huairou: AQI tetap stabil di kisaran rendah, menunjukkan bahwa Huairou memiliki kualitas udara yang lebih baik dibandingkan stasiun lainnya.\
                - Nongzhanguan: AQI meningkat signifikan pada tahun 2016 hingga 2017, menunjukkan kualitas udara di akhir periode pengamatan memburuk.\
                - Shunyi: AQI mengalami fluktuasi 2013-2014, kemudian baru stabil di tahun setelahnya.\
                - Tiantan: Peningkatan AQI paling signifikan di antara stasiun lainnya, terutama dari 2014 hingga 2017, menunjukkan kualitas udara yang terus memburuk.\
                - Wanliu: periode 2014-2016 menunjukkan kualitas udaranya perlahan membaik, walau setelahnya kembali naik\
                - Wanshouxigong: relafif stabil dengan sedikit fluktuasi.""")
            
        def plot_air_quality_distribution(df): 
            plt.figure(figsize=(12, 6))

            # countplot every station
            sns.countplot(x='station', hue='AQI Category', data=df, palette='tab10')

            plt.title("Distribusi Kualitas Udara di Setiap Kota", fontsize=16)
            plt.xlabel("Kota", fontsize=12)
            plt.ylabel("Frekuensi", fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.legend(loc='upper left', title="Kualitas Udara", fontsize=10, bbox_to_anchor=(1, 1))
            plt.tight_layout()
            return plt.gcf()
        
        fig = plot_air_quality_distribution(df)
        st.pyplot(fig)

    with tab2:
        st.header("Analisis 2")
        # Group data by month and station, calculate mean AQI
        station_hourly_aqi = df.groupby(['station', 'hour'])['AQI'].mean().reset_index()
    
        def plot_hourly_aqi(station_hourly_aqi, x_label='hour'):
            unique_stations = station_avg_aqi['station'].unique()
            # Divide the station into 3 groups
            num_groups = 3
            group_stations = np.array_split(unique_stations, num_groups)

            fig, axes = plt.subplots(num_groups, 1, figsize=(12, 6 * num_groups))

            for i, group_stations in enumerate(group_stations):
                group_data = station_hourly_aqi[station_avg_aqi['station'].isin(group_stations)]
                
                for station in group_stations:
                    station_data = group_data[group_data['station'] == station]
                    axes[i].plot(station_data[x_label], station_data['AQI'], label=f"Station: {station}")

                axes[i].set_title(f'Group {i+1} - AQI setiap jam')
                axes[i].set_xlabel(x_label)
                axes[i].set_ylabel('AQI')
                axes[i].legend(loc='upper left', bbox_to_anchor=(1, 1))
                axes[i].grid(True)
            plt.tight_layout()
            return fig

        fig = plot_aqi_over_time(station_hourly_aqi, x_label='hour')
        st.pyplot(fig)

    with tab3:
        st.header("Analisis 3")
        # Calculate correlation matrix
        correlation_matrix = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()

        # Function to plot correlation matrix
        def plot_correlation_matrix(correlation_matrix):
            fig, ax = plt.subplots(figsize=(12, 10))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
            ax.set_title("Correlation Matrix of Variables")
            return fig

        # Plot correlation matrix
        st.subheader("Matriks Korelasi Kualitas Udara")
        fig = plot_correlation_matrix(correlation_matrix)
        st.pyplot(fig)

except Exception as e:
    st.error(f"Error : {str(e)}")

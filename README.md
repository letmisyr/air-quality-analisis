# air-quality-analisis
Merupakan analisis kualitas udara di beberapa kota\
daftar nama-nama kota 
1. Aotizhongxin
2. Changping
3. Dingling
4. Dongsi
5. Guanyuan
6. Gucheng
7. Huairou
8. Nongzhanguan
9. Shunyi
10. Tiantan
11. Wanliu
12. Wanshouxigong

## setup Environment - google colab

from google.colab import drive
drive.mount('/content/drive')

!pip install -r requirements.txt
!pip install -r /content/drive/MyDrive/path/to/requirements.txt
data_dir = '/content/drive/MyDrive/Air-quality-dataset/' 

## setup Environment - Terminal 
1. Clone repository ini:
   
   git clone https://github.com/letmisyr/air-quality-dashboard.git
   cd air-quality-dashboard
   
2. Install dependensi:
   pip install -r requirements.txt
   
3. Tempatkan file data:
   - Pastikan all_data.csv berada di direktori root proyek
   - Kolom yang diperlukan: 'year', 'station', 'hour', 'AQI', 'AQI Category', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM'

## Run streamlit app
streamlit run dashboard.py\

You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://10.16.71.56:8502






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

## Library dan Packages yang digunakan

import pandas as pd\
import matplotlib.pyplot as plt\
import seaborn as sns\
import glob\
import os


## akses dataset menggunakan colab
from google.colab import drive
drive.mount('/content/drive')  

data_dir = '/content/drive/MyDrive/Air-quality-dataset/' 


## Run streamlit app
streamlit run dasrboard.py
![Screenshot 2024-12-22 190221](https://github.com/user-attachments/assets/4882b8b1-f1b0-4152-b779-113ecc3e00e5)


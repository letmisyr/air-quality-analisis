# air-quality-analisis

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

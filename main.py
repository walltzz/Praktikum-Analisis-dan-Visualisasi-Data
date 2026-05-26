import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# 0. LOAD & CLEANING DATA (Langkah 1 & 2)

# Membaca data lokal di folder yang sama
df = pd.read_csv('data_praktikum_analisis_data - data_praktikum_analisis_data.csv')

# Bersihkan data anomali (Harga <= 0) dan ubah tipe data tanggal
df = df[df['Price'] > 0]
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Menyesuaikan penamaan kolom jika belum ada
if 'Price_Per_Unit' not in df.columns:
    df['Price_Per_Unit'] = df['Price']


# TUGAS 1: Identifikasi Produk "Underperformer"

print("--- Menjalankan Tugas 1: Scatter Plot Underperformer ---")
product_analysis = df.groupby('ProductID').agg({
    'Price_Per_Unit': 'mean',
    'Quantity': 'sum'
}).reset_index()

avg_price_all = product_analysis['Price_Per_Unit'].mean()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=product_analysis, x='Price_Per_Unit', y='Quantity', alpha=0.7)
plt.axvline(avg_price_all, color='red', linestyle='--', label=f'Rata-rata Harga ({avg_price_all:.2f})')
plt.title('Identifikasi Produk Underperformer')
plt.xlabel('Price Per Unit')
plt.ylabel('Total Quantity Terjual')
plt.legend()
plt.tight_layout()
# Simpan grafik sebagai gambar untuk dipasang di GitHub nanti
plt.savefig('tugas1_underperformer.png')
plt.show()



# TUGAS 2 & 5: Segmentasi Pelanggan (RFM Analysis)

print("\n--- Menjalankan Tugas 2 & 5: RFM Analysis ---")
snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm['RFM_Group'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
print(rfm.head())



# TUGAS 3: Analisis Kontribusi Kategori (Efisiensi Iklan)

print("\n--- Menjalankan Tugas 3: Bar Chart Efisiensi Kategori ---")
category_perf = df.groupby('Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
}).reset_index()

category_perf['Efficiency_Ratio'] = category_perf['Total_Sales'] / category_perf['Ad_Budget']
category_perf = category_perf.sort_values(by='Efficiency_Ratio', ascending=True)

plt.figure(figsize=(10, 5))
sns.barplot(data=category_perf, x='Efficiency_Ratio', y='Category', palette='mako')
plt.title('Efisiensi Kategori Produk (Urut dari Paling Tidak Efisien)')
plt.xlabel('Rasio Efisiensi (Sales / Ad Budget)')
plt.ylabel('Kategori Produk')
plt.tight_layout()
# Simpan grafik sebagai gambar untuk GitHub
plt.savefig('tugas3_efisiensi_kategori.png')
plt.show()



# TUGAS 4: Uji Hipotesis Sederhana (Dampak Iklan)

print("\n--- Menjalankan Tugas 4: Uji Hipotesis Sederhana ---")
median_ad = df['Ad_Budget'].median()
iklan_tinggi = df[df['Ad_Budget'] > median_ad]['Total_Sales']
iklan_rendah = df[df['Ad_Budget'] <= median_ad]['Total_Sales']

print(f"Median Ad Budget: {median_ad}")
print(f"Rata-rata Penjualan Kelompok Iklan Tinggi: {iklan_tinggi.mean():.2f}")
print(f"Rata-rata Penjualan Kelompok Iklan Rendah: {iklan_rendah.mean():.2f}")



# TUGAS 6: Pendalaman Teknik: Regresi Linear Sederhana

print("\n--- Menjalankan Tugas 6: Regresi Linear Sederhana ---")
X = df[['Ad_Budget']]
y = df['Total_Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Koefisien Iklan (Beta 1): {model.coef_[0]:.4f}")
print(f"Intercept (Beta 0): {model.intercept_:.4f}")
print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test):.4f}")
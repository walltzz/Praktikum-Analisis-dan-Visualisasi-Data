# Laporan Praktikum: Optimasi Strategi Pemasaran E-commerce

### 1. Business Question
* [cite_start]**Tugas 1:** Apakah harga unit produk yang terlalu mahal menjadi penghambat utama volume penjualan (Quantity)? [cite: 87, 95]
* [cite_start]**Tugas 2:** Siapa saja segmen pelanggan terbaik yang berhak mendapatkan voucher loyalitas berdasarkan RFM Analysis? [cite: 96, 102]
* [cite_start]**Tugas 3:** Kategori produk mana yang memiliki efisiensi iklan paling rendah? [cite: 104, 107]
* [cite_start]**Tugas 4 & 6:** Apakah peningkatan anggaran iklan (`Ad_Budget`) memprediksi peningkatan penjualan (`Total_Sales`) secara signifikan? [cite: 110, 139, 140]

### 2. Data Wrangling
* [cite_start]**Pembersihan Anomali:** Menghapus baris transaksi dengan harga produk (`Price`) <= 0[cite: 62].
* [cite_start]**Transformasi Data:** Mengonversi kolom `Order_Date` menjadi tipe `datetime` untuk kalkulasi rentang hari transaksi[cite: 63, 118].

### 3. Insights
* **Tugas 1 (Scatter Plot Underperformer):**
  *(Isi analisis berdasarkan hasil grafik kelompokmu)*
  ![Scatter Plot](tugas1_underperformer.png)

* **Tugas 2 (RFM Analysis):**
  [cite_start]Pelanggan dengan segmen tertinggi (Skor 555) diidentifikasi sebagai pelanggan loyal[cite: 138].

* **Tugas 3 (Efisiensi Kategori):**
  *(Sebutkan kategori yang paling tidak efisien berdasarkan grafik)*
  ![Bar Chart](tugas3_efisiensi_kategori.png)

* **Tugas 4 & 6 (Uji Hipotesis & Regresi):**
  [cite_start]Rata-rata penjualan kelompok iklan tinggi memberikan performa yang lebih baik[cite: 111]. [cite_start]Parameter regresi yang didapatkan: nilai R2 Score sebesar `...`[cite: 159].

### 4. Recommendation
* [cite_start]**Rekomendasi Produk:** Lakukan strategi *bundling* atau diskon untuk produk underperformer agar membebaskan arus kas[cite: 88].
* [cite_start]**Rekomendasi Pemasaran:** Alokasikan voucher loyalitas hanya kepada segmen pelanggan bernilai tinggi[cite: 102].
* [cite_start]**Rekomendasi Budget:** Kurangi anggaran iklan pada kategori yang tidak efisien dan alihkan ke kategori yang produktif[cite: 107].
Berikut ini adalah **isi lengkap `README.md`** yang sudah tertata rapi, dengan bagian **"Cara Menjalankan Aplikasi"** dibuat berurutan dan menyatu di dalam file yang utuh:

---

### ✅ `README.md`

```markdown
# 📈 Stock Price Predictor (CNN + LSTM)

Aplikasi prediksi harga saham berbasis kombinasi **CNN (Convolutional Neural Network)** dan **LSTM (Long Short-Term Memory)** untuk lima saham bank besar di Indonesia: **BCA (BBCA), BRI (BBRI), Mandiri (BMRI), BNI (BBNI), dan BSI (BRIS)**.  
Aplikasi ini dibangun menggunakan **Streamlit** untuk antarmuka interaktif dan **yFinance** sebagai sumber data historis.

---

## 🚀 Fitur Utama

- ✅ Ambil data harga saham historis langsung dari Yahoo Finance
- ✅ Arsitektur model CNN + LSTM untuk menangkap pola jangka pendek & panjang
- ✅ Visualisasi interaktif hasil prediksi vs harga aktual
- ✅ Prediksi harga saham untuk hari berikutnya (next-day forecast)
- ✅ Perhitungan metrik evaluasi: RMSE & MAE
- ✅ Streamlit UI real-time, user-friendly

---

## 🧠 Arsitektur Model

```

Input (window size N)
↓
Conv1D → MaxPooling1D
↓
LSTM Layer
↓
Dropout → Dense Output

````

---

## 📦 Teknologi yang Digunakan

- [Python 3.10](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [yFinance](https://pypi.org/project/yfinance/)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)

---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/afiffathin31/Stock-Saham-Predictor.git
cd Stock-Saham-Predictor
````

### 2. Buat Environment Baru

```bash
conda create -n stock-cnn-lstm python=3.10
conda activate stock-cnn-lstm
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Atau install manual (jika tidak punya `requirements.txt`):

```bash
pip install streamlit tensorflow-cpu pandas yfinance scikit-learn matplotlib
```

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## 📊 Contoh Output

* 📈 Grafik perbandingan harga aktual vs prediksi
* 📍 Prediksi harga untuk hari berikutnya (next-day price)
* 📉 Metrik evaluasi:

  * RMSE (Root Mean Squared Error)
  * MAE (Mean Absolute Error)

---

## 📁 Struktur Folder

```
.
├── app.py                  # Aplikasi utama Streamlit
├── data_loader.py         # Modul untuk download & preprocessing data
├── model_cnn_lstm.py      # Arsitektur model CNN + LSTM
├── visualizer.py          # Fungsi visualisasi hasil prediksi
├── utils.py               # Fungsi bantu: prediksi next-day, evaluasi model
├── requirements.txt       # Daftar dependensi Python
└── README.md              # Dokumentasi proyek
```

---

## ☁️ Deployment ke Streamlit Cloud

1. Push proyek ini ke GitHub
2. Masuk ke: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Login dengan GitHub
4. Klik **"New App"**, pilih repo ini dan file `app.py`
5. Klik **Deploy**

App kamu akan tampil di: `https://yourusername.streamlit.app`

---

## 🤝 Kontribusi

Pull request sangat diterima!
Fork repositori ini dan kirim PR untuk fitur baru, perbaikan bug, atau refactor arsitektur.

---



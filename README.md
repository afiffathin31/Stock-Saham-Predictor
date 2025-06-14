# 📈 Stock Price Predictor (CNN + LSTM)

Aplikasi prediksi harga saham berbasis kombinasi **CNN (Convolutional Neural Network)** dan **LSTM (Long Short-Term Memory)** untuk lima saham bank besar di Indonesia: **BCA (BBCA), BRI (BBRI), Mandiri (BMRI), BNI (BBNI), dan BSI (BRIS)**. Aplikasi ini dibangun menggunakan **Streamlit** untuk antarmuka interaktif dan **yFinance** sebagai sumber data historis.

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

Input (window size N)
↓
Conv1D → MaxPooling1D
↓
LSTM Layer
↓
Dropout → Dense Output


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
git clone https://github.com/yourusername/Stock-Saham-Predictor.git
cd Stock-Saham-Predictor

### 2. Buat Environment Baru
conda create -n stock-cnn-lstm python=3.10
conda activate stock-cnn-lstm

### 3. Install Dependencies

pip install -r requirements.txt

Atau manual:

pip install streamlit tensorflow-cpu pandas yfinance scikit-learn matplotlib

### 4. Jalankan Aplikasi

streamlit run app.py

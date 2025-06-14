import streamlit as st
from data_loader import download_stock_data, scale_data
from model_cnn_lstm import create_model
from visualizer import plot_predictions
from utils import predict_next_day, evaluate_model
import datetime

st.title("📊 Real-Time Saham Prediction (CNN + LSTM)")

tickers = {
    "BCA": "BBCA.JK",
    "BRI": "BBRI.JK",
    "Mandiri": "BMRI.JK",
    "BSI": "BRIS.JK",
    "BNI": "BBNI.JK"
}

selected = st.selectbox("Pilih Saham:", list(tickers.keys()))
start_date = st.date_input("Tanggal Mulai", datetime.date(2018, 1, 1))
end_date = st.date_input("Tanggal Akhir", datetime.date.today())
window = st.slider("Window Size", 30, 100, 60)

if st.button("Prediksi"):
    df = download_stock_data(tickers[selected], start_date, end_date)
    X, y, scaler = scale_data(df.values, window)

    model = create_model((X.shape[1], 1))
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)

    pred_scaled = model.predict(X)
    pred = scaler.inverse_transform(pred_scaled)
    y_actual = scaler.inverse_transform(y.reshape(-1, 1))

    st.pyplot(plot_predictions(y_actual, pred))

    # Evaluasi model
    rmse, mae = evaluate_model(y_actual, pred)
    st.write(f"📉 **RMSE**: {rmse:.2f} | **MAE**: {mae:.2f}")

    # Prediksi next day
    next_day = predict_next_day(model, X[-1], scaler)
    st.metric("📈 Prediksi Harga Besok", f"Rp {next_day:,.2f}")

import numpy as np

def predict_next_day(model, last_window, scaler):
    """
    Melakukan prediksi harga hari berikutnya berdasarkan window terakhir
    """
    input_data = last_window.reshape(1, last_window.shape[0], 1)
    predicted_scaled = model.predict(input_data)
    predicted = scaler.inverse_transform(predicted_scaled)
    return predicted[0][0]

def evaluate_model(y_true, y_pred):
    """
    Mengembalikan metrik evaluasi: RMSE dan MAE
    """
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    return rmse, mae

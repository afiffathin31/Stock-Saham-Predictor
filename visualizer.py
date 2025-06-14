import matplotlib.pyplot as plt

def plot_predictions(actual, predicted):
    fig, ax = plt.subplots()
    ax.plot(actual, label="Actual")
    ax.plot(predicted, label="Predicted")
    ax.set_title("Predicted vs Actual Prices")
    ax.legend()
    return fig

import matplotlib.pyplot as plt

def plot_results(X, y, y_pred, label):
    plt.scatter(X, y, color='grey', label='Real data')
    plt.plot(X, y_pred, label=label, linewidth=2)
    plt.title('Полиномиальная регрессия')
    plt.xlabel('Время')
    plt.ylabel('Количество сообщений')
    plt.legend()
    plt.show()
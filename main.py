from data_processing_module import load_and_process_data, filter_outliers
from regression_module import perform_polynomial_regression
from plotting_module import plot_results

file_path = 'C:/Users/Анастасия/time_messagees.txt'

# Загрузка и обработка данных
data = load_and_process_data(file_path)
filtered_data = filter_outliers(data)

# Подготовка данных для обучения
X = filtered_data['время'].values.reshape(-1, 1)
y = filtered_data['количество_сообщений'].values

# Полиномиальная регрессия
degree = 16  # Выберите желаемую степень полинома
y_pred, mse, r2 = perform_polynomial_regression(X, y, degree)

# Отрисовка результатов
plot_results(X, y, y_pred, f'Degree {degree}')

# Вывод MSE и R2
print('Mean squared error: %.2f' % mse)
print('Coefficient of determination (R2): %.2f' % r2)
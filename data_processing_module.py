import pandas as pd

def load_and_process_data(file_path):
    data = pd.read_csv(file_path, delimiter=',', names=['время', 'количество_сообщений'])
    data['время'] = pd.to_datetime(data['время'], format='%H:%M:%S').dt.hour
    return data

def filter_outliers(data, lower_quantile=0.05, upper_quantile=0.95):
    lower_bound = data['количество_сообщений'].quantile(lower_quantile)
    upper_bound = data['количество_сообщений'].quantile(upper_quantile)
    return data[(data['количество_сообщений'] >= lower_bound) & (data['количество_сообщений'] <= upper_bound)]
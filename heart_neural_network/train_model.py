import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def train():
    """
    Функция для обучения модели предсказания сердечных заболеваний
    """
    # Определение пути к данным относительно текущего файла
    DATA_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(DATA_DIR, 'heart.csv')
    
    # Загрузка данных
    print(f"Загрузка данных из {DATA_PATH}")
    data = pd.read_csv(DATA_PATH)
    
    # Разделение на признаки и целевую переменную
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Разделение на тренировочную и тестовую выборки (80% для тренировки, 20% для теста)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Инициализация и обучение модели
    print("Обучение модели RandomForest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Предсказания на тестовых данных
    y_pred = model.predict(X_test)
    
    # Оценка точности
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Точность модели: {accuracy * 100:.2f}%')
    
    # Сохранение модели в файл
    model_filename = os.path.join(DATA_DIR, 'heart_disease_model.joblib')
    joblib.dump(model, model_filename)
    print(f'Модель сохранена в {model_filename}')
    
    return model, accuracy

if __name__ == "__main__":
    train()
 
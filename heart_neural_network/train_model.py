import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Загрузка данных
data = pd.read_csv('heart.csv')

# Разделение на признаки и целевую переменную
X = data.drop('target', axis=1)
y = data['target']

# Разделение на тренировочную и тестовую выборки (80% для тренировки, 20% для теста)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация и обучение модели
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Предсказания на тестовых данных
y_pred = model.predict(X_test)

# Оценка точности
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Сохранение модели в файл
model_filename = 'heart_disease_model.joblib'
joblib.dump(model, model_filename)
print(f'Model saved to {model_filename}')

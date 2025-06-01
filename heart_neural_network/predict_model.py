import joblib
import numpy as np
import os
import argparse
import sys

# Определение пути к модели относительно текущего файла
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, 'heart_disease_model.joblib')

# Загрузка модели из файла
model = joblib.load(MODEL_PATH)

def predict(data):
    """
    Функция для предсказания на основе предоставленных данных
    
    Args:
        data: список параметров или numpy массив
        
    Returns:
        tuple: (вероятность отсутствия риска, вероятность наличия риска)
    """
    # Преобразуем данные в формат, который ожидает модель (нужно передать как двумерный массив)
    input_data = np.array(data).reshape(1, -1)
    
    # Предсказание (вероятность)
    prediction_proba = model.predict_proba(input_data)
    
    # Вероятность риска сердечного приступа (результат = 1)
    risk_probability = prediction_proba[0][model.classes_.tolist().index(1)]
    
    # Разворот вероятности (отсутствие риска)
    reversed_probability = 1 - risk_probability
    
    return reversed_probability, risk_probability

# Функция для ввода данных с клавиатуры
def input_data():
    print("Введите данные для предсказания риска сердечного приступа:")
    
    age = int(input("Возраст (в годах): "))
    sex = int(input("Пол: 1 - мужской, 0 - женский: "))
    cp = int(input("Тип боли в груди: 1 — Типичная стенокардия, 2 — Атипичная стенокардия, 3 — Боль не связана со стенокардией, 4 — Бессимптомно: "))
    trtbps = int(input("Артериальное давление в состоянии покоя(мм рт.ст.): "))
    chol = int(input("Уровень холестерина (мг/дл): "))
    fbs = int(input("Уровень сахара в крови: 1 - выше 120 мг/дл, 0 - ниже: "))
    restecg = int(input("Результаты электрокардиограммы: 0 — Норма, 1 — Аномалия волны ST-T (инверсия волны T и/или подъем/депрессия ST более 0,05 мВ), 2 — Признаки гипертрофии левого желудочка (по критериям Эстеса): "))
    thalachh = int(input("Максимальная частота сердечных сокращений (уд/мин): "))
    exng = int(input("Наличие физической нагрузки: 1 - да, 0 - нет: "))
    oldpeak = float(input("Депрессия ST (в мВ): "))
    slp = int(input("Наклон сегмента ST: 1 — Горизонтальный, 2 — Восходящий, 3 — Нисходящий: "))
    caa = int(input("Количество крупных сосудистых заболеваний: 0 — Ни один крупный сосуд не окрашен (норма), 1 — Окрашен один крупный сосуд, 2 — Окрашены два крупных сосуда, 3 — Окрашены три крупных сосуда: "))
    thall = int(input("Уровень талассемии (thall): 1 - нормальный, 2 - фиксированный дефект, 3 - обратимый дефект: "))
    
    return [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]

def cli_predict():
    """Точка входа для работы из командной строки"""
    parser = argparse.ArgumentParser(description='Предсказание риска сердечных заболеваний')
    parser.add_argument('--file', help='Путь к файлу CSV с данными для предсказания')
    args = parser.parse_args()
    
    if args.file:
        # Если указан файл, обрабатываем его
        import pandas as pd
        try:
            df = pd.read_csv(args.file)
            results = []
            for _, row in df.iterrows():
                data = row.values
                no_risk, risk = predict(data)
                results.append((no_risk, risk))
            
            # Вывод результатов
            print("Результаты предсказания:")
            for i, (no_risk, risk) in enumerate(results):
                print(f"Запись {i+1}: Вероятность отсутствия риска: {no_risk*100:.2f}%, "
                      f"Вероятность наличия риска: {risk*100:.2f}%")
                
        except Exception as e:
            print(f"Ошибка при обработке файла: {e}")
            sys.exit(1)
    else:
        # Если файл не указан, запрашиваем данные у пользователя
        user_data = input_data()
        no_risk, risk = predict(user_data)
        
        print(f"Вероятность отсутствия сердечного заболевания: {no_risk*100:.2f}%")
        print(f"Вероятность наличия сердечного заболевания: {risk*100:.2f}%")

if __name__ == "__main__":
    # Получение данных от пользователя
    user_data = input_data()
    
    # Выполняем предсказание
    no_risk, risk = predict(user_data)
    
    print(f"Вероятность отсутствия сердечного приступа: {no_risk * 100:.2f}%")
    print(f"Вероятность наличия сердечного приступа: {risk * 100:.2f}%")

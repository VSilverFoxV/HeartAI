from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import os

# Пути к модели
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "heart_neural_network", "heart_disease_model.joblib")

# Загрузка модели
model = joblib.load(MODEL_PATH)

# Инициализация Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

# Главная страница с формой
@app.route("/")
def home():
    return render_template("index.html")

# Обработка предсказания
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Получение данных из формы
        data = request.form

        # Извлечение признаков из данных формы
        features = [
            float(data["age"]),
            int(data["sex"]),
            int(data["cp"]),
            float(data["trtbps"]),
            float(data["chol"]),
            int(data["fbs"]),
            int(data["restecg"]),
            float(data["thalachh"]),
            int(data["exng"]),
            float(data["oldpeak"]),
            int(data["slp"]),
            int(data["caa"]),
            int(data["thall"]),
        ]

        # Преобразование данных в формат для модели
        input_data = np.array(features).reshape(1, -1)

        # Выполнение предсказания вероятности
        prediction_proba = model.predict_proba(input_data)
        risk_probability = float(prediction_proba[0][1])  # Вероятность заболевания

        # Вероятность отсутствия заболевания
        no_risk_probability = 1 - risk_probability

        # Возврат только вероятности отсутствия заболевания (в процентах)
        return jsonify({"risk": round(no_risk_probability, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

def run_app():
    """Функция для запуска приложения через точку входа"""
    app.run(debug=False, host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True)
    

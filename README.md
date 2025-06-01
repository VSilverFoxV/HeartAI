# Прогноз риска сердечного приступа

Проект содержит нейронную сеть для прогноза риска сердечного приступа на основе медицинских данных пациентов.

## Структура проекта

- `heart_neural_network/` - основной модуль для обучения и прогноза
  - `train_model.py` - скрипт для обучения модели
  - `predict_model.py` - скрипт для предсказания
  - `heart_disease_model.joblib` - обученная модель
  - `heart.csv` - набор данных для обучения

- `website/` - веб-интерфейс для работы с моделью
  - `app.py` - Flask-приложение
  - `templates/` - HTML-шаблоны
  - `static/` - статические файлы (CSS, JS)

- `docs/` - документация проекта
  - `source/` - исходные файлы документации
  - `build/` - сгенерированная документация

## Зависимости

Для работы проекта на Python 3.8+ требуются следующие библиотеки:

- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- Flask
- Joblib
- Matplotlib
- Seaborn
- setuptools (для установки через pip)

Для установки всех зависимостей выполните:

```bash
pip install -r requirements.txt
```

## Установка

Для установки пакета выполните:

```bash
pip install -e .
```

## Использование

### Обучение модели
```python
from heart_neural_network.train_model import train
train()
```

### Предсказание
```python
from heart_neural_network.predict_model import predict
result = predict(data)
```

### Запуск веб-интерфейса
```bash
python -m website.app
```

## Документация

Для сборки документации вам потребуются дополнительные зависимости:

```bash
pip install -e ".[docs]"
```

Сборка HTML-документации:

```bash
python -m sphinx.cmd.build -b html docs/source docs/build/html
```

После сборки документация будет доступна в директории `docs/build/html`. 
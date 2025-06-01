Использование
============

Обучение модели
--------------

Для обучения модели вы можете использовать следующий код:

.. code-block:: python

   from heart_neural_network.train_model import train
   train()

Или через командную строку:

.. code-block:: bash

   heart-train

Предсказание
-----------

Для предсказания риска сердечного приступа на основе данных пациента:

.. code-block:: python

   from heart_neural_network.predict_model import predict
   
   # Пример данных пациента
   patient_data = {
       'age': 52,
       'sex': 1,
       'cp': 0,
       'trestbps': 125,
       'chol': 212,
       'fbs': 0,
       'restecg': 1,
       'thalach': 168,
       'exang': 0,
       'oldpeak': 1.0,
       'slope': 2,
       'ca': 2,
       'thal': 3
   }
   
   result = predict(patient_data)
   print(f"Вероятность сердечного приступа: {result:.2f}")

Или через командную строку:

.. code-block:: bash

   heart-predict --age 52 --sex 1 --cp 0 --trestbps 125 --chol 212 --fbs 0 --restecg 1 --thalach 168 --exang 0 --oldpeak 1.0 --slope 2 --ca 2 --thal 3

Запуск веб-интерфейса
--------------------

Для запуска веб-интерфейса выполните:

.. code-block:: bash

   heart-web

или

.. code-block:: bash

   python -m website.app

После этого веб-интерфейс будет доступен по адресу http://localhost:5000. 
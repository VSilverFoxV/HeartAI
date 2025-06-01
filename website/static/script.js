// Получаем форму и элемент для отображения результата
const form = document.getElementById("prediction-form");
const resultDiv = document.getElementById("result");

// Обработчик отправки формы
form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Отключаем стандартное поведение формы

    // Собираем данные формы
    const formData = new FormData(form);

    // Отправляем POST-запрос на API
    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData, // Отправляем форму как обычные данные
        });

        if (!response.ok) {
            throw new Error(`Ошибка: ${response.statusText}`);
        }

        const result = await response.json();
        if (result.error) {
            throw new Error(result.error);
        }

        // Отображаем результат
        resultDiv.innerHTML = `<p>Вероятность сердечного приступа: <strong>${(result.risk * 100).toFixed(2)}%</strong></p>`;
    } catch (error) {
        // Показываем сообщение об ошибке
        resultDiv.innerHTML = `<p class="error">Произошла ошибка: ${error.message}</p>`;
    }
});


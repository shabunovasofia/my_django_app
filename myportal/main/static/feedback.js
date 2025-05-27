document.getElementById("feedbackForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch("/send-feedback/", {
            method: "POST",
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'  // Для идентификации AJAX запроса
            }
        });

        const result = await response.json();

        document.getElementById("responseMessage").textContent = result.message;

        if (result.status === 'success') {
            this.reset();  // Очистить форму после успешной отправки
        }
    } catch (error) {
        console.error("Ошибка:", error);
        document.getElementById("responseMessage").textContent = "Ошибка при отправке сообщения!";
    }
});
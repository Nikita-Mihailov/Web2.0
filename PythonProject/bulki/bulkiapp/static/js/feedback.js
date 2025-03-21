const submitButton = document.getElementById('submit-button');
if (submitButton) {
    submitButton.addEventListener('mouseenter', () => {
        submitButton.style.color = 'white'; // Цвет текста при наведении
        submitButton.style.backgroundColor = '#cc9600'; // Цвет фона при наведении
    });
    submitButton.addEventListener('mouseleave', () => {
        submitButton.style.color = 'black'; // Восстановление цвета текста
        submitButton.style.backgroundColor = 'white'; // Восстановление цвета фона
    });
}

const inputFields = document.querySelectorAll('.input-field');
inputFields.forEach(field => {
    field.addEventListener('focus', () => {
        field.style.backgroundColor = 'lightyellow'; // Цвет фона при фокусе
    });
    field.addEventListener('blur', () => {
        field.style.backgroundColor = 'white'; // Восстановление цвета фона
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const registerButton = document.getElementById('registerButton');
    const loginButton = document.getElementById('loginButton');
    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');
    const formTitle = document.getElementById('formTitle');

    if (!registerButton || !loginButton || !registerForm || !loginForm || !formTitle) {
        console.error('Не все элементы формы найдены на странице!');
        return;
    }

    registerButton.addEventListener('click', function () {
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
        registerButton.classList.add('active');
        loginButton.classList.remove('active');
        formTitle.textContent = 'Регистрация';
    });

    loginButton.addEventListener('click', function () {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
        loginButton.classList.add('active');
        registerButton.classList.remove('active');
        formTitle.textContent = 'Вход';
    });
});

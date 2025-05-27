document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('authForm');
    const usernameInput = document.getElementById('username');
    const lastNameInput = document.getElementById('lastName');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const phoneInput = document.getElementById('phone');
    const confirmPasswordInput = document.getElementById('confirm-password');
    const phoneSignInput = document.getElementById('phoneSign');

    const usernameError = document.getElementById('usernameError');
    const lastNameError = document.getElementById('lastNameError');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    const phoneError = document.getElementById('phoneError');

    const confirmPasswordError = document.getElementById('confirmPasswordError');

    function validateName(name) {
        const regex = /^[A-ZА-Я][a-zа-я]*$/;
        return regex.test(name);
    }

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    function validatePassword(password) {
        return password.length >= 6;
    }

    function validatePhone(phone) {
        const regex = /^\+?[0-9]{10,15}$/;
        return regex.test(phone);
    }

    function validateConfirmPassword(password, confirmPassword) {
        return password === confirmPassword;
    }

    function updateValidation(input, isValid, errorElement) {
        if (isValid) {
            input.classList.remove('invalid');
            errorElement.style.display = 'none';
        } else {
            input.classList.add('invalid');
            errorElement.style.display = 'block';
        }
    }

    usernameInput.addEventListener('input', function () {
        updateValidation(usernameInput, validateName(usernameInput.value), usernameError);
    });

    lastNameInput.addEventListener('input', function () {
        updateValidation(lastNameInput, validateName(lastNameInput.value), lastNameError);
    });

    emailInput.addEventListener('input', function () {
        updateValidation(emailInput, !emailInput.value || validateEmail(emailInput.value), emailError);
    });

    phoneInput.addEventListener('input', function () {
        updateValidation(phoneInput, validatePhone(phoneInput.value), phoneError);
    });

    passwordInput.addEventListener('input', function () {
        updateValidation(passwordInput, validatePassword(passwordInput.value), passwordError);
    });

    confirmPasswordInput.addEventListener('input', function () {
        updateValidation(confirmPasswordInput, validateConfirmPassword(passwordInput.value, confirmPasswordInput.value), confirmPasswordError);
    });

    form.addEventListener('submit', function (event) {
        let isValid = true;

        if (!validateName(usernameInput.value)) {
            updateValidation(usernameInput, false, usernameError);
            isValid = false;
        }

        if (!validateName(lastNameInput.value)) {
            updateValidation(lastNameInput, false, lastNameError);
            isValid = false;
        }

        if (emailInput.value && !validateEmail(emailInput.value)) {
            updateValidation(emailInput, false, emailError);
            isValid = false;
        }

        if (!validatePhone(phoneInput.value)) {
            updateValidation(phoneInput, false, phoneError);
            isValid = false;
        }

        if (!validatePassword(passwordInput.value)) {
            updateValidation(passwordInput, false, passwordError);
            isValid = false;
        }

        if (!validateConfirmPassword(passwordInput.value, confirmPasswordInput.value)) {
            updateValidation(confirmPasswordInput, false, confirmPasswordError);
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});

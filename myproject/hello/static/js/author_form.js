document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('beautiful-form');
    const formGroups = document.querySelectorAll('.form-group');

    // Add animation to form elements
    formGroups.forEach((group, index) => {
        group.style.opacity = '0';
        group.style.transform = 'translateY(20px)';
        setTimeout(() => {
            group.style.transition = 'opacity 0.5s, transform 0.5s';
            group.style.opacity = '1';
            group.style.transform = 'translateY(0)';
        }, 100 * index);
    });

    // Add custom validation and error messages
    form.addEventListener('submit', (e) => {
        let isValid = true;
        formGroups.forEach((group) => {
            const input = group.querySelector('input, textarea, select');
            let errorMessage = group.querySelector('.error-message');
            
            if (input.value.trim() === '') {
                isValid = false;
                group.classList.add('has-error');
                if (!errorMessage) {
                    errorMessage = document.createElement('span');
                    errorMessage.className = 'error-message';
                    group.appendChild(errorMessage);
                }
                errorMessage.textContent = 'This field is required';
            } else {
                group.classList.remove('has-error');
                if (errorMessage) {
                    errorMessage.textContent = '';
                }
            }
        });

        if (!isValid) {
            e.preventDefault();
        }
    });

    // Clear error messages on input
    formGroups.forEach((group) => {
        const input = group.querySelector('input, textarea, select');
        input.addEventListener('input', () => {
            group.classList.remove('has-error');
            const errorMessage = group.querySelector('.error-message');
            if (errorMessage) {
                errorMessage.textContent = '';
            }
        });
    });
});

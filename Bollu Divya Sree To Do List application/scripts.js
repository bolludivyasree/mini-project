document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const errorMessage = document.getElementById('error-message');

    // Simple validation (For demonstration purposes)
    if (username === 'user' && password === 'password123') {
        alert('Login successful!');
        // Redirect to a new page or proceed with logged-in actions
    } else {
        errorMessage.textContent = 'Invalid username or password!';
    }
});

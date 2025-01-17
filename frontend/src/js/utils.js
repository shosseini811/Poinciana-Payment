// Utility functions
function checkAuth() {
    const token = localStorage.getItem('token');
    if (token) {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('paymentForm').style.display = 'block';
    }
}

// Check authentication status when page loads
document.addEventListener('DOMContentLoaded', checkAuth); 
// Get API URL from window object
const API_URL = window.API_URL;

if (!API_URL) {
    console.error('API URL not found! Make sure it is set in the HTML.');
}

// Handle payment form submission
document.getElementById('payment-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const amount = document.getElementById('amount').value;
    const paymentMethod = document.getElementById('payment-method').value;
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Please login first');
        return;
    }

    try {
        // Submit payment details to backend
        const paymentResponse = await fetch(`${API_URL}/submit-payment`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                amount: amount,
                payment_method: paymentMethod,
                rent_for_month: new Date().toISOString().split('T')[0]
            })
        });

        // With no-cors mode, we can't read the response
        if (paymentResponse.type === 'opaque') {
            alert('Payment submitted successfully!');
            // Reset form
            document.getElementById('payment-form').reset();
        }
    } catch (error) {
        console.error('Payment error:', error);
        alert('Error submitting payment. Please try again.');
    }
}); 
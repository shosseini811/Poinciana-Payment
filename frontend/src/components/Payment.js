import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import axios from 'axios';

const stripePromise = loadStripe('your_publishable_key');

const Payment = () => {
    const [amount, setAmount] = useState('');

    const handlePayment = async (e) => {
        e.preventDefault();
        
        const stripe = await stripePromise;
        
        // Create payment intent
        const response = await axios.post('/api/create-payment-intent', {
            amount: amount * 100 // Convert to cents
        });
        
        // Confirm payment
        const result = await stripe.confirmCardPayment(response.data.clientSecret, {
            payment_method: {
                card: elements.getElement('card'),
                billing_details: {
                    name: 'User Name',
                },
            }
        });
        
        if (result.error) {
            console.error(result.error);
        } else {
            // Payment successful
            await axios.post('/api/submit-payment', {
                amount: amount,
                stripe_payment_id: result.paymentIntent.id,
                rent_for_month: new Date().toISOString().split('T')[0]
            });
        }
    };

    return (
        <form onSubmit={handlePayment}>
            <input
                type="number"
                placeholder="Amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />
            <button type="submit">Pay Rent</button>
        </form>
    );
};

export default Payment; 
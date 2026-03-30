document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = submitBtn.querySelector('.loader');
    
    const resultContainer = document.getElementById('result-container');
    const churnProb = document.getElementById('churn-probability');
    const churnStatus = document.getElementById('churn-status');
    const resetBtn = document.getElementById('reset-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 1. Get input values for all 10 features
        const payload = {
            credit_score: parseInt(document.getElementById('credit-score').value),
            geography: document.getElementById('geography').value,
            gender: document.getElementById('gender').value,
            age: parseInt(document.getElementById('age').value),
            tenure: parseInt(document.getElementById('tenure').value),
            balance: parseFloat(document.getElementById('balance').value),
            num_products: parseInt(document.getElementById('num-products').value),
            has_crcard: document.getElementById('has-crcard').checked ? 1 : 0,
            is_active_member: document.getElementById('is-active').checked ? 1 : 0,
            estimated_salary: parseFloat(document.getElementById('estimated-salary').value)
        };

        // 2. UI Loading State
        setLoadingState(true);

        // 3. Make the API Prediction Request
        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || `Server returned ${response.status}`);
            }

            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }

            const probability = data.churn_probability;

            // 4. Update UI with Results
            displayResults(probability);
            
        } catch (error) {
            console.error('Error during prediction:', error);
            alert(`Prediction Failed: ${error.message}`);
        } finally {
            setLoadingState(false);
        }
    });

    resetBtn.addEventListener('click', () => {
        // Hide results
        resultContainer.classList.remove('show');
        setTimeout(() => {
            resultContainer.classList.add('hidden');
            // Show form
            form.style.display = 'block';
            setTimeout(() => {
                form.style.opacity = '1';
                form.style.transform = 'scale(1)';
            }, 50);
            form.reset();
        }, 500); // Wait for transition
    });

    function setLoadingState(isLoading) {
        if (isLoading) {
            submitBtn.disabled = true;
            btnText.classList.add('hidden');
            loader.classList.remove('hidden');
        } else {
            submitBtn.disabled = false;
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    }

    function displayResults(probability) {
        // Hide form with animation
        form.style.transition = 'all 0.5s ease';
        form.style.opacity = '0';
        form.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
            form.style.display = 'none';
            
            // Format probability string (convert 0-1 scale to percentage)
            const probPercent = (probability * 100).toFixed(1);
            churnProb.textContent = `${probPercent}%`;
            
            // Determine risk class
            churnStatus.className = 'status-badge'; // reset
            if (probability >= 0.7) {
                churnStatus.textContent = 'High Churn Risk';
                churnStatus.classList.add('high-risk');
            } else if (probability >= 0.4) {
                churnStatus.textContent = 'Medium Churn Risk';
                churnStatus.classList.add('medium-risk');
            } else {
                churnStatus.textContent = 'Low Churn Risk';
                churnStatus.classList.add('low-risk');
            }

            // Show results
            resultContainer.classList.remove('hidden');
            // Slight delay to allow display:block to apply before animating opacity
            requestAnimationFrame(() => {
                resultContainer.classList.add('show');
            });
            
        }, 500);
    }
});

Methodology
The NO₂ data is extracted from the dataset and preprocessed by removing missing values. A roll-number–based sinusoidal transformation is applied to generate a new variable. The empirical distribution of the transformed data is obtained using a normalized histogram. A Gaussian-like probability density function is assumed and its parameters are estimated using curve fitting. The fitted PDF is then visualized along with the histogram to evaluate the model fit.


Table
| Parameter  | Description                             | Estimated Value            |
| ---------- | --------------------------------------- | -------------------------- |
| λ (Lambda) | Controls the spread of the distribution | Obtained via curve fitting |
| μ (Mu)     | Mean of the transformed data            | Obtained via curve fitting |
| c          | Scaling constant of the PDF             | Obtained via curve fitting |


Result Graph

<img width="584" height="455" alt="image" src="https://github.com/user-attachments/assets/336914a1-e88d-47b7-85b4-42537d8d6df9" />

<img width="584" height="455" alt="image" src="https://github.com/user-attachments/assets/d2420253-6f08-4c9e-ae49-e55e21f06b18" />

<img width="584" height="432" alt="image" src="https://github.com/user-attachments/assets/ec6cf989-be90-4756-954b-79a71167cf01" />


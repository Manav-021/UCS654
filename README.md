Sampling Techniques on imbalanced Credit Card Dataset:

1.DATASET:
Creditcard_data.csv is the name of the file that will be used in this project; it has numerical feature data from transactions and contains a target variable (Class) as a binary output. The target variable will indicate whether or not the transaction was a legitimate transaction (0) or a fraudulent transaction (1). The challenge with this dataset is that there is an imbalance between the two classes of the target variable because very few transactions are classified as fraudulent transactions.

DATASET LINK:
[Creditcard_data.csv](https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv)


2.Methodology:
After loading the dataset, it was preprocessed by dividing the target variable and features. Standardization was used to scale features. Five distinct sampling techniques—Random Under Sampling, Random Over Sampling, SMOTE, SMOTEENN, and Partial Over Sampling—were employed to address class imbalance. The datasets were balanced using these sampling techniques. An 80:20 split was then used to separate the sampled datasets into training and testing datasets. The datasets were used to train five machine learning models, and their performance was evaluated using accuracy.

3.Results:
The results are shown in a comparison table with columns for sampling techniques and rows for machine learning models. Each value in the table represents the accuracy attained by a specific model–sampling combination. In addition to the table, bar graphs, line graphs, and heatmaps were made to visually compare model performance and identify the top-performing combinations.

<img width="1005" height="547" alt="image" src="https://github.com/user-attachments/assets/ea66726a-49d8-4386-b380-3ea4be2b781d" />:


4.Discussion:
Analysis of the data shows that sampling strategies have a major impact on model accuracy. Since they increased the number of instances in the minority class without sacrificing important information, oversampling and SMOTE techniques were generally superior to undersampling techniques. The different sampling strategies had varying effects on the performance of different models, suggesting that there isn't a single optimal sampling strategy for every model.


5.Tools and Libraries:
This project was implemented in Google Colab using Python. Data processing was done using NumPy and Pandas. Class imbalance was addressed using Imbalanced-learn, while machine learning models and assessment metrics were implemented using Scikit-learn. Matplotlib and Seaborn were used to visualize the results.

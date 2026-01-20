<img width="1005" height="547" alt="image" src="https://github.com/user-attachments/assets/ea66726a-49d8-4386-b380-3ea4be2b781d" />Sampling Techniques on imbalanced credit card dataset:

1.DATASET:
The CSV file to be used in the project is Creditcard_data.csv, with numerical features pertaining to transactions in the file, along with a target variable that is a binary output denoted as Class. The target output explains if a transaction is a normal transaction (0) or a fraudulent transaction (1) based on its output in the target variable Class. The problem is a class imbalance problem because it is observed that very few transactions occur that can be considered as fraudulent transactions.

DATASET LINK:
[Creditcard_data.csv](https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv)


2.Methodology
The dataset was first loaded and preprocessed by splitting the features and target variable. Feature scaling was done using standardization. To handle class imbalance, five different sampling methods were used: Random Under Sampling, Random Over Sampling, SMOTE, SMOTEENN, and Partial Over Sampling. These sampling methods were used to balance the datasets. The sampled datasets were then split into training and testing datasets using an 80:20 split. Five machine learning models were trained on the datasets, and accuracy was used to measure their performance.

3.Results
A comparison table with rows for machine learning models and columns for sampling methods displays the findings. The accuracy attained by a particular model–sampling combination is represented by each value in the table. To visually compare model performance and determine the best-performing combinations, bar graphs, line graphs, and heatmaps were created in addition to the table.





4.Discussion
Analysis of the results indicates that the accuracy of models is significantly affected by sampling techniques. Oversampling and SMOTE techniques were generally better than undersampling techniques since they increased the number of instances in the minority class without sacrificing valuable information. The performance of different models was affected differently by the various sampling techniques, which indicates that there is no best sampling technique for all models.


5.Tools and Libraries
Python was used in Google Colab to implement this project. Pandas and NumPy were used for data processing. Scikit-learn was used to implement machine learning models and evaluation metrics, and Imbalanced-learn was used to address class imbalance. The results were visualized using Matplotlib and Seaborn.

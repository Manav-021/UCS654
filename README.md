Sampling Techniques on imbalanced credit card dataset:

1.DATASET:
The CSV file to be used in the project is Creditcard_data.csv, with numerical features pertaining to transactions in the file, along with a target variable that is a binary output denoted as Class. The target output explains if a transaction is a normal transaction (0) or a fraudulent transaction (1) based on its output in the target variable Class. The problem is a class imbalance problem because it is observed that very few transactions occur that can be considered as fraudulent transactions.

DATASET LINK:
[Creditcard_data.csv](https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv)


2.Methodology
The dataset was first loaded and preprocessed by separating features and the target variable. Feature scaling was applied using standardization to normalize the data. To address class imbalance, five sampling techniques—Random Under Sampling, Random Over Sampling, SMOTE, SMOTEENN, and Partial Over Sampling—were applied to create balanced datasets. Each sampled dataset was split into training and testing sets using an 80:20 ratio. Five machine learning models were then trained on each dataset, and accuracy was used to evaluate their performance.

3.Results
The results are presented in a comparison table where rows represent machine learning models and columns represent sampling techniques. Each value in the table corresponds to the accuracy achieved by a specific model–sampling combination. In addition to the table, bar graphs, line graphs, and heatmaps were generated to visually compare model performance and identify the best-performing combinations.


4.Discussion
The results show that sampling techniques have a significant impact on model accuracy. Oversampling and SMOTE-based methods generally performed better than undersampling, as they improved minority class representation without losing important information. Different models responded differently to sampling techniques, indicating that no single sampling method is optimal for all models. This highlights the importance of choosing sampling strategies based on the model and dataset characteristics.


5.Tools and Libraries
This project was implemented using Python in Google Colab. Data processing was performed using Pandas and NumPy. Machine learning models and evaluation metrics were implemented using Scikit-learn, while class imbalance was handled using Imbalanced-learn. Matplotlib and Seaborn were used for result visualization.

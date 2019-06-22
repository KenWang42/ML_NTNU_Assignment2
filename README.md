# ML_NTNU_Assignment2

## Enviroment

OS: Win10

IDE: vscode, jupyter lab 4.4.0

Python Edition: 3.7

## Folder Content:

### data:

This folder contains dataset for various useage.

Feature_Selection_Result.csv: the output of SVM feature selection

UCI_Credit_Card.csv: Original data from assignment site

UCI_Credit_Card_NC.csv: Original data without contineus data

UCI_Credit_Card_New.csv: Dataset for feature selection practice

UCI_Credit_Card_OHE.csv: Dataset after One Hot Encode

UCI_Credit_Card_Rename.csv: Rename two columns from raw data (PAY_0 and default.payment.next.month)

### jupyter notebook

This folder contains practice and draft for formal source code

Data Cleaning: Trial on turning some ambiguios value in the dataset into more reasonable value by the guildline of description

I renamed the data columns in this notebook.

Also, I did some research on each feature and turn continuous data into logarithm.

However, with the UCI_Credit_Card_New.csv not both K-Means and SVM showed worse result.

Therefroe, I did not use this dataset in the final source code.

KMeans_Draft.ipynbb: The draft of KMeans

From this draft I learned that KMeans performance better without continuous data and created dataset UCI_Credit_Card_NC.csv for formal source code.

Preprocessing_SVM: implemented One Hot Encode to categorical data and Standar scaler transfrom to continous data and saved the dataset as UCI_Crdit_Card_OHE.csv for SVM.

SVM_Draft.ipynb: The draft of SVM, heavly reference from [thie link](https://www.kaggle.com/kaankarakeben/uci-credit-card-svm-classifier-acc-0-82)



### Source

KMeans.ipynb: It shows the probability of label 1 for each clusters and shows the overal accuracy for the algorithm. 

SVM_Classification.py: It will show accuracy for each time of 10-fold validation and the mean of them.

The SVM uses UCI_Credit_Card_OHE.csv.

SVM_Feature_Selection.ipynb: dropping out features by greedy approach to improve the performance of SVM


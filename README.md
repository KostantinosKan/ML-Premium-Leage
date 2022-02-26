# Premium Leage Matches Predictions - Machine Learning

In this project I will apply machine learning in order to predict the outcome of Premium Leage soccer matches. The purpose is to achieve better accuracy than bookmaker's. For this, I will convert bookmaker's odds to real (not implied) probabilities and compare them with my model's predictions. To this end, I will exclude bookmaker's odd features (h_odd, a_odd, d_odd) from the dataset, and I will build my model with the rest of the features.

## Code and Resources Used
**Python version:** 3.8.10<br/>
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Seaborn, MRMR.<br/>
**Data:** More than 6000 matches scraped from  https://www.oddsportal.com/ by Caldass: https://github.com/Caldass/pl-matches-predictor.

## Getting Results in 4 Steps

### Step 1 - Data Cleaning
* Deal with missing values.
* Drop irrelevant features.
* Drop features with high cardinality.
* Drop features that are unknown before a match.

### Step 2 - Feature Engineering
* Convert bookmaker's odds to implied probabilities.
* Convert implied odds to real (fair) probabilities.

### Step 3 - Exploratory Data Analysis
* Check which outcome is more possible to occur.
* Check correlations between predictors and target feature.

### Step 4 - Machine Learning
#### Data Preprocessing
* Convert categorical classes of target feature to integers.
* Convert categorical features to dummies.
* Split the dataset into training and test set.
* Perform feature selection and select the best 20 features using the MRMR technique.
#### Select Best Scaler
I tested three scalers: MinMaxScaler, StandardScaler, and RobustScaler.<br/>
![alt text](https://github.com/KostantinosKan/ML-Premium-Leage/blob/main/data/pictures/best_scaler.JPG?raw=true)

#### Select Best Model
I tested five model algorithms: LogisticRegression, RandomForestClassifier, LGBMClassifier, XGBClassifier, KNeighborsClassifier.
![alt text](https://github.com/KostantinosKan/ML-Premium-Leage/blob/main/data/pictures/best_model.JPG?raw=true)

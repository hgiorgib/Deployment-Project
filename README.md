# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals

The project objective is to automate the loan eligibility process based on customer data provided as online application forms. The data set contains socio-economic information of the applicants. As goal of the project it is needed to create a ML model to predict the approval of loan applications.

## Hypothesis

Which applicants are more likely to get a loan

1. Applicants with less or no dependents
2. Loans with longer term
3. Applicants with coapplicants
4. Loans with smaller amount

![Quantity of Loans by category](Images/QofLoans.PNG) 

## Process

#### Step 1: Data cleaning

* Null values were detected and were filled with mean and mode values according to each particular case analysis.


#### Step 2: EDA

* Presence of outliers was analyzed.

* The existence of extreme values in LoanAmount was manage by using the Log transformation, and additionally, it was possible to adjust the destribution from right skewed to a closer version of normal distribution.

![Histograms of LoanAmount distribution](Images/HLoanAmount.PNG) 


#### Step 3: Feature engineering

* Feature total_income was created and then, it was applied the log transformation to obtain a distribution close to gaussian.

* Categorical variables were transformated into dummies variables


#### Step 4: Modeling

* It was used the Random Forest Classifier model. It was applied the StandardScaler and data was split 80% for training and 20% for testing.

* The best score of 0.777 is obtained by configuring the params as follows: max_depth: 5, min_samples_leaf: 1, min_samples_split: 10, n_estimators: 10


#### Step 5: Deployment

* Pipeline was used with Random Forest Classifer as model and PCA and SelectKBest as feature union.


## Results/Demo

![Results](Images/Results.PNG) 

## Challanges 

* Complications deploying API


## Future goals

* Implementing more ML models

* Deeper analysis of hypothesis
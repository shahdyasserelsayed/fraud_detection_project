# Fraud Detection on Financial Data

## Project Description
This project builds a machine learning model to detect fraudulent credit card transactions. It handles highly imbalanced data, trains an XGBoost classifier, and outputs predictions that can be analyzed in Power BI or similar tools.

## Dataset
The project uses the Credit Card Fraud Detection dataset from Kaggle:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains 284,807 transactions with only 492 fraud cases, making it highly imbalanced.

## Features
- Numerical features from anonymized transaction data.  
- 'Time' feature converted into hourly segments for analysis.  
- Data scaling using StandardScaler.  
- Synthetic oversampling using SMOTE to handle class imbalance.

## How to Run
1. Clone this repository.  
2. Place `creditcard.csv` in the `data` folder.  
3. Run the Jupyter notebook to train and generate predictions:  
4. (Optional) Use `fraud_predictions.csv` in Power BI for visualization.
5. 
## Folder Structure
- `data` - contains original and prediction CSV files  
- `notebook` - Jupyter notebook with data processing and modeling  
- `model` - saved model and scaler files  
- `app` -  Streamlit app for live prediction  

## Results
- Model achieved ROC-AUC score of around 0.98.  
- Balanced precision and recall using SMOTE.  
- Exported predictions for further analysis and visualization.


---

### Author  
*Shahd Yasser Elsayed*  
Computer Science Major  
[Benha National University]  
[http://www.linkedin.com/in/shahdyasserelsayed]

To install required packages:
```bash
pip install -r requirements.txt

(Optional) To run the Streamlit app for live predictions, open your terminal or PowerShell and execute:  
```bash
cd C:\Users\starr\OneDrive\Desktop\fraud_detection_project\app
streamlit run app.py

>>>>>>> c68dbc3 (Initial commit with Git LFS for large CSV files)


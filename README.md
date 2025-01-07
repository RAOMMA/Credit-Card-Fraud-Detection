# Credit Card Fraud Detection

This Python script is designed to predict whether a credit card transaction is likely to be fraudulent or not based on various features. It utilizes a pre-trained machine learning model to make predictions.

## Dataset

- **Dataset Name**: Credit Card Fraud dataset
- **Data Source**: upload on git
- The dataset contains the following attributes:
  - Feature columns (30): Numerical values representing various features of credit card transactions.
  - Target column: Binary variable (0 for normal transaction, 1 for fraudulent transaction).

## Project Structure

- **README.md**: Documentation of the project.
- **fraud_detection.py**: Python script for making credit card fraud predictions.
- **model.joblib**: Pre-trained machine learning model for fraud detection.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd credit-card-fraud-detection
2. Create a virtual environment (recommended) and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use: venv\Scripts\activate

## Usage

-Clone this repository to your local machine.

-Ensure you have the pre-trained machine learning model ('model.joblib') in the same directory as the script ('fraud_detection.py').

-Open a command prompt or terminal and navigate to the directory where the script is located.

-Run the script with the necessary arguments for credit card transaction features.

## For example:
    ''' python main.py --Time 0.0, --V1 -1.359807, --V2 -0.072781, --V3 2.536347, --V4 1.378155, --V5 -0.338321, --V6 0.462388, --V7 0.239599, --V8 0.098698, --V9 0.363787, --V10 0.32442, --V11 0.3424, --V12 0.8593, --V13 0.75356, --V14 0.34535, --V15 0.234233, --V16 -1.359807, --V17 -0.072781, --V18 2.536347, --V19 1.378155, --V20 -0.338321, --V21 0.462388, --V22 0.239599, --V23 0.098698, --V24 0.363787, --V25 0.4324, --V26 -0.021053, --V27 0.6562, --V28 -0.021053, --Amount 149.62  


Follow the instructions in the script to make predictions.

## Model Training
The project uses a machine learning model to classify credit card transactions into two classes: normal and fraudulent. The pre-trained model is saved as 'model.joblib'.

## Evaluation
The script provides binary predictions. You can evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.

## Results
The project provides predictions for credit card fraud based on the input features. The performance of the model may vary depending on the dataset used.

## Future Improvements
There are several ways to improve the model and the project:

- Explore more advanced machine learning techniques.
  
- Fine-tune hyperparameters for better model performance.
  
- Gather more labeled data for improved accuracy.
## References

- Author: Mirza Salman
- Contact: salmansaluu661@gmail.com

Feel free to customize this README to include any additional information you want to provide about the project.


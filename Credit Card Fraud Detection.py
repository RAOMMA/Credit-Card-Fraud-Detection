import joblib
import pandas as pd
import argparse

# Load your encoder and model
loaded_model = joblib.load('C:/salman/ML/Credit Card Fraud Detection/model.joblib')

def predict_heart_disease(args):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame({
        'Time': [args.Time],
        'V1': [args.V1],
        'V2': [args.V2],
        'V3': [args.V3],
        'V4': [args.V4],
        'V5': [args.V5],
        'V6': [args.V6],
        'V7': [args.V7],
        'V8': [args.V8],
        'V9': [args.V9],
        'V10': [args.V10],
        'V11': [args.V11],
        'V12': [args.V12],
        'V13': [args.V13],
        'V14': [args.V14],
        'V15': [args.V15],
        'V16': [args.V16],
        'V17': [args.V17],
        'V18': [args.V18],
        'V19': [args.V19],
        'V20': [args.V20],
        'V21': [args.V21],
        'V22': [args.V22],
        'V23': [args.V23],
        'V24': [args.V24],
        'V25': [args.V25],
        'V26': [args.V26],
        'V27': [args.V27],
        'V28': [args.V28],
        'Amount': [args.Amount]
    })

    # Make predictions
    prediction = loaded_model.predict(input_df)
    return prediction[0]

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='Heart Disease Prediction')
    parser.add_argument('--Time', type=float, required=True)
    parser.add_argument('--V1', type=float, required=True)
    parser.add_argument('--V2', type=float, required=True)
    parser.add_argument('--V3', type=float, required=True)
    parser.add_argument('--V4', type=float, required=True)
    parser.add_argument('--V5', type=float, required=True)
    parser.add_argument('--V6', type=float, required=True)
    parser.add_argument('--V7', type=float, required=True)
    parser.add_argument('--V8', type=float, required=True)
    parser.add_argument('--V9', type=float, required=True)
    parser.add_argument('--V10', type=float, required=True)
    parser.add_argument('--V11', type=float, required=True)
    parser.add_argument('--V12', type=float, required=True)
    parser.add_argument('--V13', type=float, required=True)
    parser.add_argument('--V14', type=float, required=True)
    parser.add_argument('--V15', type=float, required=True)
    parser.add_argument('--V16', type=float, required=True)
    parser.add_argument('--V17', type=float, required=True)
    parser.add_argument('--V18', type=float, required=True)
    parser.add_argument('--V19', type=float, required=True)
    parser.add_argument('--V20', type=float, required=True)
    parser.add_argument('--V21', type=float, required=True)
    parser.add_argument('--V22', type=float, required=True)
    parser.add_argument('--V23', type=float, required=True)
    parser.add_argument('--V24', type=float, required=True)
    parser.add_argument('--V25', type=float, required=True)
    parser.add_argument('--V26', type=float, required=True)
    parser.add_argument('--V27', type=float, required=True)
    parser.add_argument('--V28', type=float, required=True)
    parser.add_argument('--Amount', type=float, required=True)

    args = parser.parse_args()

    # Call the predict_heart_disease function with the parsed arguments
    prediction = predict_heart_disease(args)
    if prediction==0:
        print("Normal Transaction")
    else:
        print("fraudulent transaction")


   

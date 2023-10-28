# Import necessary libraries
import pickle
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Create a Flask app instance
app = Flask(__name)

# Enable cross-origin request handling for our application
cors = CORS(app)

# Load the ARIMA model from a pickled file
model = pickle.load(open("./output/arima_model.pkl", "rb"))

# Define an API route for a status check
@app.route('/check', methods=['GET'])
@cross_origin()
def return_status():
    return "Yay! Flask App is running and newly deployed"

# Define an API route for getting time series predictions
@app.route('/', methods=['GET'])
@cross_origin()
def return_model_prediction():
    try:
        # Get prediction results and respond
        # Since it's a GET request, no data is required, as we're handling a univariate time series model
        predictions = model.predict()
        final_four_predictions = list(predictions)[-4:]
        return {"status_code": 200, "message": "Success", "body": {"preds": final_four_predictions}}

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"status_code": 404, "message": f"Error: {e}"}

if __name__ == '__main__':
    # Start the Flask app and listen on all available network interfaces
    app.run("0.0.0.0")

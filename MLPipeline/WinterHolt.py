# Import the required libraries
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Set the Seaborn theme
sns.set_theme(style="darkgrid")

# Define a class for Winter-Holt analysis
class Winterholt:

    def holt(self, df_comp):
        # Create a Holt-Winter Exponential Smoothing model
        hw_model = ExponentialSmoothing(df_comp.Healthcare.tolist())
        model_fit = hw_model.fit()

        # Make predictions
        yhat = model_fit.predict(1, len(df_comp))
        # We are calling the model to predict all data points that are the same as the dataset to see the model's performance

        # Plot the actual and predicted values
        plt.figure(figsize=(20, 5))
        plt.plot(df_comp.Healthcare.tolist())
        plt.plot(yhat.tolist(), color='red')
        plt.title("Holt Winter Model Prediction Vs Actual Healthcare")
        plt.legend(["actual", "predicted"])
        plt.savefig("Output/holtwinter.png")

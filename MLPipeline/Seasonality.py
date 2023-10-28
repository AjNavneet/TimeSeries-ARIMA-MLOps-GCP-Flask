# Import the required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Set the Seaborn theme
sns.set_theme(style="darkgrid")

# Import seasonal decomposition function from statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose

# Define a class for Seasonality analysis
class Seasonality:

    def seasonality(self, df_comp):
        output = "./Output/"
        
        # Naive decomposition (Additive Model)
        # observed = Trend + Seasonal + Residual
        additive = seasonal_decompose(df_comp.Healthcare, model="additive")
        additive.plot()
        plt.savefig(output + "seasonal_additive.png")

        # Naive decomposition (Multiplicative Model)
        # observed = Trend * Seasonal * Residual
        multiplicative = seasonal_decompose(df_comp.Healthcare, model="multiplicative")
        multiplicative.plot()
        plt.savefig(output + "seasonal_multiplicative.png")

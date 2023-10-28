# Import the required libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
import statsmodels.graphics.tsaplots as sgt

# Set the Seaborn theme
sns.set_theme(style="darkgrid")

# Define a class for White Noise analysis
class WhiteNoise:

    # Generate white noise data for the Healthcare attribute
    def white_noise(self, df_comp):
        output = "./Output/"

        # Generate white noise with the same mean and standard deviation as Healthcare data
        wn = np.random.normal(loc=df_comp.Healthcare.mean(), scale=df_comp.Healthcare.std(), size=len(df_comp))
        df_comp["wn"] = wn

        # Plot the white noise time-series
        df_comp.wn.plot(figsize=(20, 5))
        plt.title("White noise time-series", size=24)
        plt.savefig(output + "whitenoise.png")

        # Plot the autocorrelation of white noise
        autocorrelation_plot(df_comp.wn)
        plt.savefig(output + "autocorr_wn.png")

        # Plot the autocorrelation of Healthcare data
        autocorrelation_plot(df_comp.Healthcare)
        plt.savefig(output + "autocorr_health.png")

        # Plot the ACF (Auto-Correlation Function) of white noise
        sgt.plot_acf(df_comp.wn, zero=False, lags=40)
        plt.title("ACF Of WN", size=20)
        plt.savefig(output + "acf_wn.png")

        # Plot the ACF of Healthcare data
        sgt.plot_acf(df_comp.Healthcare, zero=False, lags=40)
        plt.title("ACF Of Healthcare", size=20)
        plt.savefig(output + "acf_health.png")

# Import the required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import pylab
import statsmodels.tsa.stattools as sts

# Set the Seaborn theme
sns.set_theme(style="darkgrid")

# Define a class for Stationarity analysis
class Stationarity:

    def stationarity(self, df_comp):
        output = "./Output/"
        
        # Augmented Dickey-Fuller test for stationarity (White Noise)
        sts.adfuller(df_comp.wn)
        
        # Augmented Dickey-Fuller test for stationarity (Healthcare data)
        sts.adfuller(df_comp.Healthcare)
        
        # Create a Q-Q plot for White Noise
        scipy.stats.probplot(df_comp.wn, plot=pylab)
        plt.title("QQ plot for White Noise")
        pylab.savefig(output + "qq_wn.png")
        
        # Create a Q-Q plot for Healthcare data
        scipy.stats.probplot(df_comp.Healthcare, plot=pylab)
        plt.title("QQ plot for Healthcare")
        pylab.savefig(output + "qq_healthcare.png")

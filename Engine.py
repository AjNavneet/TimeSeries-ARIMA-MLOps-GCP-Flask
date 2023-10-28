# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import custom modules from the MLPipeline package
from MLPipeline.Stationarity import Stationarity
from MLPipeline.RandomWalk import RandomWalk
from MLPipeline.WhiteNoise import WhiteNoise
from MLPipeline.Seasonality import Seasonality
from MLPipeline.WinterHolt import Winterholt
from MLPipeline.ARIMA import ARIMA_Model

# Import the data from the Excel file
raw_csv_data = pd.read_excel("./Input/CallCenterData.xlsx")

# Create a copy of the data for further processing
df_comp = raw_csv_data.copy()

# Set the 'month' column as the index
df_comp.set_index("month", inplace=True)

# Set the frequency of the data to monthly
df_comp = df_comp.asfreq('M')

# Plot the 'Healthcare' column with a specified figure size and title
df_comp.Healthcare.plot(figsize=(20, 5), title="Healthcare")

# Save the plot as an image file
plt.savefig("Output/healthcare.png")

# Perform White Noise analysis
WhiteNoise().white_noise(df_comp)

# Perform Random Walk analysis
RandomWalk().random_walk()

# Perform Stationarity analysis
Stationarity().stationarity(df_comp)

# Perform Seasonality analysis
Seasonality().seasonality(df_comp)

# Perform Winter-Holt analysis
Winterholt().holt(df_comp)

# Perform ARIMA Model analysis
ARIMA_Model().compute(df_comp)

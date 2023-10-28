# Import the required libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set the Seaborn theme
sns.set_theme(style="darkgrid")

# Define a class for Random Walk
class RandomWalk:

    def random_walk(self):
        # Random Walk
        output = "./Output/"
        walk = [99]  # Initial value of the walk

        noise1 = []  # To store the random noise

        # Generate the random walk data
        for i in range(1900):
            # Create random noise: -1 or 1 with equal probability
            noise = -1 if np.random.random() < 0.5 else 1
            noise1.append(noise)
            walk.append(walk[-1] + noise)

        # Plot the random walk
        plt.plot(walk)
        plt.figure(figsize=(20, 5))
        plt.savefig(output + "randomwalk.png")

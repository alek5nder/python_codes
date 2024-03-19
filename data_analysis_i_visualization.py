import argparse as arg  # Importing the argparse module for command-line argument parsing
import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot module for creating plots
import numpy as np  # Importing the numpy module for generating random data
import pandas as pd  # Importing the pandas module for working with tabular data

# Creating a command-line argument parser
parser = arg.ArgumentParser()
parser.add_argument("size", help="Number of randomly generated digits")
parser.add_argument("quiet",  help="Volume")
args = parser.parse_args()

# Generating and visualizing a time series of random numbers using Pandas and Matplotlib
plt.figure()
ts = pd.Series(np.random.randn(int(args.size)), index=pd.date_range("1/1/2020", periods=int(args.size)))
ts = ts.cumsum()  # Computing the cumulative sum of data

ts.plot()  # Creating a time series plot
plt.show()  # Displaying the plot
plt.close("Figure 1")  # Closing the plot

# Generating and visualizing a DataFrame using Pandas and Matplotlib
df = pd.DataFrame(np.random.randn(int(args.size), 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()

df.plot()  # Creating a DataFrame plot
plt.show()  # Displaying the plot

# Generating and visualizing a line and scatter plot of a DataFrame
df3 = pd.DataFrame(np.random.randn(int(args.size), 2), columns=["B", "C"]).cumsum()
df3["A"] = pd.Series(list(range(len(df))))

df3.plot(x="A", y="B")  # Creating a line plot
df3.plot(x="A")  # Creating a scatter plot
plt.show()  # Displaying the plots

# Generating and visualizing a bar plot of a DataFrame
df.iloc[10].plot(kind="bar")
plt.show()  # Displaying the plot

# Generating and visualizing a pie chart of a DataFrame
df = pd.DataFrame(np.random.rand(int(args.size), 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()

df.iloc[10].plot(kind="pie")
plt.show()  # Displaying the plot

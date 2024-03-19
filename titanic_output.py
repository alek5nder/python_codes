#example of execute: >>python zadPandas02.py -i titanic.csv -o output.csv -f csv 20 40 -v<< filters passengers from 20 to 40 years old
#the code uses titanic.csv as input data
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt

# Argument parsing
parser = argparse.ArgumentParser(description="Process Titanic data.")
parser.add_argument("-i", "--input", type=str, help="Input file name")
parser.add_argument("-o", "--output", type=str, help="Output file name")
parser.add_argument("-f", "--format", type=str, help="File format")
parser.add_argument("age_range", nargs=2, type=int, help="Age range")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
args = parser.parse_args()

# Read input file
if args.input:
    titanic = pd.read_csv(args.input)
else:
    titanic = pd.read_csv("titanic.csv")

# Apply age range filter
if args.age_range:
    titanic = titanic[(titanic["Age"] >= args.age_range[0]) & (titanic["Age"] <= args.age_range[1])]

# Print verbose info
if args.verbose:
    print("Data loaded successfully.")

# Print loaded data
print(titanic)

# Generate bar plot of passengers based on age
age_counts = titanic['Age'].value_counts().sort_index()
plt.bar(age_counts.index, age_counts.values)
plt.xlabel('Age')
plt.ylabel('Passenger Count')
plt.title('Passenger Count by Age')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # -------- First Line of Best Fit (All Data) --------
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_extended = np.arange(df["Year"].min(), 2051)
    line1 = res1.slope * years_extended + res1.intercept

    plt.plot(years_extended, line1, color="red")

    # -------- Second Line (from year 2000) --------
    df_recent = df[df["Year"] >= 2000]

    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    years_recent = np.arange(2000, 2051)
    line2 = res2.slope * years_recent + res2.intercept

    plt.plot(years_recent, line2, color="green")

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    return plt.gcf()
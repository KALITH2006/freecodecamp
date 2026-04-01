import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# 2. Clean data (remove top & bottom 2.5%)
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


# --------- LINE PLOT ---------
def draw_line_plot():
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line.index, df_line["value"], color="red")

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    return fig


# --------- BAR PLOT ---------
def draw_bar_plot():
    df_bar = df.copy()

    # Extract year & month
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Group data
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Ensure correct month order
    months_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df_bar = df_bar[months_order]

    fig = df_bar.plot(kind="bar", figsize=(12, 6)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    return fig


# --------- BOX PLOT ---------
def draw_box_plot():
    df_box = df.copy().reset_index()

    # Prepare data
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    # Month order
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=month_order,
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    return fig
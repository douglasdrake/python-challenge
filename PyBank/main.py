# Load the dependencies
import os
import pandas as pd

# Define input and output paths
BUDGET_FILE = "budget_data.csv"
BUDGET_DIRECTORY = "Resources"
BUDGET_PATH = os.path.join("", BUDGET_DIRECTORY)
OUTPUT_FILE = "budget_summary.csv"
OUTPUT_DIRECTORY = "Resources"
OUTPUT_PATH = os.path.join("", OUTPUT_DIRECTORY)

# Load the data
def load_budget_data(budget_path = BUDGET_PATH, budget_file = BUDGET_FILE):
    csv_path = os.path.join(budget_path, budget_file)
    return pd.read_csv(csv_path)

# Compute the required summaries and return the results in a 
# pandas dataframe
def summarize_budget_data(budget_df):
    results_df = pd.DataFrame()
    # Get the number of months
    results_df['Number of months'] = [budget_df["Date"].nunique()]
    
    # Get a column of changes
    budget_df['Change'] = budget_df["Profit/Losses"].diff()

    # Find the min and max change
    min_profit_row = budget_df["Change"].idxmin()
    max_profit_row = budget_df["Change"].idxmax()
    results_df['Minimum'] = budget_df.iloc[min_profit_row, 2]
    results_df['Minimum month'] = budget_df.iloc[min_profit_row, 0]
    results_df['Maximum'] = budget_df.iloc[max_profit_row, 2]
    results_df['Maximum month'] = budget_df.iloc[max_profit_row, 0]

    # Find the average change and total for profit/losses
    results_df['Average'] = budget_df["Change"].mean()
    results_df['Total'] = budget_df["Profit/Losses"].sum()

    return results_df

# Print the results to standard output
def print_budget_results(results_df):
    print("")
    print("Financial Analysis")
    print("-"*60)
    print(f"Total Months: {results_df['Number of months'][0]}")
    print(f"Total: ${results_df['Total'][0]}")
    print(f"Average Change: ${results_df['Average'][0]:.2f}")
    print(f"Greatest Increase in Profits: {results_df['Maximum month'][0]} (${results_df['Maximum'][0]:.0f})")
    print(f"Greatest Decrease in Profits: {results_df['Minimum month'][0]} (${results_df['Minimum'][0]:.0f})")

# Write the results as a csv file
def write_budget_results(results_df, output_path = OUTPUT_PATH, output_file = OUTPUT_FILE):
    csv_path = os.path.join(output_path, output_file)
    results_df.to_csv(csv_path, index=False)

# Small function to perform all steps
def analyze_budget_data():
    budget_df = load_budget_data()
    results_df = summarize_budget_data(budget_df)
    print_budget_results(results_df)
    write_budget_results(results_df)

analyze_budget_data()


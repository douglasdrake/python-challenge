#
import os
import pandas as pd

BUDGET_FILE = "budget_data.csv"
BUDGET_DIRECTORY = "Resources"
BUDGET_PATH = os.path.join("", BUDGET_DIRECTORY)
OUTPUT_FILE = "budget_summary.csv"
OUTPUT_DIRECTORY = "Output"
OUTPUT_PATH = os.path.join("..", OUTPUT_DIRECTORY)

def load_budget_data(budget_path = BUDGET_PATH, budget_file = BUDGET_FILE):
    csv_path = os.path.join(budget_path, budget_file)
    return pd.read_csv(csv_path)

def summarize_budget_data(budget_df):
    results_df = pd.DataFrame()
    # Get the number of months
    results_df['Number of months'] = [budget_df["Date"].nunique()]
    
    # Get a column of changes
    budget_df['Change'] = budget_df["Profit/Losses"].diff()

    # Find the min and max
    min_profit_row = budget_df["Change"].idxmin()
    max_profit_row = budget_df["Change"].idxmax()
    results_df['Minimum'] = budget_df.iloc[min_profit_row, 2]
    results_df['Minimum month'] = budget_df.iloc[min_profit_row, 0]
    results_df['Maximum'] = budget_df.iloc[max_profit_row, 2]
    results_df['Maximum month'] = budget_df.iloc[max_profit_row, 0]

    results_df['Average'] = budget_df["Change"].mean()
    results_df['Total'] = budget_df["Profit/Losses"].sum()

    return results_df

def print_budget_results(results_df):
    print("Financial Analysis")
    print("-"*66)
    print(f"Total Months: {results_df['Number of months'][0]}")
    print(f"Total: ${results_df['Total'][0]}")
    print(f"Average Change: ${results_df['Average'][0]}")
    print(f"Greatest Increase in Profits: {results_df['Maximum month'][0]} (${results_df['Maximum'][0]})")
    print(f"Greatest Decrease in Profits: {results_df['Minimum month'][0]} (${results_df['Minimum'][0]})")

def write_budget_results(results_df, output_path = OUTPUT_PATH, output_file = OUTPUT_FILE):
    csv_path = os.path.join(output_path, output_file)
    results_df.to_csv()

def analyze_budget_data():
    budget_df = load_budget_data()
    results_df = summarize_budget_data(budget_df)
    print_budget_results(results_df)
    write_budget_results(results_df)

analyze_budget_data()

#budget_data = load_budget_data()
#print(summarize_budget_data(budget_data))


# Load the dependencies
import os
import csv

# Define input and output paths
BUDGET_FILE = "budget_data.csv"
BUDGET_DIRECTORY = "Resources"
BUDGET_PATH = os.path.join("", BUDGET_DIRECTORY)
OUTPUT_FILE = "old-budget_summary.csv"
OUTPUT_DIRECTORY = "Resources"
OUTPUT_PATH = os.path.join("", OUTPUT_DIRECTORY)

# Load the data and return a list of lists
def load_budget_data(budget_path = BUDGET_PATH, budget_file = BUDGET_FILE):

    csv_path = os.path.join(budget_path, budget_file)
    with open(csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")

        # skip the header row
        next(csv_reader)

        # read the rows in - it will be a list of tuples
        data = [row for row in csv_reader]
    
        # create two tuples of data - first contains all months
        # second contains the corresponding profits/losses
        month, profit = zip(*data)
    
        # convert profit to a number
        profit = [int(item) for item in profit]

    return month, profit

def summarize_budget_data(month, profit):
    # Set up an empty dictionary to return the summary numbers
    # This allows us to have named fields 
    results = {}

    # Get the number of months
    results['Number of months'] = len(month)
    
    # Get the total profit
    results['Total'] = sum(profit)

    # Get a list of changes
    change = [next - last for next, last in zip(profit[1:], profit[:-1])]

    # minimum change
    min_change = min(change)
    min_pos = change.index(min_change)
    results['Minimum'] = min_change
    results['Minimum month'] = month[min_pos + 1]

    # maximum change
    max_change = max(change)
    max_pos = change.index(max_change)
    results['Maximum'] = max_change
    results['Maximum month'] = month[max_pos + 1]
    
    # average change
    results['Average'] = sum(change) / len(change)
    return results

# Print the results to standard output
def print_budget_results(results_dict):
    print("")
    print("Financial Analysis")
    print("-"*60)
    print(f"Total Months: {results_dict['Number of months']}")
    print(f"Total: ${results_dict['Total']}")
    print(f"Average Change: ${results_dict['Average']:.2f}")
    print(f"Greatest Increase in Profits: {results_dict['Maximum month']} (${results_dict['Maximum']:.0f})")
    print(f"Greatest Decrease in Profits: {results_dict['Minimum month']} (${results_dict['Minimum']:.0f})")

# Write the results as a csv file
# The header row is given by the keys of results_dict
# The values row is given by the items of results_dict
def write_budget_results(results_dict, output_path = OUTPUT_PATH, output_file = OUTPUT_FILE):
    header = [*results_dict.keys()]
    #values = [*results_dict.values()]

    csv_path = os.path.join(output_path, output_file)
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

        # there is only one row of results - write it out
        writer.writerow(results_dict)
            
# Small function to perform all steps
def analyze_budget_data():
    month, profit = load_budget_data()
    results = summarize_budget_data(month, profit)
    print_budget_results(results)
    write_budget_results(results)
 
analyze_budget_data()

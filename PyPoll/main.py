# Douglas Drake \python-challenge\PyPoll\main.py

# Load the dependencies
import os
import pandas as pd

# Define input and output paths
ELECTION_FILE = "election_data.csv"
ELECTION_DIRECTORY = "Resources"
ELECTION_PATH = os.path.join("", ELECTION_DIRECTORY)
OUTPUT_FILE = "election_summary.csv"
OUTPUT_DIRECTORY = "Resources"
OUTPUT_PATH = os.path.join("", OUTPUT_DIRECTORY)

# Load the data
def load_election_data(election_path = ELECTION_PATH, election_file = ELECTION_FILE):
    csv_path = os.path.join(election_path, election_file)
    return pd.read_csv(csv_path)

# Compute the required summaries and return the results in a 
# pandas dataframe with columns: Candidate, Total Votes, and Percent
def summarize_election_data(election_df):
    results_df = pd.DataFrame()

    # the value_counts method returns the results in descending order
    vote_counts = election_df['Candidate'].value_counts()
    total_votes = vote_counts.sum()
    
    # Construct the data frame.  Set the index to be integer based
    # and rename the columns
    results_df = pd.DataFrame(vote_counts).reset_index()
    results_df = results_df.rename(columns = {'index' : 'Candidate', 'Candidate' : 'Total Votes'})
    results_df['Percent'] = results_df['Total Votes'].apply(lambda x: 100 * x/ total_votes)
    
    return results_df

# Print the results to standard output
def print_election_results(results_df):
    # Define two helper functions for printing the output
    def max_line_length(df):
        # Determine the longest line of output
        max_name_length = df['Candidate'].apply(lambda x: len(x)).max()
        max_vote_length = df['Total Votes'].apply(lambda x: len(str(x))).max()
        # 1 ':', 2 '()', 1 '%' and 2 spaces and percentage is 6 wide
        return max_name_length + max_vote_length + 12

    def print_separator(n):
        print("-" * n)
 
    width = max_line_length(results_df)
    
    print("Election Results")
    print_separator(width)
    
    print(f"Total Votes: {results_df['Total Votes'].sum()}")
    print_separator(width)

    # iterate over each row printing the results
    for row in results_df.itertuples():
        print(f"{row[1]}: {row[3]:6.3f}% ({row[2]})")
    
    print_separator(width)
    
    # Our data frame gives the vote counts in descending order
    # The winner is the first row
    print(f"Winner: {results_df.loc[0, 'Candidate']}")
    print_separator(width)

# Write the results as a csv file
def write_election_results(results_df, output_path = OUTPUT_PATH, output_file = OUTPUT_FILE):
    csv_path = os.path.join(output_path, output_file)
    results_df.to_csv(csv_path, index=False)

# Small function to perform all steps
def analyze_election_data():
    election_df = load_election_data()
    results_df = summarize_election_data(election_df)
    print_election_results(results_df)
    write_election_results(results_df)

analyze_election_data()

import pandas as pd
import os

"""In this script we will convert the sport odds to the true 
   probabilities that bookmaker uses."""

DATASETS_file = "../cleaning"
csv_file = "matches_cleaned.csv"

# Load and read the data
csv_file_path = os.path.join(DATASETS_file, csv_file)
matches_df = pd.read_csv(filepath_or_buffer=csv_file_path)

## Convert the odds to percentages

# First we will calculate the implied probabilities by dividing 1 by each decimal odd, h_odd, d_odd, and a_odd.
# The total bookmaker estimated probability is > 1. This means that we have the sum of fair odds (=1) plus the over-round which
# the bookmaker adds to the decimal odds for an event E. The over-round effectively reduces the odds, making them unfair for the bettor.
matches_df['h_implied_prob'] = 1/matches_df['h_odd']
matches_df['d_implied_prob'] = 1/matches_df['d_odd']
matches_df['a_implied_prob'] = 1/matches_df['a_odd']
matches_df['bookmaker_total_prob'] = matches_df['h_implied_prob'] + matches_df['d_implied_prob'] + matches_df['a_implied_prob']

# In order to make the sum of implied probabilities equal to 1 we will re-normalize by dividing each implied probability again by the bookmaker_total_prob.
# In this way we will take the true percentages that bookmaker uses.
matches_df['h_real_prob'] = matches_df['h_implied_prob']/matches_df['bookmaker_total_prob']
matches_df['d_real_prob'] = matches_df['d_implied_prob']/matches_df['bookmaker_total_prob']
matches_df['a_real_prob'] = matches_df['a_implied_prob']/matches_df['bookmaker_total_prob']
matches_df['real_total_prob'] = matches_df['h_real_prob'] + matches_df['d_real_prob'] + matches_df['a_real_prob']

matches_df.dropna(inplace=True)
matches_df.to_csv("matches_prep.csv", index=False)
print("file 'matches_prep.csv' succesfully saved")
# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = "/Users/Claudia/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Ensure the 'analysis' folder exists inside the PyPoll folder
poll_folder = os.path.dirname(file_to_load)  # Get the PyPoll folder path
output_folder = os.path.join(poll_folder, "analysis")  # Create an analysis folder inside PyPoll
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

file_to_output = os.path.join(output_folder, "election_analysis.txt")

# Debugging: Print file paths
print(f"File to load: {file_to_load}")
print(f"File to output: {file_to_output}")

# Check if the input file exists
if not os.path.exists(file_to_load):
    print(f"Error: The file '{file_to_load}' does not exist.")
else:
    # Define variables
    total_votes = 0  # Total votes counter
    candidate_votes = {}  # Dictionary to track each candidate's votes
    winning_candidate = ""  # Track the winning candidate
    winning_count = 0  # Track the winning vote count
    winning_percentage = 0  # Track the winning vote percentage

    # Open and read the CSV file
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Skip the header row
        header = next(reader)

        # Loop through each row of data
        for row in reader:
            # Increment total vote count
            total_votes += 1

            # Extract the candidate name from the row
            candidate_name = row[2]

            # If candidate is not in the dictionary, add them
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0

            # Increment the candidate's vote count
            candidate_votes[candidate_name] += 1

    # Open the output text file to save results
    with open(file_to_output, "w") as txt_file:
        # Generate election results header
        election_results = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n"
        )
        print(election_results, end="")
        txt_file.write(election_results)

        # Loop through each candidate's data
        for candidate, votes in candidate_votes.items():
            # Calculate vote percentage
            vote_percentage = (votes / total_votes) * 100

            # Check if this candidate is the new winner
            if votes > winning_count:
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage

            # Generate candidate's results
            candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(candidate_results, end="")
            txt_file.write(candidate_results)

        # Generate the winner's summary
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.3f}%\n"
            f"-------------------------\n"
        )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

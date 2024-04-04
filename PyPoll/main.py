import csv
import os

file_path = "./Resources/election_data.csv"
output_path = "./analysis/election_analysis.txt"

total_votes =0

candidate_options = []
candidate_votes = {}

winning_candidate =""
winning_count = 0

with open(file_path) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        print(", ", end = "")

        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(output_path, "w") as text_file:
    election_results = (
        f"\n\nElection Results\n"
        f"------------------------------"
        f"Total Votes : {total_votes}\n"
        f"------------------------------"
    )
    print(election_results)

    text_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) *100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_ouput = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        print(voter_ouput, end = "")

        text_file.write(voter_ouput)

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    text_file.write(winning_candidate_summary)
#Ji-Heon Kim
#PyPoll
#main.py

import os
import csv

# Set file path

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)

    listOfVotes = []
    listOfCandidates = []
    totalVoteCount = 0
    candidateVoteCount = {}

    # Read each row of data after the header.  Add 1 to vote count for each row.
    for row in csvreader:
        totalVoteCount += 1
        listOfVotes.append(row[2])
    
    listOfCandidates = list(set(listOfVotes)) #unique list of all candidates

    numVotes = 0
    winningVoteCount = 0
    currentWinner = ""

    # For each candidate, count number of votes.
    for candidate in listOfCandidates:
        for candidateName in listOfVotes:
            if candidate == candidateName:
                numVotes += 1
        candidateVoteCount[candidate] = numVotes
    
    # Keep track of the highest vote count and who the current winner is
    
        if numVotes > winningVoteCount:
            currentWinner = candidate
            winningVoteCount = numVotes
        numVotes = 0

# Print results to console, including Total vote count and votes per candidate.  Print winning candidates name.

print("\n")
print(f"Election Results")
print("-----------------------")
print(f"Total Votes: {totalVoteCount}")
print("-----------------------")

for candidateName in sorted(candidateVoteCount, key=candidateVoteCount.get, reverse = True):
    print(f'{candidateName}: {round(candidateVoteCount[candidateName]/totalVoteCount*100,3)}% ({candidateVoteCount[candidateName]})')

print("-----------------------")
print(f'Winner: {currentWinner}')
print("-----------------------")

# Export results that were printed to console to text file "voteCount.txt"

outputFile = open("voteCount.txt", "w")

outputFile.write(f"Election Results\n")
outputFile.write("-----------------------\n")
outputFile.write(f"Total Votes: {totalVoteCount}\n")
outputFile.write("-----------------------\n")

for candidateName in sorted(candidateVoteCount, key=candidateVoteCount.get, reverse = True):
    outputFile.write(f'{candidateName}: {round(candidateVoteCount[candidateName]/totalVoteCount*100,3)}% ({candidateVoteCount[candidateName]})\n')

outputFile.write("-----------------------\n")
outputFile.write(f'Winner: {currentWinner}')
outputFile.write("-----------------------\n")
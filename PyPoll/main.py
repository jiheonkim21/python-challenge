import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)

    listOfVotes = []
    listOfCandidates = []
    totalVoteCount = 0
    candidateVoteCount = {}

    # Read each row of data after the header
    for row in csvreader:
        totalVoteCount += 1
        listOfVotes.append(row[2])
    
    listOfCandidates = list(set(listOfVotes))

    numVotes = 0
    winningVoteCount = 0
    currentWinner = ""

    for candidate in listOfCandidates:
        for candidateName in listOfVotes:
            if candidate == candidateName:
                numVotes += 1
        candidateVoteCount[candidate] = numVotes
        if numVotes > winningVoteCount:
            currentWinner = candidate
            winningVoteCount = numVotes
        numVotes = 0

# Print results to console

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

# Export to text file "voteCount.txt"

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
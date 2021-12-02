import os
import csv
from collections import Counter

# Settign a variable for the current file using os.path.join to allow for different operating systems
election_csv = os.path.join('Resources', 'election_data.csv')

# reading in the file and creating an iterator to access the data in the file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    csv_header = next(csvreader)

    # set variable to count total votes
    total_votes = 0

    # create a set to track candidates who received votes
    candidates = []
   
    # iterating through the data
    for i in csvreader:

        #count the total number of votes 
        total_votes += 1

        #append each entry of the candidates' name to the the candidates list 
        candidates.append(i[2])

    #count the number of times each of the candidates' names appears in the list
    count = Counter(candidates)

    # set variable for the winner
    winner = (count.most_common(1)[0][0])

    #print the results to the terminal 
    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {total_votes} ")
    print("----------------------------------")

    #iterate through the counter. Print the candidates name: percentage of the votes received and the total count
    for i in count:
        print(f"{i}: {round((count[i]/total_votes) *100)}% ({count[i]})")
        
    print("----------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------")

#open a text file
output_file = os.path.join("election_results.txt")

#output to the text file 
with open(output_file, 'w') as text_file:
    text_file.writelines("Election Results\n")
    text_file.writelines(f"----------------------------------\n")
    text_file.writelines(f"Total Votes: {total_votes} \n")
    text_file.writelines("----------------------------------\n")

    #iterate through the counter. Print the candidates name: percentage of the votes received and the total count
    for i in count:
        text_file.writelines(f"{i}: {round((count[i]/total_votes) *100)}% ({count[i]}) \n")

    text_file.writelines(f"----------------------------------\n")
    text_file.writelines(f"Winner: {winner}\n")
    text_file.writelines(f"----------------------------------\n")


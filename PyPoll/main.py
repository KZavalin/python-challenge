#Load dependencies
import csv
import os
#set initial variables
votes=0
candidate_list=[]
votes_list=[]
print_list=["Election Results",
            "----------------------------"]
max=0
#Open file
file = os.path.join("Resources", "election_data.csv")
with open(file) as csv_file:
    election_data=csv.reader(csv_file)
    header=next(election_data)
    #The total number of votes cast
    for row in election_data:
        votes+=1
        votes_list.append(row[2])
        #A complete list of candidates who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
print_list.extend( [f'Total Votes: {votes}',
 "----------------------------"])            
for i in candidate_list:
     #The total number of votes each candidate won
    v=votes_list.count(i)
    #The percentage of votes each candidate won
    percent=round(100*v/votes,3)
    print_list.append(f'{i}: {percent}% ({v})')
    #The winner of the election based on popular vote
    if v>max:
        max=v
        winner=i
print_list.extend([ "----------------------------", f'Winner: {winner}',
 "----------------------------"])  
#Print/save results as text file
savepath = os.path.join("election_results.txt")
with open(savepath, 'w') as summary:
    for line in print_list:
        summary.write(line)
        summary.write('\n')
        print(line)
        
#Expected results
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------
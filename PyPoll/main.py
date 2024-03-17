import pandas as pd

# Create a DataFrame from the provided data
#poll = pd.read_csv("C:/Users/Priscy/Desktop/GitHubRepository/Python_Challenge/PyPoll/Resources.csv")
poll = pd.read_csv("PyPoll/election_data.csv")

#Total Votes
#poll["County"].count()
total_votos = poll["County"].count()

#Candidates
#poll["Candidate"].unique()
#print(f"Raymon Anthony Doane % {cand3}")
cand1 = poll.groupby("Candidate").count()["County"]["Charles Casper Stockham"]
cand2 = poll.groupby("Candidate").count()["County"]["Diana DeGette"]
cand3 = poll.groupby("Candidate").count()["County"]["Raymon Anthony Doane"]

#Porcentage Candidate
#print(f"Charles Casper Stockham {pc_cand1}% {cand1}")
pc_cand1 = poll.groupby("Candidate").count()["County"]["Charles Casper Stockham"]/poll["County"].count() * 100
pc_cand2 = poll.groupby("Candidate").count()["County"]["Diana DeGette"]/poll["County"].count() * 100
pc_cand3 = poll.groupby("Candidate").count()["County"]["Raymon Anthony Doane"]/poll["County"].count() * 100

#Winner
#print(f"Winner: {poll['Candidate'].describe()['top']}")
Winner = poll['Candidate'].describe()['top']

print(f'''
Election Results:
      
--------------------------------------------------
      
Total votes: {total_votos}

--------------------------------------------------

Charles Casper Stockham: {pc_cand1}% ({cand1})

Diana DeGette: {pc_cand2}% ({cand2})

Raymon Anthony Doane: {pc_cand3}% ({cand3})

--------------------------------------------------

Winner: {poll['Candidate'].describe()['top']}

--------------------------------------------------
''')

archivo = open("analysispypoll.txt","w")
archivo.write(f'''
Election Results:
      
--------------------------------------------------
      
Total votes: {total_votos}

--------------------------------------------------

Charles Casper Stockham: {pc_cand1}% ({cand1})

Diana DeGette: {pc_cand2}% ({cand2})

Raymon Anthony Doane: {pc_cand3}% ({cand3})

--------------------------------------------------

Winner: {poll['Candidate'].describe()['top']}

--------------------------------------------------
''')
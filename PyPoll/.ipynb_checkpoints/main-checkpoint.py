import pandas as pd
from pathlib import Path
import locale



# I imported the csv file using pandas
poll_csv = Path("Resources/election_data.csv")
poll_df = pd.read_csv (poll_csv, encoding="utf-8")


# I counted all the votes from the column Ballot ID using the count function
total_votes = poll_df["Ballot ID"].count()


candidates = poll_df["Candidate"].unique()
candidate_total = poll_df['Candidate'].value_counts()

#for each candidate i use.loc to find all the values containing the name of the candidate and use those to get the percentage and the total votes
candidate_charles = poll_df.loc[poll_df["Candidate"] == 'Charles Casper Stockham']
charles_votes = candidate_charles.count()
charles_per = charles_votes/total_votes *100
charles_per = round(charles_per[1],3)
charles_total= (candidate_charles, charles_votes)


#for each candidate i use.loc to find all the values containing the name of the candidate and use those to get the percentage and the total votes
candidate_diana = poll_df.loc[poll_df["Candidate"] == 'Diana DeGette']
diana_votes = candidate_diana.count()
diana_per = diana_votes/total_votes *100
diana_per = round(diana_per[1],3)
diana_total= (candidate_diana, diana_votes)


#for each candidate i use.loc to find all the values containing the name of the candidate and use those to get the percentage and the total votes
candidate_raymond = poll_df.loc[poll_df["Candidate"] == 'Raymon Anthony Doane']
raymond_votes = candidate_raymond.count()
raymond_per = raymond_votes/total_votes *100
raymond_per = round(raymond_per[1],3)
raymond_total= (candidate_raymond, raymond_votes)


#to get the winner I used idmax which get the index of the max value
candidate_winner= candidate_total.idxmax()


print('Election results')
print('-------------------')
print('total_votes : ', total_votes)
print('-------------------')
print(candidates[0], " : ", charles_per,'%' " ", '(', charles_votes[1],')')
print(candidates[1], " : ", diana_per,'%', " ", '(', diana_votes[1],')')
print(candidates[2], ' : ', raymond_per,'%', ' ', '(', raymond_votes[1], ')')
print('-------------------')
print('Winner : ', candidate_winner)
